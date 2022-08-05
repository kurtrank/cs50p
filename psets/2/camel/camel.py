s = input("camelCase: ")

print("snake_case: ", end="")

for c in s:
    print("_" + c.lower() if c.isupper() else c, end="")
