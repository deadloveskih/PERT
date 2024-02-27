from ..work_with_data import *
from ..calculations import *
from ..task import Task

def add_data(
                task_name: str,
                predecessor: str,
                optimistic: str,
                nominal: str,
                pessimistic: str,
                csv_write: bool
             ) -> Task:
    try:
        float(optimistic)
        float(nominal)
        float(pessimistic)
    except ValueError:
        print("Parametrs for 'add' should be float or integer")
        exit()

    time = calc_time(float(optimistic), float(nominal), float(pessimistic))
    deviation = calc_deviation(float(optimistic), float(pessimistic))

    if csv_write and add_input_data(task_name, predecessor, optimistic, nominal, pessimistic):
        add_output_data(task_name, str(time), str(deviation))

    task = Task(
                    task_name,
                    predecessor,
                    optimistic,
                    nominal,
                    pessimistic,
                    time,
                    deviation
                )

    return task