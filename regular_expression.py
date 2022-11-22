#validate email
#strip used for blank space removel
email = input("wahts your Email? ").strip()
 
if "@" in email and "." in email:
    print("valid")

else:
    print("invalid")     