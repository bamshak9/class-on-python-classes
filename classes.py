class RegForm:
    amount_expected_to_be_paid =50000
    def __init__(self, firstname, lastname, address, amount):
        self.firstname=firstname
        self.lastname=lastname
        self.address= address
        self.amount_paid_by_student=amount
        self.amount_due= self.amount_expected_to_be_paid-amount
    def details(self):
        return f"firstname: {self.firstname}\nlastname: {self.lastname}\naddress: {self.address}\namount paid: {self.amount_paid_by_student}"
    def welcome(self):
        return f"Welcome to Blockfuse Labs {self.firstname} {self.lastname}"
    def balance(self):
        return f"{self.firstname}'s amount due is {self.amount_due}"
    def balance_checker(self):
        if self.amount_due==0:
            return f"You have completely paid your fees congratulations!"
        elif self.amount_due>0:
            return f"Your balance to pay off is {self.amount_due}"
        else:
            return f"You have overpaid by {self.amount_due}"
Joseph =RegForm("Joseph", "Bienose", "Jos", 30000)
Mary =RegForm("Mary", "Jackie", "Lagos", 50000)
print(Joseph)
'''
print(Joseph.firstname)
print(Joseph.amount_expected_to_be_paid)
print(Joseph.amount_expected_to_be_paid,Joseph.firstname, Joseph.lastname, Joseph.address, Joseph.amount_paid_by_student)
'''
print(Joseph.details())
print(Joseph.welcome())
print(Joseph.balance())
print(Mary.balance())
print(Joseph.balance_checker())
print(Mary.balance_checker())