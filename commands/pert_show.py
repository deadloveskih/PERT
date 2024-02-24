import pprint
from work_with_data import *

def show_data() -> None:
    input_data_buf = bufferize("data/input_data.csv")
    output_data_buf = bufferize("data/output_data.csv")

    all_data = list(zip(input_data_buf, output_data_buf))
    for task in all_data:
        print("_"*40)
        task = task[0] | task[1]
        pprint.pprint(task, width=40)
        print("_"*40)