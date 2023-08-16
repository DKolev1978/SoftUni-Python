from abc import ABC, abstractmethod


class BaseEquipment(ABC):
    VALID_EQUIPMENT_TYPES = ["KneePad", "ElbowPad"]
    VALID_EQUIPMENT_TYPES_PRICES = {"KneePad": 15, "ElbowPad": 25}

    def __init__(self, protection: int, price: float):
        self.protection = protection
        self.price = price

    @abstractmethod
    def increase_price(self):
        ...
