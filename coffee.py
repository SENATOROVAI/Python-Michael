coffee = 0.1
milk = 1
ostatok_coffee =coffee * 1000 # в граммах
ostatok_milk = milk * 1000 # в мл
person = 0
# expresso = 7 kofe
# latte = 180 milk + expresso
# cap = 100 milk
# americano = expresso + water
while ostatok_milk >= 0 or ostatok_coffee >= 0:
    person += 1 
    if person % 3 == 0 and person % 5 == 0: #cap
        if ostatok_milk < 100:
            person -= 1
            break
        ostatok_milk -= 100
    elif person % 3 == 0:                   #cap
        if ostatok_milk < 100:
            break
        ostatok_milk -= 100
    elif person % 5 == 0:                   #latte
        if ostatok_milk < 180 or ostatok_coffee < 7:
            person -= 1
            break
        ostatok_milk -= 180
        ostatok_coffee -= 7
    else:
        if ostatok_coffee < 7:
            person -= 1
            break
        ostatok_coffee -= 7
    
visitors = person