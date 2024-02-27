from functools import singledispatchmethod
from .task import Task
from .calculations import *
from . import commands
from .work_with_data.fields import input_fields, output_fields
from .work_with_data.init_files import init_file

class PERT:

    __singleton = None

    def __init__(self, csv_write: bool=False, csv_read: bool=False) -> None:
        if csv_write or csv_read:
            assert init_file("PERT/data/input_data.csv", input_fields)
            assert init_file("PERT/data/output_data.csv", output_fields)

        
        self.csv_write = csv_write
        self.csv_read = csv_read
        self.__cache = dict()
        self.show_data()
    
    @classmethod
    def getInstance(cls, *, csv_write=False, csv_read=False) -> object:
        if not cls.__singleton:
            cls.__singleton = PERT(csv_write, csv_read)

        return cls.__singleton

    @singledispatchmethod
    def add_data(self, task_name: str, predecessor: str, optimistic: str, nominal: str, pessimistic: str) -> Task:
        task = commands.add_data(task_name, predecessor, optimistic, nominal, pessimistic, self.csv_write)
        self.__cache[task_name] = task

        return task
    
    @add_data.register(Task)
    def _(self, task: Task) -> Task:
        task = commands.add_data(
                                    task["task_name"],
                                    task["predecessor"],
                                    task["optimistic"],
                                    task["nominal"],
                                    task["pessimistic"],
                                    self.csv_write
                                 )
        
        self.__cache[task.task_name] = task

        return task

    def del_data(self, task_name: str) -> None:
        self.__cache.pop(task_name)
        
        if self.csv_write:
            commands.del_data(task_name)

    def print_data(self, task_name: str) -> Task:
        if self.csv_read and (task := commands.print_data(task_name)):
            return task
        
        return self.__cache.get(task_name, "Not found")

    def show_data(self) -> dict:
        if not self.__cache and self.csv_read:
            self.__cache = commands.show_data()
        
        return self.__cache

    def summarize(self) -> dict:
        return commands.summarize(list(self.__cache.values()))