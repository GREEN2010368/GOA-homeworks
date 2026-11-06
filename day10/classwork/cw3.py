first=int(input("please enter your first number"))
second=int(input("please enter your second number"))

while second!=0:
    first,second=second,first%second
print("უდიდესი საერთო გამყოფია",first)