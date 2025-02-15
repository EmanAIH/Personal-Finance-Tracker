import tkinter as tk
from tkinter import messagebox
import json

# Create the main class
class FinanceTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("600x400")
        self.records = self.load_data()  # Load previously saved data
        self.create_widgets()  # Create the GUI components

    # Define the create_widgets function
    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Personal Finance Tracker", font=("Helvetica", 16))
        self.title_label.pack(pady=20)

        self.amount_label = tk.Label(self.root, text="Amount ($):")
        self.amount_label.pack(pady=5)
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        self.category_label = tk.Label(self.root, text="Category:")
        self.category_label.pack(pady=5)
        self.category_entry = tk.Entry(self.root)
        self.category_entry.pack(pady=5)

        self.description_label = tk.Label(self.root, text="Description:")
        self.description_label.pack(pady=5)
        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Entry", command=self.add_entry)
        self.add_button.pack(pady=10)

        self.view_button = tk.Button(self.root, text="View All Entries", command=self.view_entries)
        self.view_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    # Define the add_entry function
    def add_entry(self):
        amount = self.amount_entry.get()
        category = self.category_entry.get()
        description = self.description_entry.get()

        if amount and category and description:
            entry = {
                "amount": amount,
                "category": category,
                "description": description
            }
            self.records.append(entry)
            self.save_data()
            messagebox.showinfo("Success", "Your entry was added successfully")
        else:
            messagebox.showwarning("Error", "Please fill in ALL fields")

    # Define the view_entries function
    def view_entries(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Entries")
        view_window.geometry("600x400")

        for idx, record in enumerate(self.records):
            text = f"Amount: {record['amount']} | Category: {record['category']} | Description: {record['description']}"
            tk.Label(view_window, text=text).pack(pady=5)

    # Define the load_data function
    def load_data(self):
        try:
            with open("finance_data.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Return empty list if file doesn't exist or is corrupted

    # Define the save_data function
    def save_data(self):
        with open("finance_data.json", "w") as f:
            json.dump(self.records, f)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTrackerApp(root)
    root.mainloop()
