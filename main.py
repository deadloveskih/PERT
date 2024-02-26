from work_with_data import init_file, input_fields, output_fields
from PERT import PERT
from pprint import pprint

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
    assert init_file("data/input_data.csv", input_fields)
    assert init_file("data/output_data.csv", output_fields)
    pert = PERT.getInstance()

    while((user_input := input("pert: ")) != "quit"):
        match user_input.split(" "):
            case ["add", *data]:
                if len(data) == 5:
                    pert.add_data(data[0], data[1], data[2], data[3], data[4])
                else:
                    print("using: add 'task_name' 'predecessor/another' (float) (float) (float)")
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
    main();