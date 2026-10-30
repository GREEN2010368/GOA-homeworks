correct_password = "phyton123"

password = input("Enter your password: ")

while password != correct_password: 
    password = input("wrong password! try again: ")

print("Acsess Granted")