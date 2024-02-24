from work_with_data import *
from calculations import *

def add_data(task: str, optimistic: str, nominal: str, pessimistic: str) -> None:
    add_input_data(task, optimistic, nominal, pessimistic)
    time = calc_time(float(optimistic), float(nominal), float(pessimistic))
    deviation = calc_deviation(float(optimistic), float(pessimistic))
    add_output_data(task, str(time), str(deviation))