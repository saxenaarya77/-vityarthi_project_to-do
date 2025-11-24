# VITYARTHI_PROJECT_TO-DO
 vityarthi: A Simple To-Do List Application
# Overview of the Project
This project, **vityarthi**, is a **command-line interface (CLI) To-Do List application** built using Python. It allows users to manage their daily tasks by providing a simple, interactive menu to add, view, and remove tasks from a list. The data is stored in memory for the duration of the program's execution.
#Features
* **Add Task:** Easily input and save a new task to the list.
* **View Tasks:** Display all current tasks in a numbered list.
* **Remove Task:** Select a task by its number to remove it from the list.
* **Simple Menu:** An intuitive menu system for easy navigation and interaction.
## Technologies/Tools Used
* **Language:** **Python 3** (The project is a single Python script).
## ⬇️ Steps to Install & Run the Project

Since this is a simple Python script, no special installation is required beyond having a working Python environment.

### Prerequisites

You must have **Python 3** installed on your system.

### Running the Application

1.  **Save the Code:** Save the provided code into a file named, for example, `todo_list.py`.
2.  **Open Terminal/Command Prompt:** Navigate to the directory where you saved the file.
3.  **Execute the Script:** Run the following command:

    ```bash
    python todo_list.py
    ```
4.  The application menu will appear, and you can start managing your tasks.

---

## Instructions for Testing
Follow these steps to test the core functionalities of the To-Do List application:

1.  **Start the Program:** Run the script (`python todo_list.py`).

2.  **Test 'View tasks' (Initial State):**
    * Enter **2** when the menu appears.
    * **Expected Result:** It should print "No task added yet."

3.  **Test 'Add a task':**
    * Enter **1**.
    * When prompted, enter a task (e.g., "Grocery Shopping").
    * **Expected Result:** It should print "Task added !"
    * Repeat this step a few times to add multiple tasks.

4.  **Test 'View tasks' (With Tasks):**
    * Enter **2**.
    * **Expected Result:** It should display the list of all tasks you added, each numbered starting from 1.

5.  **Test 'Remove a task':**
    * Enter **3**.
    * The task list will be displayed.
    * Enter the number corresponding to a task you wish to remove (e.g., **1** to remove the first task).
    * **Expected Result:** It should print "Removed: [task name]" (Note: Due to a small error in the provided code snippet, the removal message will display the task number minus one, not the task name itself).

6.  **Test 'Exit':**
    * Enter **4**.
    * **Expected Result:** It should print "Exiting..... goodbye!" and the program should terminate.

7.  **Test Invalid Input:**
    * Enter any number or character not between 1 and 4 (e.g., **5** or **a**).
    * **Expected Result:** It should print "Invalid choice .! Please enter 1–4."
