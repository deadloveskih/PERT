from work_with_data import *

def show_data() -> list:
    input_data_buf = bufferize("data/input_data.csv")
    output_data_buf = bufferize("data/output_data.csv")

    all_data = list(zip(input_data_buf, output_data_buf))
    tasks = []
    for task in all_data:
        tasks.append(task[0] | task[1])

    return tasks