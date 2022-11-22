name = input("whats your name? ")

file = open("names.txt", "a")#append "a" "w" for write
file.write(f"{name}\n")
file.close()