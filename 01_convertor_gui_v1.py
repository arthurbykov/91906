from tkinter import *
from functools import partial  # To prevent unwanted windows

class VolumeConverter:

    def __init__(self):

        # Set up the GUI frame
        self.volume_frame = Frame(padx=10, pady=10)
        self.volume_frame.grid()

        self.volume_heading = Label(self.volume_frame,
                                    text="Volume Converter",
                                    font=("Arial", "16", "bold")
                                    )
        self.volume_heading.grid(row=0, columnspan=3)

        # Volume entry fields
        self.volume_entry1 = Entry(self.volume_frame,
                                   font=("Arial", "14"),
                                   width=10)
        self.volume_entry1.grid(row=1, column=0, padx=5, pady=5)
        self.volume_entry1.bind('<KeyRelease>', self.mirror_text)

        self.equals_label = Label(self.volume_frame,
                                  text="=")
        self.equals_label.grid(row=1, column=1, padx=5, pady=5)

        self.volume_entry2 = Entry(self.volume_frame,
                                   font=("Arial", "14"),
                                   width=10)
        self.volume_entry2.grid(row=1, column=2, padx=5, pady=5)
        self.volume_entry2.bind('<KeyRelease>', self.mirror_text)

        # Volume conversion buttons
        self.button_frame = Frame(self.volume_frame)
        self.button_frame.grid(row=2, columnspan=3)

        self.to_liters_button = Button(self.button_frame,
                                       text="To Liters",
                                       bg="#990099",
                                       fg="#FFFFFF",
                                       font=("Arial", "12", "bold"),
                                       width=12)
        self.to_liters_button.grid(row=0, column=0, padx=5, pady=5)

        self.to_gallons_button = Button(self.button_frame,
                                         text="To Gallons",
                                         bg="#009900",
                                         fg="#FFFFFF",
                                         font=("Arial", "12", "bold"),
                                         width=12)
        self.to_gallons_button.grid(row=0, column=1, padx=5, pady=5)

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

    # Opens Help / Info dialogue box
    def to_help(self):
        DisplayHelp()

    # Opens History / Export dialogue box
    def to_history(self):
        HistoryExport()

    # Function to mirror text from one entry field to another
    def mirror_text(self, event=None):
        text = self.volume_entry1.get()
        self.volume_entry2.delete(0, END)
        self.volume_entry2.insert(0, text)

class DisplayHelp:

    def __init__(self):

        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.help_box = Toplevel()

        self.help_frame = Frame(self.help_box, width=300, height=200,
                                bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background,
                                        text="Help / Info",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use the program, simply enter the volume " \
                    "you wish to convert in one field, and it will " \
                    "be mirrored in the other field. Then, choose " \
                    "the unit you want to convert to and press the " \
                    "corresponding button. \n\n" \
                    "For example, enter a volume in liters and press " \
                    "'To Gallons' to convert it to gallons."
        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10, pady=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="Dismiss", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=self.close_help)
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    # closes help dialogue
    def close_help(self):
        self.help_box.destroy()

class HistoryExport:

    def __init__(self):

        # setup dialogue box and background colour
        background = "#ffe6cc"
        self.history_box = Toplevel()

        self.history_frame = Frame(self.history_box, width=300,
                                   height=200, bg=background)
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
    root.title("Volume Converter")
    VolumeConverter()
    root.mainloop()
