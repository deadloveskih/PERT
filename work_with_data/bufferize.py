import csv

def bufferize(csv_path: str) -> list:
    try:
        with open(csv_path, "r") as csv_file:
            buffer = []
            reader = csv.DictReader(csv_file)

            for row in reader:
                buffer.append(row)

            return buffer
    except IOError:
        print("Error: failed open file while bufferize data")