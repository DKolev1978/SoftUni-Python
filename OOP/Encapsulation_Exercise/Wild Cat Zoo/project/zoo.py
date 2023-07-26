from typing import List

from project import Cheetah, Tiger, Lion
from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List = []
        self.workers: List = []

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:
            worker = next(w for w in self.workers if w.name == worker_name)
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except StopIteration:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_workers_salary = sum(w.salary for w in self.workers)
        if total_workers_salary <= self.__budget:
            self.__budget -= total_workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_animal_tend = sum(a.money_for_care for a in self.animals)
        if total_animal_tend <= self.__budget:
            self.__budget -= total_animal_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self,amount):
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals\n"
        lions = [animal for animal in self.animals if isinstance(animal, Lion)]
        tigers = [animal for animal in self.animals if isinstance(animal, Tiger)]
        cheetahs = [animal for animal in self.animals if isinstance(animal, Cheetah)]

        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join(str(l) for l in lions)

        result += f"\n----- {len(tigers)} Tigers:\n"
        result += "\n".join(str(t) for t in tigers)

        result += f"\n----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join(str(c) for c in cheetahs)

        return result

    def workers_status(self) -> str:
        result = f"You have {len(self.workers)} workers\n"
        keepers = [worker for worker in self.workers if worker.__class__.__name__ == "Keeper"]
        caretakers = [worker for worker in self.workers if worker.__class__.__name__ == "Caretaker"]
        vets = [worker for worker in self.workers if worker.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join(str(k) for k in keepers)

        result += f"\n----- {len(caretakers)} Caretakers:\n"
        result += "\n".join(str(c) for c in caretakers)

        result += f"\n----- {len(vets)} Vets:\n"
        result += "\n".join(str(v) for v in vets)

        return result

