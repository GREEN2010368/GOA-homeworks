sul = 0
raodenoba = 0
dadebiti = 0

ricxvi = int(input("შეიყვანეთ რიცხვი (0-ის შესაყვანად დასრულდება): "))

while ricxvi != 0:

    if ricxvi > 0:
        print("რიცხვი დადებითია")
        dadebiti += 1
    else:
        print("რიცხვი უარყოფითია")

    if ricxvi % 2 == 0:
        print("რიცხვი ლუწია")
    else:
        print("რიცხვი კენტია")

    sul += ricxvi
    raodenoba += 1

    ricxvi = int(input("შეიყვანეთ შემდეგი რიცხვი: "))

print("რიცხვების ჯამი:", sul)
print("რიცხვების რაოდენობა:", raodenoba)
print("დადებითი რიცხვების რაოდენობა:", dadebiti)