greeting = input("Greeting: ").strip().lower()

pay = 100

if greeting.startswith('hello'):
    pay = 0
elif greeting.startswith('h'):
    pay = 20

print(f"${pay}")
