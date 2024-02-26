from work_with_data import *
from calculations import *

def add_data(task_name: str, optimistic: str, nominal: str, pessimistic: str) -> dict:
    if add_input_data(task_name, optimistic, nominal, pessimistic):
        time = calc_time(float(optimistic), float(nominal), float(pessimistic))
        deviation = calc_deviation(float(optimistic), float(pessimistic))
        add_output_data(task_name, str(time), str(deviation))

        return {
                    "Deviation": deviation,
                    "Nominal": nominal,
                    "Optimistic": optimistic,
                    "Pessimistic": pessimistic,
                    "Task": task_name,
                    "Time": time
                }