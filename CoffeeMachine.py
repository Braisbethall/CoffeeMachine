class CoffeeMachine:

    def __init__(self, current_water, current_milk, current_coffee_beans, current_cups, current_money):
        self.water = current_water
        self.milk = current_milk
        self.coffee_beans = current_coffee_beans
        self.cups = current_cups
        self.money = current_money

    def fill(self):
        print("Write how many ml of water you want to add:")
        water_supply = int(input())
        print("Write how many ml of milk you want to add:")
        milk_supply = int(input())
        print("Write how many grams of coffee beans you want to add:")
        coffee_beans_supply = int(input())
        print("Write how many disposable coffee cups you want to add:")
        cups_supply = int(input())
        self.water += water_supply
        self.milk += milk_supply
        self.coffee_beans += coffee_beans_supply
        self.cups += cups_supply

    def ingredient_check(self, needed_cups, needed_water, needed_milk, needed_coffee_beans):
        if self.cups < needed_cups:
            return "cups"
        elif self.water < needed_water:
            return "water"
        elif self.milk < needed_milk:
            return "milk"
        elif self.coffee_beans < needed_coffee_beans:
            return "coffee beans"
        else:
            return None

    def make_coffee(self, cups, water, milk, coffee_beans, money):
        if self.ingredient_check(cups, water, milk, coffee_beans):
            print(f"Sorry, not enough {self.ingredient_check(cups, water, milk, coffee_beans)}!")
        else:
            print("I have enough resources, making you a coffee!")
            self.cups -= cups
            self.water -= water
            self.milk -= milk
            self.money += money
            self.coffee_beans -= coffee_beans

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        purchase = input()
        if purchase == "1":
            self.make_coffee(1, 250, 0, 16, 4)
        elif purchase == "2":
            self.make_coffee(1, 350, 75, 20, 7)
        elif purchase == "3":
            self.make_coffee(1, 200, 100, 12, 6)
        elif purchase == "back":
            return

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def remaining(self):
        print(f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money""")


my_coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
print("Write action (buy, fill, take, remaining, exit):")
action = input()
while action != "exit":
    if action == "buy":
        my_coffee_machine.buy()
    elif action == "fill":
        my_coffee_machine.fill()
    elif action == "take":
        my_coffee_machine.take()
    elif action == "remaining":
        my_coffee_machine.remaining()
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()

