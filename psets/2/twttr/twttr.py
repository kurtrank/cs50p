s = input("Input: ")

print("Output: ", end="")

for c in s:
    print((c if c not in ["a", "e", "i", "o", "u", "A",
          "E", "I", "O", "U", ] else ""), end="")
