menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    total = 0

    while True:
        try:
            total += get_menu_item_price()
            print(f"${total:.2f}")
        except EOFError:
            break


def get_menu_item_price():
    name = input("Item: ").title()
    return menu[name] if name in menu else 0


main()
