from commands import *
from work_with_data import init_file


def help() -> None:
    print("MIT License Copyright (c) 2024 deadloveskih", end="\n\n")
    print("add command")
    print("\tusing: add 'task_name' (1) (2) (3)", end="\n\n")
    print("\t(1) float optimistic value of time for task")
    print("\t(2) float nominal value of time for task")
    print("\t(3) float pessimistic value of time for task", end="\n\n")
    print("\tadd record in csv files", end="\n\n")
    print("del command")
    print("\tusing: del 'task_name'", end="\n\n")
    print("\tdelete record from csv files", end="\n\n")
    print("print command")
    print("\tusing: print 'task_name'", end="\n\n")
    print("\tprint values of one task", end="\n\n")
    print("show command")
    print("\tusing: show", end="\n\n")
    print("\tprint values of all tasks", end="\n\n")
    print("summarize command")
    print("\tusing: summarize", end="\n\n")
    print("\tprint summarize time and deviation of all tasks", end="\n\n")


def main() -> None:
    assert init_file("data/input_data.csv", ["Task", "Optimistic", "Nominal", "Pessimistic"])
    assert init_file("data/output_data.csv", ["Task", "Time", "Deviation"])

    while((user_input := input("pert: ")) != "quit"):
        match user_input.split(" "):
            case ["add", *data]:
                if len(data) == 4:
                    add_data(data[0], data[1], data[2], data[3])
                else:
                    print("using: add 'task_name' (float) (float) (float)")
            case ["del", task_name]:
                del_data(task_name)
            case ["print", task_name]:
                print_data(task_name)
            case ["show"]:
                show_data()
            case ["summarize"]:
                summarize()
            case ["help"]:
                help()
            case _:
                print(f"Undefined command: {user_input}")
                


if __name__ == "__main__":
    main();