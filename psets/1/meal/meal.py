def main():
    time = convert(input("What time is it? ").strip())

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    h, m = time.split(":")

    # convert `#:##` string into hours float
    return float(h) + (float(m) / 60)


if __name__ == "__main__":
    main()
