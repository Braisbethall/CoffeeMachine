current_water = 400
current_milk = 540
current_coffee_beans = 120
current_cups = 9
current_money = 550


def print_stats(water, milk, coffee_beans, cups, money):
    print()
    print(f"""The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{cups} of disposable cups
${money} of money""")
    print()


def make_action(dealing):
    global current_coffee_beans, current_cups, current_milk, current_water, current_money
    while True:
        if dealing == "fill":
            print("Write how many ml of water you want to add:")
            water_supply = int(input())
            print("Write how many ml of milk you want to add:")
            milk_supply = int(input())
            print("Write how many grams of coffee beans you want to add:")
            coffee_beans_supply = int(input())
            print("Write how many disposable coffee cups you want to add:")
            cups_supply = int(input())
            current_water += water_supply
            current_milk += milk_supply
            current_coffee_beans += coffee_beans_supply
            current_cups += cups_supply
        elif dealing == "buy":
            espresso = [current_cups // 1, current_water // 250, current_coffee_beans // 16]
            latte = [current_cups // 1, current_water // 350, current_milk // 75, current_coffee_beans // 20]
            cappuccino = [current_cups // 1, current_water // 200, current_milk // 100, current_coffee_beans // 12]
            deficit_espresso = ""
            deficit_latte = ""
            deficit_cappuccino = ""
            if espresso[1] == 0:
                deficit_espresso = "water"
            elif espresso[2] == 0:
                deficit_espresso = "coffee beans"
            elif espresso[0] == 0:
                deficit_espresso = "cups"
            if latte[1] == 0:
                deficit_latte = "water"
            elif latte[2] == 0:
                deficit_latte = "milk"
            elif latte[3] == 0:
                deficit_latte = "coffee beans"
            elif latte[0] == 0:
                deficit_latte = "cups"
            if cappuccino[1] == 0:
                deficit_cappuccino = "water"
            elif cappuccino[2] == 0:
                deficit_cappuccino = "milk"
            elif cappuccino[3] == 0:
                deficit_cappuccino = "coffee beans"
            elif cappuccino[0] == 0:
                deficit_cappuccino = "cups"
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            coffee = input()
            if coffee == "1":
                if min(espresso) >= 1:
                    print("I have enough resources, making you a coffee!")
                    current_cups -= 1
                    current_water -= 250
                    current_money += 4
                    current_coffee_beans -= 16
                else:
                    print(f"Sorry, not enough {deficit_espresso}!")
            elif coffee == "2":
                if min(latte) >= 1:
                    print("I have enough resources, making you a coffee!")
                    current_cups -= 1
                    current_water -= 350
                    current_milk -= 75
                    current_money += 7
                    current_coffee_beans -= 20
                else:
                    print(f"Sorry, not enough {deficit_latte}!")
            elif coffee == "3":
                if min(cappuccino) >= 1:
                    print("I have enough resources, making you a coffee!")
                    current_cups -= 1
                    current_water -= 200
                    current_milk -= 100
                    current_money += 6
                    current_coffee_beans -= 12
                else:
                    print(f"Sorry, not enough {deficit_cappuccino}!")
            elif coffee == "back":
                print("Write action (buy, fill, take, remaining, exit):")
                dealing = input()
                continue
        elif dealing == "take":
            print(f"I gave you ${current_money}")
            current_money = 0
        elif dealing == "remaining":
            print_stats(current_water, current_milk, current_coffee_beans, current_cups, current_money)
        elif dealing == "exit":
            break
        print("Write action (buy, fill, take, remaining, exit):")
        dealing = input()


print("Write action (buy, fill, take, remaining, exit):")
action = input()
make_action(action)
