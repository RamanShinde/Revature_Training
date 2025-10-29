from Oop.Polymorphism.bankdetails import BankDetails


class CreditDetails(BankDetails):
    def __init__(self,customerId,customerName,balance,creditscore,status):
        super().__init__(customerId,customerName,balance)
        self.creditscore=creditscore
        self.status=status

    def welcome_message(self):
        return f"{self.customerName} welcome to bank"

    def display_credit(self):
        return (f"Credit score: {self.creditscore}"
                f"Credit status: {self.status}")