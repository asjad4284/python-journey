from abc import ABC, abstractmethod

class Bank(ABC):

    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"
    @abstractmethod
    def withdraw(self,amount):
        pass

class Swiss(Bank):
    def __init__(self):
        self.bal=1000
    
    def basicinfo(self):
        print("This is the Swiss bank")
        return "Swiss Bank: " + str(self.bal)
    
    def withdraw(self,amount):
        if self.bal > amount:
            self.bal=self.bal-amount
            print("Withdrawn amount:",amount)
            print("New Balance:",self.bal)
            return self.bal
        else:
            print("Insufficient funds")
            return self.bal

def main():
    assert issubclass(Bank, ABC)
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()
