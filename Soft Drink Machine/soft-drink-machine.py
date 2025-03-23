def check_valid_money(user_money, accepted_currencies):
    """
    Checks if all the money provided by the user is in the list of accepted currencies.

    Args:
        user_money (list of int): The amounts of money provided by the user.
        accepted_currencies (set of int): The set of accepted currency denominations.

    Returns:
        bool: True if all user money is valid, otherwise False.
    """
    for money in user_money:
        if money not in accepted_currencies:
            return False
    return True

def play_soft_drink_menu(user_money, soft_drink_price):
    drinks ={
        1: "Coke",
        2: "Pepsi",
        3: "Sprite",
        4: "Fanta",
        5: "Mirinda"
    }
    user_selected_drinks = []

    if user_money < soft_drink_price:
        print("You don't have enough money to buy a soft drink.")
        print("This is your balance kshs.{} .".format(user_money))
    
    while user_money >= soft_drink_price:
        print("--------------------------------------------------------------------")
        for k, v in drinks.items():
            print(f"{k}: {v}")
        user_drink = input("Please select a drink from the menu: ")

        try:
            user_drink = int(user_drink)
        except ValueError:
            print("You have selected an invalid option.")
            print("Please try again.")
            continue
        

        if user_drink not in drinks.keys():
            print("You have selected an invalid option.")
            print("Please try again.")
            continue

        user_selected_drinks.append(drinks[user_drink])
        user_money -= soft_drink_price
        # print("You have selected {} for kshs.{}.".format(drinks[user_drink], soft_drink_price))
        # print("This is your balance kshs.{} .".format(user_money))
        # print("--------------------------------------------------------------------")
        print("--------------------------------------------------------------------")
        print("Do you wish to continue?")
        user_choice = input("Enter 'y' for yes and 'n' for no: ")
        while user_choice != "y" and user_choice != "n":
            print("You have entered an invalid option.")
            print("Please try again.")
            user_choice = input("Enter 'y' for yes and 'n' for no: ")
        if user_choice == "n":
            break
        else:
            if user_money < soft_drink_price:
                print("Money left is not enough to buy a soft drink.")
                break
            else:
                continue
    
    print("--------------------------------------------------------------------")
    print("These are the drinks you have selected: ")
    for drink in user_selected_drinks:
        print(drink)

    print("This is your balance kshs.{}/= ".format(user_money))
        
def main():
    accepted_currencies = {10, 20, 40, 50, 100, 200, 500, 1000}
    soft_drink_price = 50


    print("********************Welcome to the Soft Drink Machine********************")
    user_money = input("Please enter the amount of money you have seperated by spaces: ")
    user_money = list(map(int, user_money.split()))

    while not check_valid_money(user_money, accepted_currencies):
        print("The money you provided is not valid.")
        user_money = input("Please enter the amount of money you have seperated by spaces: ")
        user_money = list(map(int, user_money.split()))

    user_money = sum(user_money)

    play_soft_drink_menu(user_money, soft_drink_price)

    print("********************Thank you for using the Soft Drink Machine********************")



if __name__ == "__main__":
    main()