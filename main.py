from commands import *
from work_with_data import init_file


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
                break
            case _:
                print(f"Undefined command: {user_input}")
                


if __name__ == "__main__":
    main();