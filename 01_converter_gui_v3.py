from tkinter import *
from tkinter import messagebox
from datetime import datetime


class VolumeConverter:
    def __init__(self, master):
        self.master = master
        self.master.title("Volume Converter")
        self.master.resizable(False, False)

        self.unit_options = ['Liters', 'Gallons', 'Quarts', 'Cubic Meters', 'Cubic Feet']

        self.volume_frame = Frame(master, padx=10, pady=10)
        self.volume_frame.grid()

        self.volume_heading = Label(self.volume_frame, text="Volume Converter", font=("Arial", 16, "bold"))
        self.volume_heading.grid(row=0, column=0, columnspan=4)

        self.volume_entry1 = Entry(self.volume_frame, font=("Arial", 14), width=10)
        self.volume_entry1.grid(row=1, column=0, padx=5, pady=5)
        self.volume_entry1.bind('<KeyRelease>', self.convert_volume)

        self.equals_label = Label(self.volume_frame, text="=", font=("Arial", 14))
        self.equals_label.grid(row=1, column=1, padx=5, pady=5)

        self.volume_entry2 = Entry(self.volume_frame, font=("Arial", 14), width=10, state=DISABLED)
        self.volume_entry2.grid(row=1, column=2, padx=5, pady=5)

        self.selected_unit1 = StringVar()
        self.selected_unit1.set(self.unit_options[0])

        self.selected_unit2 = StringVar()
        self.selected_unit2.set(self.unit_options[1])

        self.unit_dropdown1 = OptionMenu(self.volume_frame, self.selected_unit1, *self.unit_options, command=self.convert_volume)
        self.unit_dropdown1.config(font=("Arial", 10), bg="#E6E6E6", width=10)
        self.unit_dropdown1.grid(row=2, column=0, padx=5, pady=5)
        self.unit_dropdown1.bind("<Button-1>", lambda event: self.unit_dropdown1.config(state="active"))

        self.unit_dropdown2 = OptionMenu(self.volume_frame, self.selected_unit2, *self.unit_options, command=self.convert_volume)
        self.unit_dropdown2.config(font=("Arial", 10), bg="#E6E6E6", width=10)
        self.unit_dropdown2.grid(row=2, column=2, padx=5, pady=5)
        self.unit_dropdown2.bind("<Button-1>", lambda event: self.unit_dropdown2.config(state="active"))

        self.swap_button = Button(self.volume_frame, text="\u2194", bg="#004C99", fg="#FFFFFF",
                                  font=("Arial", 12, "bold"), width=3, height=1, command=self.swap_units)
        self.swap_button.grid(row=2, column=1, padx=5, pady=5)

        self.help_button = Button(self.volume_frame, text="?", bg="#004C99", fg="#FFFFFF", font=("Arial", 12, "bold"), width=3, height=1, command=self.display_help)
        self.help_button.grid(row=3, column=1, padx=5, pady=5)

        self.view_logs_button = Button(self.volume_frame, text="View Logs", bg="#004C99", fg="#FFFFFF", font=("Arial", 12, "bold"), width=10, command=self.view_logs)
        self.view_logs_button.grid(row=3, column=0, padx=5, pady=5)

        self.save_button = Button(self.volume_frame, text="Save", bg="#004C99", fg="#FFFFFF", font=("Arial", 12, "bold"), width=10, command=self.save_conversion)
        self.save_button.grid(row=3, column=2, padx=5, pady=5)

        self.save_label = Label(self.volume_frame, text="", font=("Arial", 10), fg="#004C99", width=40)
        self.save_label.grid(row=4, column=0, columnspan=3, padx=5, pady=2)

        self.history = []

    def convert_volume(self, event=None):
        try:
            value = float(self.volume_entry1.get())
            unit_from = self.selected_unit1.get()
            unit_to = self.selected_unit2.get()

            conversion_factors = {
                'Liters': 1,
                'Gallons': 0.264172,
                'Quarts': 1.05669,
                'Cubic Meters': 0.001,
                'Cubic Feet': 0.0353147
            }

            converted_value = value * conversion_factors[unit_to] / conversion_factors[
                unit_from]  # Adjusted calculation
            self.volume_entry2.config(state=NORMAL)
            self.volume_entry2.delete(0, END)
            self.volume_entry2.insert(0, "{:.4f}".format(converted_value))
            self.volume_entry2.config(state=DISABLED)

        except ValueError:
            # Handle non-numeric input
            self.volume_entry2.config(state=NORMAL)
            self.volume_entry2.delete(0, END)
            self.volume_entry2.insert(0, "Invalid Input")
            self.volume_entry2.config(state=DISABLED)

    def swap_units(self):
        temp_unit = self.selected_unit1.get()
        self.selected_unit1.set(self.selected_unit2.get())
        self.selected_unit2.set(temp_unit)
        self.convert_volume()

    def save_conversion(self):
        try:
            value = float(self.volume_entry1.get())
            unit_from = self.selected_unit1.get()
            unit_to = self.selected_unit2.get()

            converted_value = float(self.volume_entry2.get())
            self.history.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), value, unit_from, converted_value, unit_to))
            self.save_label.config(text="Conversion saved to history.", fg="#004C99")

        except ValueError:
            # Handle non-numeric input
            self.save_label.config(text="Invalid input. Please enter numeric values.", fg="red")

    def view_logs(self):
        log_window = Toplevel(self.master)
        log_window.title("Conversion Logs")
        log_window.resizable(False, False)

        log_frame = Frame(log_window, padx=10, pady=10)
        log_frame.grid()

        logs_heading = Label(log_frame, text="Conversion Logs", font=("Arial", 16, "bold"))
        logs_heading.grid(row=0, column=0, columnspan=2)

        logs_text = "\n".join([f"{log[0]}: {log[1]} {log[2]} -> {log[3]} {log[4]}" for log in self.history])
        logs_label = Label(log_frame, text=logs_text, font=("Arial", 12))
        logs_label.grid(row=1, column=0, columnspan=2)

        export_frame = Frame(log_frame)
        export_frame.grid(row=2, column=0, columnspan=2)

        file_name_label = Label(export_frame, text="File Name:")
        file_name_label.grid(row=0, column=0)

        self.export_file_name = Entry(export_frame, font=("Arial", 10), width=20)
        self.export_file_name.grid(row=0, column=1)

        export_button = Button(export_frame, text="Export Logs", bg="#004C99", fg="#FFFFFF", font=("Arial", 10, "bold"), command=self.export_logs)
        export_button.grid(row=0, column=2)

    def export_logs(self):
        if not self.history:
            messagebox.showinfo("Export Logs", "No logs available to export.")
            return

        filename = self.export_file_name.get()
        if not filename:
            filename = datetime.now().strftime("conversion_logs_%Y%m%d_%H%M%S.txt")

        with open(filename, "w") as file:
            file.write("Date,Value,From Unit,Converted Value,To Unit\n")
            for log in self.history:
                file.write(",".join(map(str, log)) + "\n")

        messagebox.showinfo("Export Logs", f"Logs exported to {filename}")

    def display_help(self):
        help_text = "This program allows you to convert volumes between different units. \n\n" \
                    "1. Enter the volume you want to convert in the first field.\n" \
                    "2. Select the unit of the volume you entered from the dropdown menu next to it.\n" \
                    "3. Select the unit you want to convert to from the dropdown menu on the other side.\n" \
                    "4. The converted volume will be displayed in the second field.\n" \
                    "5. Click 'Save' to save the conversion to history.\n" \
                    "6. Click 'View Logs' to see all the previous conversions.\n" \
                    "7. You can export the conversion logs to a file by clicking 'Export Logs'."
        messagebox.showinfo("Help", help_text)


def main():
    root = Tk()
    app = VolumeConverter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
