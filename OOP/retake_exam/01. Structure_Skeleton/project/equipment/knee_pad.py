from project.equipment.base_equipment import BaseEquipment


class KneePad(BaseEquipment):
    PRICE = 15.0

    def __init__(self, protection: int = 120):
        super().__init__(protection, self.PRICE)

    @staticmethod
    def increase_price():
        KneePad.PRICE += KneePad.PRICE * 0.2
