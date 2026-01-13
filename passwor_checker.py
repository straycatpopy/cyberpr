password=input("Enter your password: ")
if len(password)<8:
    print("password must be 8 characters long")

elif not any(char.isdigit() for char in password):
    print("password must contain at least one digit")

elif not any(char.isupper() for char in password):
    print ("password must contain at least one uppercase letter")
elif not any(char.islower() for char in password):

    print("password must contain at least one lowercase letter")
elif not any(char in "!@#$%^&*()_" for char in password):
    print("password muct contain at one special character")
else:
    print("password is strong enough")
    