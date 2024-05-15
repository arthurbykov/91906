from tkinter import *


class VolumeConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Volume Converter")
        self.master.resizable(False, False)
        self.unit_options = ['Liters', 'Gallons', 'Quarts', 'Cubic Meters', 'Cubic Feet']
        self.volume_frame = Frame(master, padx=10, pady=10)
        self.volume_heading = Label(self.volume_frame, text="Volume Converter", font=("Arial", 16, "bold"))
        self.volume_entry1 = Entry(self.volume_frame, font=("Arial", 14), width=10)
        self.equals_label = Label(self.volume_frame, text="=", font=("Arial", 14))
        self.volume_entry2 = Entry(self.volume_frame, font=("Arial", 14), width=10, state=DISABLED)
        self.selected_unit1 = StringVar()
        self.selected_unit1.set(self.unit_options[0])
        self.selected_unit2 = StringVar()
        self.selected_unit2.set(self.unit_options[0])
        self.unit_dropdown1 = OptionMenu(self.volume_frame, self.selected_unit1, *self.unit_options)
        self.unit_dropdown1.config(font=("Arial", 10, "bold"), bg="#E6E6E6", width=14,
                                   indicatoron=False, compound='center')
        self.unit_dropdown2 = OptionMenu(self.volume_frame, self.selected_unit2, *self.unit_options)
        self.unit_dropdown2.config(font=("Arial", 10, "bold"), bg="#E6E6E6", width=14,
                                   indicatoron=False, compound='center')
        self.swap_button = Button(
            self.volume_frame, text="\u2194", bg="#004C99", fg="#FFFFFF", font=("Arial", 12, "bold"), width=3, height=1)
        self.help_button = Button(
            self.volume_frame, text="?", bg="#004C99", fg="#FFFFFF", font=("Arial", 12, "bold"), width=3, height=1)
        self.view_logs_button = Button(
            self.volume_frame, text="View Logs", bg="#004C99", fg="#FFFFFF", font=("Arial", 12, "bold"), width=10)
        self.save_button = Button(
            self.volume_frame, text="Save", bg="#004C99", fg="#FFFFFF", font=("Arial", 12, "bold"), width=10)
        self.save_label = Label(
            self.volume_frame, text="", font=("Arial", 10), fg="#004C99", width=40)

        # Bind events for button hover effect
        self.bind_hover_effect(self.swap_button)
        self.bind_hover_effect(self.help_button)
        self.bind_hover_effect(self.view_logs_button)
        self.bind_hover_effect(self.save_button)

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
        button.bind("<Enter>", lambda event, button1=button: button1.config(bg="#005CAE"))
        button.bind("<Leave>", lambda event, button1=button: button.config(bg="#004C99"))


def main():
    root = Tk()
    app = VolumeConverterGUI(root)
    app.init_gui_elements()
    root.mainloop()


if __name__ == "__main__":
    main()
