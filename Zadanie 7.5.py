def hideCard(cardNumber):
    if len(cardNumber) != 16:
        return "Invalid card number"

    return cardNumber[:2] + "*" * 10 + cardNumber[-4:]


cardNumber = "5290312400019022"
print(hideCard(cardNumber))

