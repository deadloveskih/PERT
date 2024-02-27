from .work_with_data import init_file, input_fields, output_fields
from .PERT import PERT
from pprint import pprint

def help() -> None:
    print("MIT License Copyright (c) 2024 deadloveskih", end="\n\n")

    print("add command")
    print("\tusing: add 'task_name' 'predecessor/another/etc' (1) (2) (3)", end="\n\n")
    print("\t(1) float optimistic value of time for task")
    print("\t(2) float nominal value of time for task")
    print("\t(3) float pessimistic value of time for task", end="\n\n")
    print("\tadd record in csv files(if csv_write=True) and cache", end="\n\n")

    print("del command")
    print("\tusing: del 'task_name'", end="\n\n")
    print("\tdelete record from csv files(if csv_write=True) and cache", end="\n\n")

    print("print command")
    print("\tusing: print 'task_name'", end="\n\n")
    print("\tprint values of one task", end="\n\n")

    print("show command")
    print("\tusing: show", end="\n\n")
    print("\tloads data from csv(if csv_read=True) to cache and print values of all tasks from cache", end="\n\n")

    print("summarize command")
    print("\tusing: summarize", end="\n\n")
    print("\tprint summarize time and deviation of cached tasks", end="\n\n")

def intercative(*, csv_write: bool, csv_read: bool) -> None:
    pert = PERT.getInstance(csv_write, csv_read)

    while((user_input := input("pert: ")) != "quit"):
        match user_input.split(" "):
            case ["add", *data]:
                if len(data) == 5:
                    pert.add_data(data[0], data[1], data[2], data[3], data[4])
                else:
                    print("using: add 'task_name' 'predecessor/another/etc' (float) (float) (float)")
            case ["del", task_name]:
                pert.del_data(task_name)
            case ["print", task_name]:
                pprint(pert.print_data(task_name), width=40)
            case ["show"]:
                pprint(pert.show_data(), width=40)
            case ["summarize"]:
                pprint(pert.summarize(), width=40)
            case ["help"]:
                help()
            case _:
                print(f"Undefined command: {user_input}")

  
if __name__ == "__main__":
    intercative();