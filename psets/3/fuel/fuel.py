def main():
    p = get_percentage()
    print(format_fuel(p))


def get_percentage():
    while True:
        frac = input("Fraction: ").split('/')
        try:
            x = int(frac[0])
            y = int(frac[1])
            p = round(x / y * 100)
        except:
            pass
        else:
            if p <= 100:
                return p


def format_fuel(p):
    return "E" if p <= 1 else "F" if p >= 99 else f"{p}%"


main()
