class Task:
    def __init__(
                    self,
                    task_name: str,
                    predecessor: str,
                    optimistic: str,
                    nominal: str,
                    pessimistic: str,
                    time: str="",
                    deviation: str=""
                 ) -> None:
        
        self.task_name = task_name
        self.predecessor = predecessor
        self._followers = dict()
        self.optimistic = optimistic
        self.nominal = nominal
        self.pessimistic = pessimistic
        self.time = time
        self.deviation = deviation

    def __repr__(self) -> str:
        string = f"""
    {"_"*40}
    Task: {self.task_name}
    Predecessor: {self.predecessor.keys()}
    Follower: {self._followers.keys()}
    Optimistic: {self.optimistic}
    Nominal: {self.nominal}
    Pessimistic: {self.pessimistic}
    Time: {self.time}
    Deviation: {self.deviation}
    {"_"*40}
"""

        return string

    def __getitem__(self, attr: str) -> any:
        return self.__dict__[attr]
    
    def __setitem__(self, attr: str, value: object) -> None:
        self.__setattr__(attr, value)