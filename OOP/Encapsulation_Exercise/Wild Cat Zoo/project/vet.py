from project.worker import Worker


class Vet(Worker):
    def __int__(self, name: str, age: int, salary: int) -> None:
        super().__int__(name, age, salary)
