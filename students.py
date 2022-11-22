# with open("students.csv") as file:
#     for line in file:
#         name, house= line.rstrip().split(",")
#         # row = line.rstrip().split(",")
#         print(f"{name} is in {house}") #no need for row[0] is in row[1]
####sorted students
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)         