from recipies import MENU
from machineResources import resources


def emit_report():
    """Print a formatted report of the resources in the machine at the current moment"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    if resources["money"] > 0:
        print(f"Money: ${resources["money"]}")


def verify_resources(ingredients):
    """Receive a list of ingredients and return False if there isn't sufficient to make the order"""
    missing_resource = []
    if ingredients.get("water") is not None:
        if resources["water"] < ingredients["water"]:
            missing_resource.append("water")
    if ingredients.get("milk") is not None:
        if resources["milk"] < ingredients["milk"]:
            missing_resource.append("milk")
    if ingredients.get("coffee") is not None:
        if resources["coffee"] < ingredients["coffee"]:
            missing_resource.append("coffee")

    if len(missing_resource) > 0:
        sep = " and "
        print(f"Sorry there is not enough {sep.join(missing_resource)}.")
        return False
    return True


def receive_money():
    """Get the input from user, calculate and return total value informed"""
    received_money = int(input("how many quarters?: ")) * 0.25
    received_money += int(input("how many dimes?: ")) * 0.1
    received_money += int(input("how many nickles?: ")) * 0.05
    received_money += int(input("how many pennies?: ")) * 0.01
    return received_money


def validate_payment(total_value, cost):
    """Verify if the total value inputted by user is enough
    to pay the cost of the product and return True if it is"""
    if total_value < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    if total_value > cost:
        print(f"Here is ${total_value - cost:.2f} dollars in change.")

    return True


def get_payment(cost):
    """Verify all processes of payment and return if its valid (True)"""
    total_value = receive_money()
    return validate_payment(total_value, cost)


def update_resources(product):
    """Remove resources from machine and add the money paid"""
    if product["ingredients"].get("water") is not None:
        resources["water"] -= product["ingredients"]["water"]
    if product["ingredients"].get("milk") is not None:
        resources["milk"] -= product["ingredients"]["milk"]
    if product["ingredients"].get("coffee") is not None:
        resources["coffee"] -= product["ingredients"]["coffee"]

    resources["money"] += product["cost"]


def make_a_coffee(product, description):
    """Make all steps to make a coffee"""
    valid = verify_resources(product["ingredients"])

    if valid:
        valid = get_payment(product["cost"])

    if valid:
        update_resources(product)
        print(f"Here is your {description} ☕.Enjoy!")


def machine_on():
    """Process running while the machine is on"""
    options = ["espresso", "latte", "cappuccino"]
    while 1 == 1:

        choice = input("What would you like? (espresso/latte/cappuccino): ")

        match choice:
            case "off":
                return
            case "report":
                emit_report()
            case _:
                if choice in options:
                    make_a_coffee(MENU[choice], choice)
                else:
                    print("Invalid command. Please try again.")


machine_on()
print("Good bye!")
