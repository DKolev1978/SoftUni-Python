from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    PRICE = 25.0

    def __init__(self, protection):
        super().__init__(protection, self.PRICE)

    @staticmethod
    def increase_price():
        ElbowPad.PRICE += ElbowPad.PRICE * 0.1
