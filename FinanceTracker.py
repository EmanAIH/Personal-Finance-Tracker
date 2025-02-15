# Create a new directory for the project

import tkinter as tk
from tkinter import messagebox
import json

#Create the main class

class FinanceTrackerApp():
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.root.geometry("600x400")
        self.records = self.load_data() # Load previously saved data
        self.create_widgets() # Create the GUI components


#define the create the widgets function
def create_widgets(self):
    # Create a label for the title
    self.title_label = tk.Label(self.root, text= "Personal Finance Tracker", font=("Helvetica", 16))
    self.title_label.pack(pady=20)

    # Create a label for the amount
    self.amount_label = tk.Label(self.root, text= "Amount ($):")
    self.amount_label.pack(pady=5)

    # Create an entry widget for the amount
    self.amount_entry = tk.Entry(self.root)
    self.amount_entry.pack(pady=5)

    # Create a label for the category
    self.category_label = tk.Label(self.root, text="Category:")
    self.category_label.pack(pady=5)

    #create an entry for the category
    self.category_entry = tk.Entry(self.root)
    self.category_entry.pack(pady=5)

    # Create a label for the date
    self.description_Label = tk.Label(self.root, text="Description:")
    self.description_label.pack(pady=5)

    # Create an entry for the description
    self.description_entry = tk.Entry(self.root)
    self.description_entry.pack(pady=5)

    # Create a button to add a new entry
    self.add_button = tk.Button(self.root, text = "Add Entry", command=self.add_entry)
    self.add_button.pack(pady=10)

    # Create a button to view  entries
    self.view_button = tk.Button(self.root, text="View All Entries", command=self.view_entries)
    self.view_button.pack(pady=5)

    # create a button to exit
    self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
    self.exit_button.pack(pady=5)

#define the create the add entries function
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
    self.records.append(entry) # add new entry to list
    self.save_data() # save the updated data
    messagebox.showinfo("Good! your entry was added successfully")
   
   
    else:
    messagebox.showwarning("Error", "Please fill in ALL fields")       