class Employees():
    def __init__(self,name,last):
        self.name=name
        self.last=last

class Supervisors(Employees):
    def __init__(self, name, last,password):
        super().__init__(name, last)
        self.password=password

class Chefs(Employees):
    def request_leave(self,days):
        return self.name + " wants leave for "+ str(days) + " days."

adrian=Supervisors("Adrian","A","abc")

corey=Chefs("Corey","C")
print(adrian.password)
print(corey.last)
print(corey.request_leave(5))