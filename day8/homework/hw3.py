correct_password="python123"
password=input("please enter your password")
while password!=correct_password:
    print("incorrect")
    password=input("please enter your password")
    if  password==correct_password:
        print("welcome")