# Updated utils.py

import datetime
import re

def parse_task_entry(entry):
    task = {}
    match = re.match(r'^(.*?)\s*(-p\s*[hml])?\s*(-d\s*(t|sun|mon|tues|wed|thu|fri|sat|\d{2}-\d{2}-\d{4}))?$', entry, re.IGNORECASE)
    if match:
        task['description'] = match.group(1).strip()
        priority = match.group(2)
        due_date = match.group(4)
        
        if priority:
            pr = priority.split()[1].lower()
            if pr in ['h', 'm', 'l']:
                task['priority'] = pr
            else:
                return None  # Invalid priority
        else:
            task['priority'] = 'm'  # Default priority is medium
        
        if due_date:
            task['due_date'] = parse_due_date(due_date.lower())
            if task['due_date'] is None:
                return None  # Invalid due date format
        else:
            task['due_date'] = None
        
        return task
    else:
        return None

def parse_due_date(due_date):
    today = datetime.date.today()
    days = {'t': 0, 'mon': 0, 'tues': 1, 'wed': 2, 'thu': 3, 'fri': 4, 'sat': 5, 'sun': 6}
    if due_date == 't':
        return today
    if due_date in days:
        delta_days = (days[due_date] - today.weekday() + 7) % 7
        if delta_days == 0:
            delta_days = 7  # Ensure the due date is set to the next occurrence
        return today + datetime.timedelta(days=delta_days)
    try:
        return datetime.datetime.strptime(due_date, '%m-%d-%Y').date()
    except ValueError:
        return None
