class Atm(object):
    def __init__(self,atmCardNumber,pinNumber):
        self.atmCardNumber = atmCardNumber
        self.pinNumber     = pinNumber

    def usersInputs(self):
        atmCardNumber = int(input("Enter your ATM card's number"))
        pinNumber     = int(input("Enter the pin number"))

    def cashWithdrawal(self):
        withdrawalAmount = int(input("Enter the withdrawal amount:- "))
        amount = 50000 - withdrawalAmount
        print("Now the balance is ",amount)

    def balanceAmount(self):
        print("Amount is 50,000")
        

vibha = Atm("1234567890","5000")
print(vibha.atmCardNumber,vibha.pinNumber)
print("Press 1 to withdraw money from your account")
print("Press 2 to check the balance amount in your account")
numberEntered = int(input("Enter number:- "))
if(numberEntered == 1):
    vibha.cashWithdrawal()
elif(numberEntered == 2):
    vibha.balanceAmount()
else:
    print("Invalid number entered")