from ..work_with_data import *

def print_data(task_name: str) -> dict:
    input_data_buf = bufferize("data/input_data.csv")
    output_data_buf = bufferize("data/output_data.csv")
    
    input_data_task = [task for task in input_data_buf if task["Task"] == task_name].pop()
    output_data_task = [task for task in output_data_buf if task["Task"] == task_name].pop()

    result = input_data_task.items() | output_data_task.items()
    return dict(result)
