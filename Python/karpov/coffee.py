coffee *= 1000
milk *= 1000
visitors = 1

while True:
    if visitors % 3 == 0:
        if milk >= 100 and coffee >= 7:
            coffee -= 7
            milk -= 100
        else:
            break
    elif visitors % 5 == 0:
        if milk >= 180 and coffee >= 7:
            coffee -= 7
            milk -= 180
        else:
            break
    else:
        if coffee >= 7:
            coffee -= 7
        else:
            break
    visitors += 1
visitors -= 1