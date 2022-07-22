# gather input and break into pieces
x, y, z = input("Expression: ").strip().split(" ")

# convert to numbers
x = float(x)
z = float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)
    case _:
        print(f"Operation `{y}` not supported")
