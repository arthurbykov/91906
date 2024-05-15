from tkinter import *


class VolumeConverter:
    def __init__(self):
        self.previous_left_text = ""
        self.previous_right_text = ""
        self.previous_left_unit = ""
        self.previous_right_unit = ""

        # Set up the GUI frame
        self.volume_frame = Frame(padx=10, pady=10)
        self.volume_frame.grid()

        # Title
        self.volume_heading = Label(self.volume_frame,
                                    text="Volume Converter",
                                    font=("Arial", "16", "bold"))
        self.volume_heading.grid(row=0, column=0, columnspan=3)

        # Volume entry fields
        self.volume_entry1 = Entry(self.volume_frame,
                                   font=("Arial", "14"),
                                   width=10)
        self.volume_entry1.grid(row=1, column=0, padx=5, pady=5)
        self.volume_entry1.bind('<KeyRelease>', self.mirror_text_left)

        self.equals_label = Label(self.volume_frame,
                                  text="=")
        self.equals_label.grid(row=1, column=1, padx=5, pady=5)

        self.volume_entry2 = Entry(self.volume_frame,
                                   font=("Arial", "14"),
                                   width=10)
        self.volume_entry2.grid(row=1, column=2, padx=5, pady=5)
        self.volume_entry2.bind('<KeyRelease>', self.mirror_text_right)

        # Unit selection dropdown menu
        self.unit_options = ['Liters', 'Gallons', 'Quarts', 'Cubic Meters', 'Cubic Feet']
        self.selected_unit1 = StringVar()
        self.selected_unit1.set(self.unit_options[0])  # default value
        self.selected_unit2 = StringVar()
        self.selected_unit2.set(self.unit_options[0])  # default value

        self.unit_dropdown1 = OptionMenu(self.volume_frame, self.selected_unit1, *self.unit_options)
        self.unit_dropdown1.config(font=("Arial", "10"), bg="#E6E6E6", width=10)
        self.unit_dropdown1.grid(row=2, column=0, padx=5, pady=5)

        self.unit_dropdown2 = OptionMenu(self.volume_frame, self.selected_unit2, *self.unit_options)
        self.unit_dropdown2.config(font=("Arial", "10"), bg="#E6E6E6", width=10)
        self.unit_dropdown2.grid(row=2, column=2, padx=5, pady=5)

        # Help and history/export buttons
        self.help_button = Button(self.volume_frame,
                                  text="Help / Info",
                                  bg="#CC6600",
                                  fg="#FFFFFF",
                                  font=("Arial", "12", "bold"),
                                  width=12,
                                  command=self.to_help)
        self.help_button.grid(row=3, column=0, padx=5, pady=5)

        self.history_button = Button(self.volume_frame,
                                     text="History / Export",
                                     bg="#004C99",
                                     fg="#FFFFFF",
                                     font=("Arial", "12", "bold"),
                                     width=12,
                                     state=DISABLED,
                                     command=self.to_history)
        self.history_button.grid(row=3, column=2, padx=5, pady=5)

        # Initialize selected units
        self.select_units("Liters")

    # Opens Help / Info dialogue box
    @staticmethod
    def to_help():
        DisplayHelp()

    # Opens History / Export dialogue box
    @staticmethod
    def to_history():
        HistoryExport()

    # Function to mirror text from one entry field to another
    def mirror_text_left(self, event=None):
        current_left_text = self.volume_entry1.get()
        if current_left_text != self.previous_left_text:
            self.volume_entry2.delete(0, END)
            self.volume_entry2.insert(0, current_left_text)
            self.previous_left_text = current_left_text

    def mirror_text_right(self, event=None):
        current_right_text = self.volume_entry2.get()
        if current_right_text != self.previous_right_text:
            self.volume_entry1.delete(0, END)
            self.volume_entry1.insert(0, current_right_text)
            self.previous_right_text = current_right_text

    # Function to select units for each field
    # Function to select units for each field
    def select_units(self, units):
        # Update selected units
        self.previous_left_unit = self.selected_unit1.get()
        self.previous_right_unit = self.selected_unit2.get()

        # Update dropdown menus to prevent selecting the same unit in both
        if self.previous_left_unit == units:
            self.selected_unit2.set(self.previous_right_unit)
        elif self.previous_right_unit == units:
            self.selected_unit1.set(self.previous_left_unit)

        # Update dropdown menus to reflect changes
        self.unit_dropdown1['menu'].delete(0, 'end')
        self.unit_dropdown2['menu'].delete(0, 'end')
        for unit in self.unit_options:
            self.unit_dropdown1['menu'].add_command(label=unit, command=lambda u=unit: self.selected_unit1.set(u))
            self.unit_dropdown2['menu'].add_command(label=unit, command=lambda u=unit: self.selected_unit2.set(u))


class DisplayHelp:
    def __init__(self):
        background = "#ffe6cc"
        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300, height=200, bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background,
                                        text="Help / Info", font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the volume " \
                    "you wish to convert in one field, and it will " \
                    "be mirrored in the other field. Then, choose " \
                    "the unit you want to convert to from the dropdown " \
                    "menus above each field. \n\n" \
                    "For example, enter a volume in liters and select " \
                    "'Gallons' from the dropdown menu to convert it."
        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wraplength=350, justify="left")
        self.help_text_label.grid(row=1, padx=10, pady=10)

        self.dismiss_button = Button(self.help_frame, font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600", fg="#FFFFFF",
                                     command=self.close_help)
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialogue
    def close_help(self):
        self.help_box.destroy()

class HistoryExport:
    def __init__(self):
        background = "#ffe6cc"
        self.history_box = Toplevel()

        self.history_frame = Frame(self.history_box, width=300, height=200, bg=background)
        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame,
                                           text="History / Export",
                                           font=("Arial", "16", "bold"))
        self.history_heading_label.grid(row=0)

        hist_text = "No history available yet."
        self.text_instructions_label = Label(self.history_frame,
                                             text=hist_text,
                                             wraplength=300,
                                             justify="left",
                                             padx=10, pady=10)
        self.text_instructions_label.grid(row=1)

        self.dismiss_button = Button(self.history_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=self.close_history)
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes history dialogue
    def close_history(self):
        self.history_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.resizable(False, False)
    root.title("Volume Converter")
    VolumeConverter()
    root.mainloop()
