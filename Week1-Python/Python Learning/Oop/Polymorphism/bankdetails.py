

class BankDetails:
    def __init__(self,customerId,customerName,Balance):
        self.customerId=customerId
        self.customerName=customerName
        self.Balance=Balance

    def welcome_message(self):
        return "Welcome to Our Bank"

    def display(self):
        return (f'customerId:-{self.customerId}\t'
                f'CustomerName:-{self.customerName}\t'
                f'Balance:-{self.Balance}')
