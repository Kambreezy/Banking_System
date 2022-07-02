class account:
    accHolder = ""
    amount = 0.00
    balance = 0.00
    def createAccount(self):
        desc = "Account %s has been created and $ %.2f deposited. New balance is $ %.2f" % (self.accHolder,self.amount,self.balance)
        return desc
bank = 'Wananchi Bank'
location ='321 Street Rd Kenya'
customer = input('Enter your name ')
print('Hello ' + customer + ", welcome to "+ bank + " located at " + location)
print("Select from the following options \n")
print("0. Create Account")
print("1. Exit App")
choice = int(input("Enter your selection "))
if choice == 0:
    new_account = account()
    new_account.accHolder = input("Enter new account name ")
    new_account.amount = float(input("How much do yu wanna deposit "))
    new_account.balance = new_account.amount
    print(new_account.createAccount())
elif choice == 1:
    print(''' 
    Thank you for checking us out.
    This is just a test program yet to be scaled.
    Developer: Amos Kambreezy. Github:https://github.com/Kambreezy
    ''')
else:
    print("Invalid Choice")


