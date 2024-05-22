from tkinter import *
from tkinter import ttk
from datetime import datetime


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

        # Create Treeview widget
        self.tree = ttk.Treeview(self.log_frame,
                                 columns=("Date", "Time", "Value", "From Unit", "Converted Value", "To Unit"))
        self.tree.grid(row=0, column=0, columnspan=2, sticky='nsew')

        # Configure the scrollbars
        self.tree_scroll_y = Scrollbar(self.log_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree_scroll_y.grid(row=0, column=2, sticky='ns')

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

        # Define tags for alternating row colors
        self.tree.tag_configure('oddrow', background='#e0e0e0')
        self.tree.tag_configure('evenrow', background='white')

        self.display_logs()

    def display_logs(self):
        index = 1
        for log in self.history:
            date_obj = datetime.strptime(log[0], '%Y-%m-%d %H:%M:%S')
            date_str = date_obj.strftime('%d.%m.%y')
            time_str = date_obj.strftime('%H:%M')
            tag = 'evenrow' if index % 2 == 0 else 'oddrow'
            self.tree.insert("", "end", text=str(index), values=(date_str, time_str, log[1], log[2], log[3], log[4]),
                             tags=(tag,))
            index += 1


def main():
    root = Tk()

    # Sample history data for testing
    sample_history = [
        ("2024-05-17 12:00:00", 1.0, "Liters", 0.2642, "Gallons"),
        ("2024-05-17 12:05:00", 2.0, "Cubic Meters", 70.6293, "Cubic Feet"),
        ("2024-05-17 12:10:00", 3.5, "Quarts", 3.3069, "Liters"),
        ("2024-05-17 12:15:00", 4.0, "Gallons", 15.1416, "Liters"),
        ("2024-05-17 12:20:00", 5.0, "Liters", 1.32086, "Gallons"),
        ("2024-05-17 12:25:00", 6.0, "Cubic Feet", 0.1699, "Cubic Meters"),
        ("2024-05-17 12:30:00", 7.0, "Pints", 3.30693, "Liters"),
        ("2024-05-17 12:35:00", 8.0, "Milliliters", 0.00845, "Liters"),
        ("2024-05-17 12:40:00", 9.0, "Liters", 0.237, "Quarts"),
        ("2024-05-17 12:45:00", 10.0, "Gallons", 37.8541, "Liters"),
        ("2024-05-17 12:50:00", 11.0, "Cubic Meters", 388.35, "Gallons"),
        ("2024-05-17 12:55:00", 12.0, "Quarts", 11.3562, "Liters"),
        ("2024-05-17 13:00:00", 13.0, "Pints", 6.5569, "Liters"),
        ("2024-05-17 13:05:00", 14.0, "Liters", 0.369, "Pints"),
        ("2024-05-17 13:10:00", 15.0, "Gallons", 56.78, "Liters"),
        ("2024-05-17 13:15:00", 16.0, "Cubic Feet", 0.453, "Cubic Meters"),
        ("2024-05-17 13:20:00", 17.0, "Pints", 8.3453, "Liters"),
        ("2024-05-17 13:25:00", 18.0, "Milliliters", 0.0189, "Liters"),
        ("2024-05-17 13:30:00", 19.0, "Liters", 0.419, "Quarts"),
        ("2024-05-17 13:35:00", 20.0, "Gallons", 75.7082, "Liters")
    ]

    app = LogViewer(root, sample_history)
    root.mainloop()


if __name__ == "__main__":
    main()
