#email = input("enter your email? ").strip()

# username, domain = email.split("@")

# if username and domain.endswith(".com"):
#     print("valid")

# else:
#     print("invalid")    

# re library
    
import re

email = input("whats your email address ?").strip()

if re.search(".+@.+", email):  # .+@.+ used for any content left and ring of the @ sigh we can recreate .+ to ..*
    print("valid")

else:
    print("invalid")     


