import tkinter as tk
from tkinter import messagebox
import os

class TodoApp:
    def __init__(self, root):
        """
        Initialize the main application window and setup the UI.
        
        Args:
            root (tk.Tk): The main window object provided by tkinter.
        """
        self.root = root
        self.root.title("My Python Project - To Do List")
        self.root.geometry("400x500") # Set the initial window size
        
        # Define a file to save tasks so they aren't lost when closing the app
        self.filename = "tasks.txt"
        
        # --- UI SETUP ---
        
        # 1. Title Label
        # We use a Label widget to show the header text.
        self.label = tk.Label(self.root, text="Daily Tasks", font=("Helvetica", 24, "bold"))
        self.label.pack(pady=10) # pack() places the widget in the window. pady adds vertical padding.

        # 2. Input Area Frame
        # A Frame is a container to organize other widgets.
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        # Entry widget: This is the text box where the user types the task.
        self.task_entry = tk.Entry(self.input_frame, width=25, font=("Helvetica", 14))
        self.task_entry.pack(side=tk.LEFT, padx=10)

        # Button widget: Clicking this triggers the add_task function.
        self.add_button = tk.Button(self.input_frame, text="Add", font=("Helvetica", 12), 
                                    bg="#4CAF50", fg="white", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # 3. Listbox Area
        # Listbox widget: This displays the list of tasks.
        self.tasks_listbox = tk.Listbox(self.root, width=40, height=10, font=("Helvetica", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=10)
        
        # Scrollbar: Useful if the list of tasks gets very long.
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Link the scrollbar to the listbox
        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tasks_listbox.yview)

        # 4. Action Buttons Frame
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=20)

        # Delete Button
        self.delete_button = tk.Button(self.button_frame, text="Delete Task", font=("Helvetica", 12), 
                                       bg="#f44336", fg="white", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        # Clear All Button
        self.clear_button = tk.Button(self.button_frame, text="Clear All", font=("Helvetica", 12), 
                                      bg="#FF9800", fg="white", command=self.clear_all_tasks)
        self.clear_button.pack(side=tk.LEFT, padx=10)

        # --- DATA LOADING ---
        # Load existing tasks from the text file when the app starts.
        self.load_tasks()

    def add_task(self):
        """
        Reads the text from the entry box and adds it to the listbox.
        Also triggers a save to the file.
        """
        task = self.task_entry.get() # Get text from input box
        if task != "":
            self.tasks_listbox.insert(tk.END, task) # Add to the end of the listbox
            self.task_entry.delete(0, tk.END) # Clear the input box
            self.save_tasks() # Save changes to file
        else:
            # Show a warning pop-up if the user tries to add an empty task
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        """
        Deletes the currently selected task from the listbox.
        """
        try:
            # curselection() returns the index of the selected item
            selected_task_index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(selected_task_index)
            self.save_tasks() # Update file after deletion
        except IndexError:
            # This happens if the user clicks 'Delete' without selecting anything
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def clear_all_tasks(self):
        """
        Removes all items from the listbox.
        """
        if messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?"):
            self.tasks_listbox.delete(0, tk.END)
            self.save_tasks()

    def save_tasks(self):
        """
        Iterates through the listbox items and writes them to a text file.
        This ensures data persistence (tasks stay after closing the app).
        """
        tasks = self.tasks_listbox.get(0, tk.END) # Get all items from listbox
        with open(self.filename, "w") as f:
            for task in tasks:
                f.write(task + "\n")

    def load_tasks(self):
        """
        Reads tasks from the text file and populates the listbox on startup.
        """
        # Check if the file exists before trying to open it
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                for line in f:
                    # strip() removes the newline character at the end
                    self.tasks_listbox.insert(tk.END, line.strip())

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    
    # Instantiate our application class
    app = TodoApp(root)
    
    # Start the GUI event loop (keeps the window open)
    root.mainloop()