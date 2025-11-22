# -vityarthi_project_to-do
Python GUI To-Do List

A simple, desktop-based To-Do List application built using Python and Tkinter. This project demonstrates how to build a Graphical User Interface (GUI) that supports creating, reading, updating, and deleting tasks, with data persistence.

📋 Features

Add Tasks: Type a task and click "Add" to append it to your list.

Persistent Storage: Tasks are automatically saved to a local file (tasks.txt). Your list is remembered even after you close and reopen the app.

Delete Tasks: Select specific tasks and remove them with the "Delete Task" button.

Clear All: A "Clear All" button to wipe the list, featuring a confirmation popup to prevent accidental deletions.

Scrollable View: Includes a scrollbar to manage long lists of tasks comfortably.

🛠️ Prerequisites

Python 3.x installed on your system.

Tkinter: This usually comes pre-installed with standard Python distributions.

🚀 How to Run

Save the file: Copy the Python code into a file named todo_app.py.

Open your terminal or command prompt.

Navigate to the directory where you saved the file.

Run the command:

python todo_app.py


📂 File Structure

todo_app.py: The main script containing the source code and logic.

tasks.txt: A text file generated automatically by the program to store your tasks. Do not delete this if you want to keep your task history.

💡 Code Overview

The project is structured using a class-based approach (TodoApp):

UI Setup (__init__): Configures the 400x500 window, creates frames, labels, entry fields, and buttons using the Grid/Pack geometry managers.

Data Handling:

save_tasks(): Iterates through the Listbox items and writes them to tasks.txt.

load_tasks(): Reads tasks.txt on startup to populate the list.

Event Handling: Functions like add_task and delete_task handle user interactions and update the UI dynamically.

📝 License

This project is open-source and free to use for educational purposes.