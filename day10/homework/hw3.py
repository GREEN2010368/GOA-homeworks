secret = 42
count = 0

guess = int(input("გამოიცანით საიდუმლო რიცხვი: "))

while guess != secret:
    count += 1

    if guss > secret:
        print("შეყვანილი რიცხვი მეტია საიდუმლო რიცხვზე!")
    else:
        print("შეყვანილი რიცხვი ნაკლებია საიდუმლო რიცხვზე!")

    guess = int(input("სცადეთ თავიდან: "))

count += 1

print("გილოცავთ! თქვენ გამოიცანით რიცხვი!")
print("მცდელობების რაოდენობა:", count)