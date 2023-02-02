class Atm:
    # constractor also called special/magic/dunder methood
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
            Welcome to Sumit's Bank :)
            Hello how would you like to proceed ?
            1. Enter 1 to create pin
            2. Enter 2 to deposit
            3. Enter 3 to withdrall
            4. Enter 4 to check the balance
            5. Enter 5 to exit
        """)
        if user_input == "1" :
            print("You selected create pin option")
            self.create_pin()
        elif user_input == "2":
            print("You selected deposit option")
            self.deposit()
        elif user_input == "3":
            print("You selected withdrall option")
            self.withdral()
        elif user_input == "4":
            print("You selected check balance option")
            self.check_ballance()
        elif user_input == "5":
            print("You selected exit")
            self.exit_code()
        else:
            print("Please choose the right option")

    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin set successfully")
        self.menu()

    def deposit(self):
        print("Enter your pin: ")
        entered_pin = input()
        if(entered_pin == self.pin):
            self.temp_bal = int(input("Enter your ballance: "))
            self.balance = self.balance + self.temp_bal
            print("Deposit successful")
            self.menu()
        else:
            print("Entered pin is not valid !")
            self.menu()

    def withdral(self):
        print("Enter your pin: ")
        entered_pin = input()
        if(entered_pin == self.pin):
            with_bal = int(input("Enter amount: "))
            if(with_bal <= self.balance):
                self.balance = self.balance - with_bal
                print("Withdrall successful")
                self.menu()
            else:
                print("Insufficiant ballance")
                self.menu()
        else:
            print("Entered pin is invalid")
            self.menu()

    def check_ballance(self):
        print("Enter your pin: ")
        entered_pin = input()
        if(entered_pin == self.pin):
            print("Current ballance is ", self.balance)
            self.menu()
        else:
            print("Entered pin is invalid")
            self.menu()

    def exit_code(self):
        print("Visit Again :) Thanks")

per1 = Atm()
