# try:
#     x = int(input("enter an integer :"))
#     #value error
# except:
#     print(" x is not an integer") 
#    #name error
# else:
#     print(f"entered value x is {x} ")   

while True:
    try:
        x = int(input("enter an integer :"))
    except:
        print("x is not an integer")
    else:
        break
print(f"{x} is an integer")        

        

    