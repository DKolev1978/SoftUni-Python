from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_TEAM_TYPES = {'IndoorTeam': IndoorTeam, "OutdoorTeam": OutdoorTeam}
    VALID_EQUIPMENT = {'KneePad': KneePad, 'ElbowPad': ElbowPad}
    VALID_EQUIPMENT_TYPES_PRICES = {"KneePad": 15, "ElbowPad": 25}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list = []
        self.teams: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")

        self.__name = value

    def create_team(self, team_type: str, team_name: str, country: str, advantage: int):
        return self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)

    def add_equipment(self, equipment_type: str):
        if equipment_type not in BaseEquipment.VALID_EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")

        self.equipment.append(equipment_type)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")
        if self.capacity == 0:
            raise Exception("Not enough tournament capacity.")
        new_team = self.create_team(team_type, team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def get_team_type(self, team_name):
        team_type = [name for name in self.teams if name.name == team_name]
        return team_type[0]

    def get_team_by_name(self, team_name):
        team_name = [name for name in self.teams if name.name == team_name]
        return team_name[0]

    def sell_equipment(self, equipment_type: str, team_name: str):
        current_team_type = self.get_team_type(team_name)
        if self.VALID_EQUIPMENT_TYPES_PRICES[equipment_type] > current_team_type.budget:
            raise Exception("Budget is not enough!")

        equipment = self.equipment.remove(equipment_type)
        team_name_current = self.get_team_by_name(team_name)
        team_name_current.equipment.append(equipment)
        team_name_current.budget -= self.VALID_EQUIPMENT_TYPES_PRICES[equipment_type]
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        if not self.get_team_by_name(team_name):
            raise Exception("No such team!")
        wins = self.get_team_by_name(team_name)
        if wins.wins > 0:
            raise Exception(f"The team has {wins.wins} wins! Removal is impossible!")
        current_team_name = self.get_team_by_name(team_name)
        self.teams.remove(current_team_name)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        equipment_to_raise_prices = self.VALID_EQUIPMENT[equipment_type]
        equipment_to_raise_prices.increase_price()
        for el in self.equipment:
            equipment_count = 0
            if equipment_type == el:
                equipment_count += 1
        return f"Successfully changed {equipment_count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        pass

    def get_statistics(self):
        return f"Tournament: {self.name}\n" \
               f"Number of Teams: {self.capacity}\n" \
               f"Teams:"




t = Tournament('SoftUniada2023', 2)

print(t.add_equipment('KneePad'))
print(t.add_equipment('ElbowPad'))

print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))

print(t.sell_equipment('KneePad', 'Spartak'))

print(t.remove_team('Levski'))
print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))

print(t.increase_equipment_price('ElbowPad'))
print(t.increase_equipment_price('KneePad'))

print(t.play('Lokomotiv', 'Spartak'))

print(t.get_statistics())
