# Task Scheduler

This Python script, `task_scheduler.py`, is a simple command-line task management application that allows users to add, view, and delete tasks with due dates. The application stores task data in a JSON file.

## How to Use

1. **Installation**:

   - Make sure you have Python installed on your system.

2. **Run the Application**:

   - Open a terminal or command prompt.
   - Navigate to the directory where `task_scheduler.py` is located.

   ```
   $ cd /path/to/directory
   ```

   - Run the script:

   ```
   $ python task_scheduler.py
   ```

3. **Menu Options**:

   - The application provides the following menu options:

     - **Add Task**: Allows you to add a new task with a name and due date (in YYYY-MM-DD format).

     - **View Tasks**: Displays a list of tasks with their names and due dates.

     - **Delete Task**: Lets you delete a task by specifying its number in the list.

     - **Quit**: Exits the application.

4. **Data Storage**:

   - The tasks are stored in a JSON file named `tasks.json` in the same directory as the script.

5. **Error Handling**:

   - The application handles various errors, such as invalid date format or task numbers.

## Example Usage

1. **Add Task**:

   - Choose option 1.
   - Enter a task name.
   - Enter the due date in YYYY-MM-DD format.

2. **View Tasks**:

   - Choose option 2 to see a list of added tasks with their due dates.

3. **Delete Task**:

   - Choose option 3.
   - Enter the number of the task you want to delete.

4. **Quit**:

   - Choose option 4 to exit the application.

## Data Persistence

The application loads tasks from the `tasks.json` file when it starts and saves tasks back to the file after any additions or deletions. This ensures that your tasks are retained even when the application is closed and reopened.

## Error Handling

The application checks for invalid date formats and incorrect task numbers, providing appropriate error messages to guide the user.

## Important Notes

- Please ensure that you have Python installed on your system.
- Make sure to provide dates in the specified format (YYYY-MM-DD).
- Be cautious when deleting tasks, as this action is irreversible.

## Author

This Python Task Scheduler was created by Sagnik Sahoo.

Feel free to customize and extend this application to suit your needs. Enjoy managing your tasks!
