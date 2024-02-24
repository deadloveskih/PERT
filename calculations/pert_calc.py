from math import sqrt

def calc_time(optimistic: float, nominal: float, pessimistic: float) -> float:
    return (optimistic + 4*nominal + pessimistic)/6

def calc_deviation(optimistic: float, pessimistic: float) -> float:
    return (pessimistic - optimistic)/6

def calc_time_sum(list_tasks: list) -> float:
    time_sum = 0
    for task in list_tasks:
        time_sum += float(task["Time"])

    return round(time_sum, 3)

def calc_deviation_sum(list_tasks: list) -> float:
    deviation_sum = 0
    for task in list_tasks:
        deviation_sum += float(task["Deviation"])**2

    return round(sqrt(deviation_sum), 3)
