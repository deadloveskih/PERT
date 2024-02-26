from work_with_data import *
from task import Task

def show_data() -> dict:
    input_data_buf = bufferize("data/input_data.csv")
    output_data_buf = bufferize("data/output_data.csv")

    all_data = list(zip(input_data_buf, output_data_buf))
    tasks = dict()
    for task in all_data:
        task = task[0] | task[1]
        task = Task(
                        task["Task"],
                        task["Predecessor"],
                        task["Optimistic"],
                        task["Nominal"],
                        task["Pessimistic"],
                        task["Time"],
                        task["Deviation"]
                    )
        
        tasks[task.task_name] = task

    return tasks