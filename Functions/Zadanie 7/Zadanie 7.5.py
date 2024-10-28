def hide_card(cardNumber):
    for i in range(2,len(cardNumber)-4):
        cardNumber[i] += "*"


cardNumber = "5290312400019022"
hide_card(cardNumber)

print(cardNumber)