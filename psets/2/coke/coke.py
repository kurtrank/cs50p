due = 50

while due > 0:
    coin = int(input("Insert Coin: "))
    due = (due - coin) if coin in [5, 10, 25] else due

    if due > 0:
        print("Amount Owed: ", due)
    else:
        print("Change Owed: ", due * -1)
