from abc import ABC


class Supply(ABC):
    def __init__(self, name: str, energy: int):
        self.name = name
        self.energy = energy

