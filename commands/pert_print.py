from ..work_with_data import *
from ..task import Task

def print_data(task_name: str) -> dict:
    input_data_buf = bufferize("PERT/data/input_data.csv")
    output_data_buf = bufferize("PERT/data/output_data.csv")
    
    input_data_task = [task for task in input_data_buf if task["task_name"] == task_name]
    output_data_task = [task for task in output_data_buf if task["task_name"] == task_name]

    if input_data_task:
        task = input_data_task[0] | output_data_task[0]
        task = Task(
                            task["task_name"],
                            task["predecessor"],
                            task["optimistic"],
                            task["nominal"],
                            task["pessimistic"],
                            task["time"],
                            task["deviation"]
                        )
        
        return task
