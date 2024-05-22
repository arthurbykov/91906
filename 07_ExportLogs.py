from tkinter import *
from datetime import datetime
import re


class LogExporter:
    def __init__(self, master):
        self.master = master
        self.master.title("Export Logs")
        self.master.resizable(False, False)

        self.history = [
            ("2024-05-17 12:00:00", 1.0, "Liters", 0.2642, "Gallons"),
            ("2024-05-17 12:05:00", 2.0, "Cubic Meters", 70.6293, "Cubic Feet"),
            ("2024-05-17 12:10:00", 3.5, "Quarts", 3.3069, "Liters"),
            ("2024-05-17 12:15:00", 4.0, "Gallons", 15.1416, "Liters"),
            ("2024-05-17 12:20:00", 5.0, "Liters", 1.32086, "Gallons")
        ]

        self.export_frame = Frame(master, padx=10, pady=10)
        self.export_frame.grid()

        self.export_heading = Label(self.export_frame, text="Export Conversion Logs", font=("Arial", 16, "bold"))
        self.export_heading.grid(row=0, column=0, columnspan=3, pady=10)

        self.file_name_label = Label(self.export_frame, text="File Name:")
        self.file_name_label.grid(row=1, column=0, padx=5, pady=5)

        self.export_file_name = Entry(self.export_frame, font=("Arial", 10), width=20)
        self.export_file_name.grid(row=1, column=1, padx=5, pady=5)

        self.export_button = Button(self.export_frame, text="Export Logs", bg="#004C99", fg="#FFFFFF",
                                    font=("Arial", 10, "bold"), command=self.export_logs)
        self.export_button.grid(row=1, column=2, padx=5, pady=5)

        self.error_label = Label(self.export_frame, text="", font=("Arial", 10), fg="red", padx=5, pady=2)
        self.error_label.grid(row=2, column=0, columnspan=3)

    def export_logs(self):
        self.error_label.config(text="")

        if not self.history:
            self.error_label.config(text="No logs available to export.")
            return

        filename = self.export_file_name.get().strip()
        if not filename:
            filename = datetime.now().strftime(
                "conversion_logs_%Y%m%d_%H%M%S.txt")  # Use current date and time as default

        if not re.match(r'^[\w\-. ]+$', filename):
            self.error_label.config(text="Filename contains illegal characters.")
            return

        if not filename.endswith(".txt"):
            filename += ".txt"

        try:
            with open(filename, "w") as file:
                file.write(
                    "{:<20} {:<10} {:<15} {:<15} {:<15}\n".format("Date", "Value", "From Unit", "Converted Value",
                                                                  "To Unit"))
                for log in self.history:
                    file.write("{:<20} {:<10} {:<15} {:<15} {:<15}\n".format(*log))

            self.error_label.config(text=f"Logs exported to {filename}", fg="green")
        except Exception as e:
            self.error_label.config(text=f"Error exporting logs: {e}", fg="red")


def main():
    root = Tk()
    app = LogExporter(root)
    root.mainloop()


if __name__ == "__main__":
    main()
