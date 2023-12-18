coffee = 1
milk = 2
ostatok_coffee = coffee * 1000  # в граммах
ostatok_milk = milk * 1000  # в мл
person = 1
# expresso = 7 kofe
# latte = 180 milk + expresso
# cap = 100 milk
# americano = expresso + water
while ostatok_milk >= 0 or ostatok_coffee >= 0:
    if person % 3 == 0 and person % 5 == 0:  # cap
        if ostatok_milk < 100:
            break
        else:
            ostatok_milk -= 100
    elif person % 3 == 0:  # cap
        if ostatok_milk < 100 and ostatok_coffee < 7:
            break
        else:
            ostatok_milk -= 100
            ostatok_coffee -= 7
    elif person % 5 == 0:  # latte
        if ostatok_milk < 180 and ostatok_coffee < 7:
            break
        else:
            ostatok_milk -= 180
            ostatok_coffee -= 7
    else:
        if ostatok_coffee < 7:
            break
        else:
            ostatok_coffee -= 7
    person += 1
visitors = person - 1
print(visitors)
