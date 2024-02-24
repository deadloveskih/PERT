from os import path
import csv

def init_file(csv_path: str, fields: list, *args) -> None:
    if not path.exists(csv_path):
        try:
            with open(csv_path, "w") as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(fields)
                if args:
                    writer = csv.DictWriter(csv_file, fieldnames=fields)
                    writer.writerows(args[0])
        except IOError:
            print("Error: failed creating files")
            return 0        
    
    return 1