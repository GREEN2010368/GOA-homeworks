correct_username="gio"
correct_password="12345"

username=input("please enter your user name: ")
password=int(input("please enter your password: "))

if username==correct_username and password==correct_password:
    print("login successful!")
elif username!=correct_username and password!=correct_password:
    print("wrong username or password")