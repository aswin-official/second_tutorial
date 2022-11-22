names = []

for _ in range(3):
    name = input("Enter the  name ")
    names.append(name)

for name in sorted(names):
    print(f"hello, {name}")    