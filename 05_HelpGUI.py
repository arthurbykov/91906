from tkinter import messagebox


def display_help():
    help_text = "This program allows you to convert volumes between different units. \n\n" \
                "1. Enter the volume you want to convert in the first field.\n" \
                "2. Select the unit of the volume you entered from the dropdown menu next to it.\n" \
                "3. Select the unit you want to convert to from the dropdown menu on the other side.\n" \
                "4. The converted volume will be displayed in the second field.\n" \
                "5. Click 'Save' to save the conversion to history.\n" \
                "6. Click 'View Logs' to see all the previous conversions.\n" \
                "7. You can export the conversion logs to a file by clicking 'Export Logs'."
    messagebox.showinfo("Help", help_text)


# Testing the help display
display_help()
