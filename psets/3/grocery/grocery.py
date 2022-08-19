list = {}


def main():
    while True:
        try:
            add_item_to_list()
        except EOFError:
            print_list()
            break


def print_list():
    print('\n')
    for item, quantity in sorted(list.items()):
        print(f"{quantity} {item.upper()}")


def add_item_to_list():
    name = input().lower()
    list[name] = list[name] + 1 if name in list else 1


main()
