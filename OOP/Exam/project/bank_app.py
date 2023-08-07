from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOANS = ["StudentLoan", "MortgageLoan"]
    VALID_CLIENTS = ["Student", "Adult"]
    STUDENT_VALID_LOAN = "StudentLoan"
    ADULT_VALID_LOAN = "MortgageLoan"

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        if loan_type == Student.LOAN_TYPE:
            loan = StudentLoan()
            self.loans.append(loan)

        if loan_type == Adult.LOAN_TYPE:
            loan = MortgageLoan()
            self.loans.append(loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if self.capacity <= 0:
            return "Not enough bank capacity."

        if client_type == Student.CLIENT_TYPE:
            client = Student(client_name, client_id, income)
            self.clients.append(client)

        else:
            client = Adult(client_name, client_id, income)
            self.clients.append(client)

        self.capacity -= 1
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan_type_class = [cl.LOAN_TYPE for cl in self.clients if cl.client_id == client_id][0]
        if loan_type_class != loan_type:
            raise Exception("Inappropriate loan type!")
        client_to_remove_add = [c for c in self.clients if c.client_id == client_id]
        client_name = client_to_remove_add[0]

        return f"Successfully granted {loan_type} to {client_name} with ID {client_id}."

    def remove_client(self, client_id: str):
        pass

    def increase_loan_interest(self, loan_type: str):
        pass

    def increase_clients_interest(self, min_rate: float):
        pass

    def get_statistics(self):
        result = f"Active Clients: {len(self.clients)}\n"
        return result


bank = BankApp(3)

print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))
print(bank.add_loan('StudentLoan'))
print(bank.add_loan('MortgageLoan'))

print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))
print(bank.get_statistics())

print(bank.grant_loan('StudentLoan', '1234567891'))
print(bank.grant_loan('MortgageLoan', '1234567000'))
print(bank.grant_loan('MortgageLoan', '1234567000'))

print(bank.remove_client('1234567999'))

print(bank.increase_loan_interest('StudentLoan'))
print(bank.increase_loan_interest('MortgageLoan'))

print(bank.increase_clients_interest(1.2))
print(bank.increase_clients_interest(3.5))

print(bank.get_statistics())
