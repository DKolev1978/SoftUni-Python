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

    def add_equipment(self, equipment_type: str):
        if equipment_type not in BaseEquipment.VALID_EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")
        eq_type = self.VALID_EQUIPMENT[equipment_type](equipment_type)
        self.equipment.append(eq_type)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAM_TYPES:
            raise Exception("Invalid team type!")
        if self.capacity == 0:
            raise Exception("Not enough tournament capacity.")
        new_team = self.VALID_TEAM_TYPES[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def _get_team(self, team_name):
        cur_team = [team for team in self.teams if team.name == team_name]
        if cur_team:
            return cur_team[0]
        return None

    def _calculate_equipment_prices(self, equipment_type):
        equipment_type_price = 0
        for eq_type in self.equipment:
            if eq_type == "KneePad":
                equipment_type_price += 15
            else:
                equipment_type_price += 25
        return equipment_type_price

    def _get_equipment(self, equipment_type):
        cur_eq = [eq for eq in self.equipment if eq.__class__.__name__ == equipment_type]
        print(cur_eq, "Fuck you")
        print(cur_eq[0], "Fuck you")
        return cur_eq[0] if cur_eq else None

    def sell_equipment(self, equipment_type: str, team_name: str):
        current_team = self._get_team(team_name)
        cur_eq = self._get_equipment(equipment_type)
        equipment_type_price = self._calculate_equipment_prices(equipment_type)
        if equipment_type_price > current_team.budget:
            raise Exception("Budget is not enough!")

        current_team.budget -= equipment_type_price
        self.equipment.remove(cur_eq)
        current_team.equipment.append(cur_eq)

        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team_for_removal = self._get_team(team_name)
        if not team_for_removal:
            raise Exception("No such team!")
        if team_for_removal.wins > 0:
            raise Exception(f"The team has {team_for_removal.wins} wins! Removal is impossible!")
        self.teams.remove(team_for_removal)
        return f"Successfully removed {team_for_removal.name}."

    def increase_equipment_price(self, equipment_type: str):

        # equipment_to_raise_prices.increase_price()
        # for el in self.equipment:
        #     equipment_count = 0
        #     if equipment_type == el:
        #         equipment_count += 1
        # return f"Successfully changed {equipment_count}pcs of equipment."

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
