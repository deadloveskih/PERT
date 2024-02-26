import commands


class PERT:

    __singleton = None

    def __init__(self) -> None:
        self.__cache = []
    
    @classmethod
    def getInstance(cls) -> object:
        if not cls.__singleton:
            cls.__singleton = PERT()

        return cls.__singleton

    def add_data(self, task_name: str, optimistic: str, nominal: str, pessimistic: str) -> dict:
        task = commands.add_data(task_name, optimistic, nominal, pessimistic)
        self.__cache.append(task)

        return task

    def del_data(self, task_name: str) -> None:
        for task in self.__cache:
            if task["Task"] == task_name:
                self.__cache.remove(task)
            
        return commands.del_data(task_name)

    def print_data(self, task_name: str) -> dict:
        for task in self.__cache:
            if task["Task"] == task_name:
                return task
            
        return commands.print_data(task_name)

    def show_data(self) -> list:
        return commands.show_data()

    def summarize(self) -> dict:
        return  commands.summarize()