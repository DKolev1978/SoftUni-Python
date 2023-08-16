from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):

    def __init__(self, name: str, country: str, advantage: int, budget: float = 1_000.0):
        super().__init__(name, country, advantage, budget)
        # self.equipment: list = []

    def win(self):
        self.advantage += 115
        self.wins += 1

