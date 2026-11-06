for i in range(5):
    saxeli = input("შეიყვანეთ სტუდენტის სახელი: ")
    qula = int(input("შეიყვანეთ სტუდენტის ქულა: "))

    if qula >= 90:
        shedegi = "შესანიშნავი"
    elif qula >= 70:
        shedegi = "კარგი"
    elif qula >= 50:
        shedegi = "დამაკმაყოფილებელი"
    else:
        shedegi = "ჩაჭრილი"

    print(saxeli, "-", shedegi)