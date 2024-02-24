import csv
import os
from .bufferize import bufferize
from .init_files import init_file

fields = ["Task", "Optimistic", "Nominal", "Pessimistic"]

def add_input_data(task: str, optimistic: str, nominal: str, pessimistic: str) -> None:
    try:
        with open("data/input_data.csv", "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writerow({'Task': task, 'Optimistic': optimistic, "Nominal": nominal, "Pessimistic": pessimistic})
    except IOError:
        print("Error: failed open file while add data to input_data")

def del_input_data(task: str) -> None:
    buffer_input_data = bufferize("data/input_data.csv")
    for item in buffer_input_data:
        if item["Task"] == task:
            buffer_input_data.remove(item)
    try:
        os.remove("data/input_data.csv")
        assert init_file("data/input_data.csv", fields, buffer_input_data)
    except OSError:
        print("Error: failed del data from input_data")