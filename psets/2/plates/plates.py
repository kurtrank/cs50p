def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # must start with two letters
    if s[0].isnumeric() and s[1].isnumeric():
        return False

    # must be between 2 and 6 characters
    if len(s) < 2 or len(s) > 7:
        return False

    # numbers must be at the end
    if find_number_problems(s):
        return False

    # no spaces or punctuation
    if any(map(lambda c: c in s, [" ", ".", "!", "?", ",", ";", ":"])):
        return False

    return True


def find_number_problems(s):
    in_numbers = False

    for c in s:
        if c.isnumeric():
            # check first number if equal to 0
            if not in_numbers and int(c) == 0:
                return True

            # set numbers state
            in_numbers = True

        # must not be any letters after numbers start
        if in_numbers and not c.isnumeric():
            return True

    return False


main()
