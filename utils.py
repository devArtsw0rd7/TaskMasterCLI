import datetime
import re

def parse_task_entry(entry):
    task = {}
    match = re.match(r'^(.*?)\s*(-p\s*[hml])?\s*(-d\s*(t|sun|m|tues|w|th|f|sat|\d{2}-\d{2}-\d{4}))?$', entry, re.IGNORECASE)
    if match:
        task['description'] = match.group(1).strip()
        priority = match.group(2)
        due_date = match.group(4)
        
        if priority:
            task['priority'] = priority.split()[1].lower()
        else:
            task['priority'] = 'm'  # Default priority is medium
        
        if due_date:
            task['due_date'] = parse_due_date(due_date.lower())
        else:
            task['due_date'] = None
        
        return task
    else:
        return None

def parse_due_date(due_date):
    today = datetime.date.today()
    days = {'t': 0, 'm': 0, 'tues': 0, 'w': 0, 'th': 0, 'f': 0, 'sat': 0, 'sun': 0}
    for day, day_number in zip(days.keys(), range(7)):
        if day == due_date:
            delta_days = (day_number - today.weekday()) % 7
            return today + datetime.timedelta(days=delta_days)
    try:
        return datetime.datetime.strptime(due_date, '%m-%d-%Y').date()
    except ValueError:
        return None
