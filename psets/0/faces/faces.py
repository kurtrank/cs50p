def main():
    print(convert(input("How are you feeling? ")))


def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")


main()
