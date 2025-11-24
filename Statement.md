 # Project Statement: Simple To-Do List Application
---
# Problem Statement

Many people require a quick and easy way to **track and manage their daily or short-term tasks** without the complexity of feature-rich applications. The primary problem is the need for a **minimalist, command-line interface (CLI) based tool** to handle the essential functions of a task manager: adding, viewing, and removing tasks.

---

# Scope of the Project

The scope of this project is to create a **basic, console-based To-Do List application** using Python.

* **In-Scope:**
    * Allow users to **add** new tasks to a list.
    * Allow users to **view** all current tasks with corresponding index numbers.
    * Allow users to **remove** tasks based on their index number.
    * Provide a simple menu for navigation.
    * The task list is **ephemeral** (not saved to a file and lost upon exit).
* **Out-of-Scope:**
    * Data persistence (saving tasks to a file).
    * Editing or updating existing tasks.
    * Task prioritization, due dates, or status tracking (e.g., "completed").
    * Graphical User Interface (GUI).

---

# Target Users

The application is designed for users who:

* **Need a simple, fast tool** for managing a small number of tasks.
* Are comfortable working within a **command-line environment**.
* Are beginners or students looking for a **minimalist task-tracking solution**.

## High-Level Features

The application provides four main functions accessible via a simple menu:

1.  **Add a Task:** Allows the user to input a new task, which is then appended to the list.
2.  **View Tasks:** Displays the complete list of tasks, numbered sequentially for easy reference.
3.  **Remove a Task:** Prompts the user to enter the number of the task they wish to delete from the list.
4.  **Exit:** Terminates the application.
