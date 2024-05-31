from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import re


# Function to check the input
def check_input(value, unit_from, unit_to):
    try:
        value = float(value)
        if value < 0:
            return False, "Input value cannot be negative"
        conversion_factors = {
            'Liters': 1,
            'Gallons': 0.264172,
            'Quarts': 1.05669,
            'Cubic Meters': 0.001,
            'Cubic Feet': 0.0353147
        }
        if unit_from not in conversion_factors or unit_to not in conversion_factors:
            return False, "Selected units not found"
        return True, None
    except ValueError:
        return False, "Invalid input value"


# Function to convert volume
def convert_volume(value, unit_from, unit_to):
    try:
        value = float(value)
        conversion_factors = {
            'Liters': 1,
            'Gallons': 0.264172,
            'Quarts': 1.05669,
            'Cubic Meters': 0.001,
            'Cubic Feet': 0.0353147
        }
        converted_value = value * conversion_factors[unit_to] / conversion_factors[unit_from]
        return converted_value
    except ValueError:
        return "Invalid Input"

# Function to round the number


def round_number(number):
    return "{:.4f}".format(number)

# Function to display help


def display_help():
    help_text = ("This program allows you to convert volumes between different units.\n\n"
                 "1. Enter the volume you want to convert in the first field.\n"
                 "2. Select the unit of the volume you entered from the dropdown menu next to it.\n"
                 "3. Select the unit you want to convert to from the dropdown menu on the other side.\n"
                 "4. The converted volume will be displayed in the second field.\n"
                 "5. Click 'Save' to save the conversion to history.\n"
                 "6. Click 'View Logs' to see all the previous conversions.\n"
                 "7. You can export the conversion logs to a file by clicking 'Export Logs'.")
    messagebox.showinfo("Help", help_text)

# Function to swap units


def swap_units(unit1, unit2):
    return unit2, unit1

# Class to handle log viewing and exporting


class LogViewer:
    def __init__(self, master, history):
        self.master = master
        self.master.title("Conversion Logs")
        self.master.resizable(False, False)
        self.history = history

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
        self.style.configure("Treeview", font=("Helvetica", 10), rowheight=25)
        self.style.map("Treeview", background=[("selected", "blue")], foreground=[("selected", "white")])

        self.log_frame = Frame(master, padx=10, pady=10)
        self.log_frame.grid()

        self.tree = ttk.Treeview(self.log_frame,
                                 columns=("Date", "Time", "Value", "From Unit", "Converted Value", "To Unit"))
        self.tree.grid(row=0, column=0, columnspan=3, sticky='nsew')

        self.tree_scroll_y = Scrollbar(self.log_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree_scroll_y.grid(row=0, column=3, sticky='ns')
        self.tree.configure(yscrollcommand=self.tree_scroll_y.set)

        self.tree.heading("#0", text="#")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Time", text="Time")
        self.tree.heading("Value", text="Value 1")
        self.tree.heading("From Unit", text="From Unit")
        self.tree.heading("Converted Value", text="Value 2")
        self.tree.heading("To Unit", text="To Unit")
        self.tree.column("#0", width=40, anchor="center", stretch=False, minwidth=40)
        self.tree.column("Date", width=80, anchor="center", stretch=False, minwidth=100)
        self.tree.column("Time", width=60, anchor="center", stretch=False, minwidth=100)
        self.tree.column("Value", width=65, anchor="center", stretch=False, minwidth=100)
        self.tree.column("From Unit", width=90, anchor="center", stretch=False, minwidth=100)
        self.tree.column("Converted Value", width=65, anchor="center", stretch=False, minwidth=120)
        self.tree.column("To Unit", width=90, anchor="center", stretch=False, minwidth=100)

        self.tree.tag_configure('oddrow', background='#e0e0e0')
        self.tree.tag_configure('evenrow', background='white')

        self.display_logs()

        # Export logs section
        self.file_name_label = Label(self.log_frame, text="File Name:")
        self.file_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
        self.export_file_name = Entry(self.log_frame, font=("Arial", 10), width=20)
        self.export_file_name.grid(row=1, column=1, padx=(0, 5), pady=5, sticky=W)
        self.export_button = Button(self.log_frame, text="Export Logs", bg="#004C99", fg="#FFFFFF",
                                    font=("Arial", 10, "bold"), command=self.export_logs)
        self.export_button.grid(row=1, column=2, padx=(5, 0), pady=5, sticky=W)
        self.error_label = Label(self.log_frame, text="", font=("Arial", 10), fg="red", padx=5, pady=2)
        self.error_label.grid(row=2, column=0, columnspan=3)

        # Adjust column weights to center the export section
        self.log_frame.grid_columnconfigure(0, weight=1)
        self.log_frame.grid_columnconfigure(1, weight=0)
        self.log_frame.grid_columnconfigure(2, weight=1)
        self.log_frame.grid_columnconfigure(3, weight=1)

    def display_logs(self):
        index = 1
        for log in self.history:
            date_obj = datetime.strptime(log[0], '%Y-%m-%d %H:%M:%S')
            date_str = date_obj.strftime('%d.%m.%y')
            time_str = date_obj.strftime('%H:%M')
            tag = 'evenrow' if index % 2 == 0 else 'oddrow'
            self.tree.insert("", "end", text=str(index),
                             values=(date_str, time_str, log[1], log[2], log[3], log[4]), tags=(tag,))
            index += 1

    def export_logs(self):
        self.error_label.config(text="")
        if not self.history:
            self.error_label.config(text="No logs available to export.", fg="red")  # Set text color to red
            return

        filename = self.export_file_name.get().strip()
        if not filename:
            filename = datetime.now().strftime("conversion_logs_%Y%m%d_%H%M%S.txt")

        # Check for illegal characters in the filename
        if not re.match(r'^[\w\-. ]+$', filename):
            self.error_label.config(text="Filename contains illegal characters.", fg="red")  # Set text color to red
            return

        if not filename.endswith(".txt"):
            filename += ".txt"

        try:
            # Write the logs to the file
            with open(filename, "w") as file:
                file.write(
                    "{:<20} {:<10} {:<15} {:<15} {:<15}\n".format("Date", "Value", "From Unit", "Converted Value",
                                                                  "To Unit"))
                for log in self.history:
                    file.write("{:<20} {:<10} {:<15} {:<15} {:<15}\n".format(*log))
            self.error_label.config(text=f"Logs exported to {filename}", fg="green")
        except Exception as e:
            self.error_label.config(text=f"Error exporting logs: {e}", fg="red")

# Class to handle the main volume converter GUI


class VolumeConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Volume Converter")
        self.master.resizable(False, False)
        self.history = []

        self.volume_frame = Frame(master, padx=20, pady=20, bg="#E6E6E6")
        self.volume_heading = Label(self.volume_frame, text="Volume Converter", font=("Helvetica", 20, "bold"),
                                    bg="#E6E6E6", pady=10)
        self.volume_entry1 = Entry(self.volume_frame, font=("Arial", 12), width=14)
        self.equals_label = Label(self.volume_frame, text="=", font=("Arial", 12, "bold"), bg="#E6E6E6")
        self.volume_entry2 = Entry(self.volume_frame, font=("Arial", 12), width=14, state=DISABLED)
        self.unit_options = ["Liters", "Gallons", "Quarts", "Cubic Meters", "Cubic Feet"]
        self.selected_unit1 = StringVar()
        self.selected_unit1.set("Liters")
        self.selected_unit2 = StringVar()
        self.selected_unit2.set("Gallons")
        self.unit_dropdown1 = OptionMenu(self.volume_frame, self.selected_unit1, *self.unit_options)
        self.unit_dropdown1.config(font=("Arial", 10, "bold"), bg="#E6E6E6",
                                   width=14, indicatoron=False, compound='center')
        self.unit_dropdown2 = OptionMenu(self.volume_frame, self.selected_unit2, *self.unit_options)
        self.unit_dropdown2.config(font=("Arial", 10, "bold"), bg="#E6E6E6",
                                   width=14, indicatoron=False, compound='center')
        self.swap_button = Button(self.volume_frame, text="\u2194", bg="#004C99", fg="#FFFFFF",
                                  font=("Arial", 12, "bold"), width=3, height=1, command=self.swap_units)
        self.help_button = Button(self.volume_frame, text="?", bg="#004C99", fg="#FFFFFF",
                                  font=("Arial", 12, "bold"), width=3, height=1, command=display_help)
        self.view_logs_button = Button(self.volume_frame, text="View Logs", bg="#004C99", fg="#FFFFFF",
                                       font=("Arial", 12, "bold"), width=10, command=self.view_logs)
        self.save_button = Button(self.volume_frame, text="Save", bg="#004C99", fg="#FFFFFF",
                                  font=("Arial", 12, "bold"), width=10, command=self.save_conversion)
        self.save_label = Label(self.volume_frame, text="", font=("Arial", 10), fg="#004C99", width=40)
        self.bind_hover_effect(self.swap_button)
        self.bind_hover_effect(self.help_button)
        self.bind_hover_effect(self.view_logs_button)
        self.bind_hover_effect(self.save_button)

        # Bind events for real-time conversion
        self.volume_entry1.bind("<KeyRelease>", self.update_conversion)
        self.selected_unit1.trace("w", self.update_conversion)
        self.selected_unit2.trace("w", self.update_conversion)

        self.init_gui_elements()

    def init_gui_elements(self):
        self.volume_frame.grid()
        self.volume_heading.grid(row=0, column=0, columnspan=4)
        self.volume_entry1.grid(row=1, column=0, padx=5, pady=5)
        self.equals_label.grid(row=1, column=1, padx=5, pady=5)
        self.volume_entry2.grid(row=1, column=2, padx=5, pady=5)
        self.unit_dropdown1.grid(row=2, column=0, padx=5, pady=5)
        self.unit_dropdown2.grid(row=2, column=2, padx=5, pady=5)
        self.swap_button.grid(row=2, column=1, padx=5, pady=5)
        self.help_button.grid(row=3, column=1, padx=5, pady=5)
        self.view_logs_button.grid(row=3, column=0, padx=5, pady=5)
        self.save_button.grid(row=3, column=2, padx=5, pady=5)
        self.save_label.grid(row=4, column=0, columnspan=3, padx=5, pady=2)

    @staticmethod
    def bind_hover_effect(button):
        # Change button color on hover
        button.bind("<Enter>", lambda event, button1=button: button1.config(bg="#005CAE"))
        button.bind("<Leave>", lambda event, button1=button: button.config(bg="#004C99"))

    def swap_units(self):
        # Swap the selected units and update the conversion
        unit1 = self.selected_unit1.get()
        unit2 = self.selected_unit2.get()
        self.selected_unit1.set(unit2)
        self.selected_unit2.set(unit1)
        self.update_conversion()

    def view_logs(self):
        # Open a new window to view logs
        log_viewer_window = Toplevel(self.master)
        LogViewer(log_viewer_window, self.history)

    def update_conversion(self, *args):
        # Perform conversion and update the output field
        value = self.volume_entry1.get()
        unit_from = self.selected_unit1.get()
        unit_to = self.selected_unit2.get()
        valid, error_msg = check_input(value, unit_from, unit_to)
        if valid:
            converted_value = convert_volume(value, unit_from, unit_to)
            rounded_value = round_number(converted_value)
            self.volume_entry2.config(state=NORMAL)
            self.volume_entry2.delete(0, END)
            self.volume_entry2.insert(0, rounded_value)
            self.volume_entry2.config(state=DISABLED)
            self.save_label.config(text="", fg="green")
        else:
            self.volume_entry2.config(state=NORMAL)
            self.volume_entry2.delete(0, END)
            self.volume_entry2.insert(0, "Error")
            self.volume_entry2.config(state=DISABLED)
            self.save_label.config(text=error_msg, fg="red")

    def save_conversion(self):
        # Save the current conversion to the history
        value = self.volume_entry1.get()
        unit_from = self.selected_unit1.get()
        unit_to = self.selected_unit2.get()
        valid, error_msg = check_input(value, unit_from, unit_to)
        if valid:
            converted_value = convert_volume(value, unit_from, unit_to)
            rounded_value = round_number(converted_value)
            self.volume_entry2.config(state=NORMAL)
            self.volume_entry2.delete(0, END)
            self.volume_entry2.insert(0, rounded_value)
            self.volume_entry2.config(state=DISABLED)
            self.save_label.config(text="Conversion saved", fg="green")
            log_entry = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), value, unit_from, rounded_value, unit_to)
            self.history.append(log_entry)
        else:
            self.save_label.config(text=error_msg, fg="red")


# Main function to initialize and run the application
def main():
    root = Tk()
    app = VolumeConverterGUI(root)
    app.init_gui_elements()
    root.mainloop()


if __name__ == "__main__":
    main()
