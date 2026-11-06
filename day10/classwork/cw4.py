n=int(input("შეიყვანეთ დადებით მთელი რიცსვი"))
ჯამი=0
while n>0:
    number=n%10
if number % 2==1:
    ჯამი+=number
n//=10
print(ჯამი)