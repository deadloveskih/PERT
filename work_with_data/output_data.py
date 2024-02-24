import csv
import os
from .bufferize import bufferize
from .init_files import init_file


fields = ["Task", "Time", "Deviation"]

def add_output_data(task: str, time: str, deviation: str) -> None:
    try:
        with open("data/output_data.csv", "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writerow({'Task': task, 'Time': time, "Deviation": deviation})
    except IOError:
        print("Error: failed open file while add data to output_data")

def del_output_data(task: str) -> None:
    buffer_input_data = bufferize("data/output_data.csv")
    for item in buffer_input_data:
        if item["Task"] == task:
            buffer_input_data.remove(item)
    try:
        os.remove("data/output_data.csv")
        assert init_file("data/output_data.csv", fields, buffer_input_data)
    except OSError:
        print("Error: failed del data from output_data")