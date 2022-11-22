# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,",line.rstrip())#we can also use 'end="" '  
# 
# improved
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.strip())  

names = []

with open("names.csv") as file:
   for line in file:
      names.append(line. rstrip()) 


for name in sorted( names): #sorted
   print(f"hello, {name}")
   #convert name.txt ito name.csv to add houses