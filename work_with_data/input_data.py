import csv
import os
from .bufferize import bufferize
from .init_files import init_file
from .fields import input_fields

def add_input_data(task: str, predecessor: str, optimistic: str, nominal: str, pessimistic: str) -> int:
    try:
        float(optimistic)
        float(nominal)
        float(pessimistic)
    except ValueError:
        print("Parametrs for 'add' should be float or integer")
        return 0
    try:
        with open("data/input_data.csv", "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=input_fields)
            writer.writerow({'Task': task, "Predecessor": predecessor, 'Optimistic': optimistic, "Nominal": nominal, "Pessimistic": pessimistic})
    except IOError:
        print("Error: failed open file while add data to input_data")

    return 1

def del_input_data(task: str) -> None:
    buffer_input_data = bufferize("data/input_data.csv")
    for item in buffer_input_data:
        if item["Task"] == task:
            buffer_input_data.remove(item)
    try:
        os.remove("data/input_data.csv")
        assert init_file("data/input_data.csv", input_fields, buffer_input_data)
    except OSError:
        print("Error: failed del data from input_data")