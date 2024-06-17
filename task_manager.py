from utils import parse_task_entry

class TaskManager:
    def __init__(self):
        self.tasks = []

    def run(self):
        print("Enter tasks to be prioritized (type 'p' to begin prioritization selections, 'q' to quit):")
        while True:
            entry = input()
            if entry.lower() == 'p':
                break
            elif entry.lower() == 'q':
                return
            else:
                task = parse_task_entry(entry)
                if task:
                    self.tasks.append(task)
                    print("Task added:", task)
                else:
                    print("Invalid task format. Please try again.")
        
        print("\nTasks to be prioritized:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['description']} (Priority: {task['priority'].upper()}, Due Date: {task['due_date']})")

        # The next steps would involve the pairwise comparison and outputting the prioritized list
        # but we'll start with task entry and parsing.

