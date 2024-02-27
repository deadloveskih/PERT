from ..work_with_data import *
from ..calculations import *
from ..task import Task

def add_data(task_name: str, predecessor: str, optimistic: str, nominal: str, pessimistic: str) -> Task:
    if add_input_data(task_name, predecessor, optimistic, nominal, pessimistic):
        time = calc_time(float(optimistic), float(nominal), float(pessimistic))
        deviation = calc_deviation(float(optimistic), float(pessimistic))
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