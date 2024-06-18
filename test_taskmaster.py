import pytest
from task_manager import TaskManager
from utils import parse_task_entry
import datetime
from unittest.mock import patch

# Helper function to setup TaskManager
def create_task_manager():
    manager = TaskManager()
    return manager

def test_add_task_without_priority_or_due_date():
    manager = create_task_manager()
    task_entry = "Finish report"
    task = parse_task_entry(task_entry)
    manager.tasks.append(task)
    assert task['description'] == 'Finish report'
    assert task['priority'] == 'm'
    assert task['due_date'] is None

def test_add_task_with_high_priority():
    manager = create_task_manager()
    task_entry = "Prepare presentation -p h"
    task = parse_task_entry(task_entry)
    manager.tasks.append(task)
    assert task['description'] == 'Prepare presentation'
    assert task['priority'] == 'h'
    assert task['due_date'] is None

def test_add_task_with_due_date_keyword():
    manager = create_task_manager()
    task_entry = "Grocery shopping -d sun"
    task = parse_task_entry(task_entry)
    manager.tasks.append(task)
    assert task['description'] == 'Grocery shopping'
    assert task['priority'] == 'm'
    assert task['due_date'] is not None

def test_add_task_with_specific_date():
    manager = create_task_manager()
    task_entry = "Dentist appointment -d 06-23-2024"
    task = parse_task_entry(task_entry)
    manager.tasks.append(task)
    assert task['description'] == 'Dentist appointment'
    assert task['priority'] == 'm'
    assert task['due_date'] == datetime.date(2024, 6, 23)

def test_invalid_priority():
    manager = create_task_manager()
    task_entry = "Clean the house -p x"
    task = parse_task_entry(task_entry)
    assert task is None

def test_invalid_date_format():
    manager = create_task_manager()
    task_entry = "Gym session -d 2024-23-06"
    task = parse_task_entry(task_entry)
    assert task is None

def test_default_priority_is_medium():
    manager = create_task_manager()
    task_entry = "Read book"
    task = parse_task_entry(task_entry)
    manager.tasks.append(task)
    assert task['description'] == 'Read book'
    assert task['priority'] == 'm'
    assert task['due_date'] is None

def test_due_date_keyword_today():
    manager = create_task_manager()
    task_entry = "Team meeting -d t"
    task = parse_task_entry(task_entry)
    manager.tasks.append(task)
    assert task['description'] == 'Team meeting'
    assert task['priority'] == 'm'
    assert task['due_date'] == datetime.date.today()

@patch('builtins.input', side_effect=['q'])
def test_program_exit_on_q_command(mock_input):
    manager = create_task_manager()
    result = manager.run()
    assert result is None  # Assuming 'q' exits the program cleanly

@patch('builtins.input', side_effect=['p'])
def test_start_prioritization_on_p_command(mock_input):
    manager = create_task_manager()
    result = manager.run()
    assert result == 'Begin prioritization selections'
