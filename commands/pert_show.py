from ..work_with_data import *
from ..task import Task

def show_data() -> dict:
    input_data_buf = bufferize("PERT/data/input_data.csv")
    output_data_buf = bufferize("PERT/data/output_data.csv")

    all_data = list(zip(input_data_buf, output_data_buf))
    tasks = dict()
    for task in all_data:
        task = task[0] | task[1]
        task = Task(
                        task["task_name"],
                        task["predecessor"],
                        task["optimistic"],
                        task["nominal"],
                        task["pessimistic"],
                        task["time"],
                        task["deviation"]
                    )
        
        tasks[task.task_name] = task

    return tasks