user_number=int(input("please enter your number: "))
if user_number > 0 and user_number % 2 == 0:
    print("positive number")
elif user_number > 0 and user_number % 2 != 0:
    print("positive even")
elif user_number < 0:
    print("negative number")
else:
    print("zero")