n=int(input("please enter n: "))
pirveli=n
bolo=n%10
while pirveli>=10:
    pirveli=n//10
if pirveli==bolo:
    print("equal")
else:
    print("not_equal")