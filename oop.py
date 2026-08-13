class Payslip:
    def __init__(self,name,payment,amount):
        self.name=name
        self.payment=payment
        self.amount=amount

    def pay(self):
        self.payment="yes"

    def status(self):
        if self.payment=="yes":
            return self.name + " is paid: " + str(self.amount)
        else:
            return self.name +" is not paid yet"

john=Payslip("John","no",1000)
corey=Payslip("Corey","no",3000)

print(john.status())
print(corey.status())

corey.pay()

print("After payemnt")
print(corey.status())