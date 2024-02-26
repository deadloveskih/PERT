from work_with_data import *
from calculations import *

def del_data(task_name: str) -> None:
    del_input_data(task_name)
    del_output_data(task_name)