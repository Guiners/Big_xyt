from re import T

from numpy import number


class Stock:
    def __init__(self) -> None:
        self.price = 0
        self.quantity = 0
        self.order = ""
        self.type = ""
        self.id = 0
        self.info = []

    def print_info(self) -> None:
        print("ID   ORDER   TYPE   PRICE   QUANTITY")
        self.info.append([
            str(self.id).rjust(3, "0"),
            self.order,
            self.type,
            self.price,
            self.quantity,
        ])
        for operation in self.info:
            for i in operation:
                print(i, end="    ")

    def update_info(self, order: str, type: str) -> None:
        self.order = order
        self.type = type
        self.id += 1

    def get_user_input(self) -> int:
        user_input = int(input())
        while type(user_input) is number == False:
            print("Excepted integer")
            user_input = int(input())
        return user_input
        

    def main(self) -> None:
        while True:
            print("\nPress 1 if you want to buy stocks")
            print("Press 2 if you want to sell stocks")
            print("Press 3 if you want to close program")
        
            user_input = self.get_user_input()

            if user_input == 3:
                break
            elif not(user_input in [1,2,3]):
                print("Invalid number, try again")
                continue
            try:
                self.price = float(input("Input price: "))
                self.quantity = int(input("Input quantity: "))
            except:
                print("Excepted integer")
                continue

            if self.quantity < 0 or self.price < 0:
                print("Number is negative, please input positive number")
                continue
            
            if user_input == 1:
                self.update_info("Buy", "Add")
            elif user_input == 2:
                self.update_info("Sell", "Remove")
            
            self.print_info()