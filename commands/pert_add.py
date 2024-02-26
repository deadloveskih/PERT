from work_with_data import *
from calculations import *
from .pert_print import print_data

def add_data(task_name: str, optimistic: str, nominal: str, pessimistic: str) -> dict:
    if add_input_data(task_name, optimistic, nominal, pessimistic):
        time = calc_time(float(optimistic), float(nominal), float(pessimistic))
        deviation = calc_deviation(float(optimistic), float(pessimistic))
        add_output_data(task_name, str(time), str(deviation))

    return print_data(task_name)