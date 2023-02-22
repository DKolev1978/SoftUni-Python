class Party:
    def __init__(self):
        self.people = []


party_people = Party()
line = input()
while line != "End":
    party_people.people.append(line)
    line = input()
print(f"Going: {', '.join(party_people.people)}")
print(f"Total: {len(party_people.people)}")