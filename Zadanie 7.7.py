def coins(money):
    ammount_of_coins = 0
    if money // 5 > 0:
        ammount_of_coins += money // 5
        money -= (money // 5 * 5)
    if money // 2 > 0:
        ammount_of_coins += money // 2
        money -= (money // 2 * 2)
    ammount_of_coins += money

    return ammount_of_coins

money = int(input("Type how much money something cost: "))
print(coins(money))

