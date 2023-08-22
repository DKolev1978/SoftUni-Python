from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    @abstractmethod
    def expenses(self) -> int:
        ...

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = 0
        for positions in self.sponsors.values():
            for pos in positions:
                if race_pos <= pos:
                    revenue += positions[pos]
                    break

        revenue -= self.expenses
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"