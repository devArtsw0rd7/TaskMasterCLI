import datetime
from utils import parse_task_entry

class TaskManager:
    def __init__(self):
        self.tasks = []

    def run(self):
        first_prompt = True
        while True:
            if first_prompt:
                user_input = input("\n\n\n\n\n\nWELCOME TO TASK MASTER!!!\n\nEnter tasks to be prioritized:\n")
                first_prompt = False
            else:
                user_input = input("\nENTER NEXT TASK or type 'p' to begin prioritizing selections. Type 'h' for help or 'q' to quit:\n")

            user_input = user_input.strip().lower()  # Convert input to lowercase for case insensitivity

            if user_input == 'q':
                print("\nExiting TaskMasterCLI.")
                return None

            if user_input == 'p':
                print("\nBegin prioritization selections")
                self.prioritize_tasks()
                return 'Begin prioritization selections'

            if user_input in ['h', 'help']:
                self.display_help()
                continue

            task = parse_task_entry(user_input)
            if task:
                self.tasks.append(task)
                print(f"Task added: {task['description']}")
            else:
                print("Invalid task entry. Please try again.")

    def prioritize_tasks(self):
        self.sort_tasks()
        self.print_prioritized_tasks()

    def sort_tasks(self):
        self.tasks.sort(key=self.compare_tasks)
        
    def compare_tasks(self, task):
        return (
            -self.compare_priority(task['priority']),  # Use negative to reverse the order
            self.compare_due_date(task['due_date']),
        )
    
    def compare_priority(self, priority):
        if priority == 'h':
            return 3
        elif priority == 'm':
            return 2
        elif priority == 'l':
            return 1
        else:
            return 0  # Default case, though should not happen with valid inputs
    
    def compare_due_date(self, due_date):
        if due_date is None:
            return datetime.date.max  # Push tasks with no due date to the end
        else:
            return due_date  # Sort by actual due date for tasks with due dates

    def print_prioritized_tasks(self):
        if not self.tasks:
            print("No tasks to prioritize.")
            return
        
        print("\nPrioritized Task List:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task['description']} - Priority: {task['priority']} - Due Date: {task['due_date']}")
    
    def display_help(self):
        print("\nTask Master CLI Help & Documentation")
        print("-" * 40)
        print("Commands and Options:")
        print("'q': Quit the program")
        print("'p': Begin prioritization of tasks")
        print("'h' or 'help': Display this help message")
        print("\nTask Entry Format:")
        print("Each task entry should follow the format:")
        print("  Task description -p [h|m|l] -d [due_date]")
        print("  Example: 'Finish report -p h -d 06-30-2024'")
        print("\nNote: Priority ('-p') and Due Date ('-d') are optional.")
        print("Priority defaults to 'm' (medium) if not specified.")
        print("Due Date keywords: t (today), sun, m (Monday), tues, w (Wednesday), th (Thursday), f (Friday), sat.")
        print("Specific date format: MM-DD-YYYY")
