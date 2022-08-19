months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    date = False

    while date == False:
        date = get_date()

    print(date)


def get_date():
    i = input("Date: ").strip().split("/")

    if len(i) == 3:
        m, d, y = i

        if not m.isnumeric():
            return False
    else:
        try:
            md, y = i[0].split(", ")
            m, d = md.split(" ")
        except:
            return False

    if (verify_date(d, m, y)):
        return f"{int(y)}-{int(get_month(m)):02}-{int(d):02}"
    else:
        return False


def verify_date(d, m, y):
    if not d.isnumeric() or int(d) > 31:
        return False
    if not get_month(m):
        return False

    return True


def get_month(m):
    return months.index(m) + 1 if not m.isnumeric() and m in months else m if m.isnumeric() and int(m) < 13 else False


main()
