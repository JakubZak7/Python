#The playing cards have the following values: Ace (A), King (K), Queen (Q), Jack (J) and 10 (T) have a value of 10 each.
# The other cards have the value indicated by the card number.
# Define a function f(player1,player2) that returns true if the first player has cards of the same or higher value, and false otherwise. Example:

def f(player1,player2):
    player1summary = 0
    player2summary = 0

    for char in player1:
        if char == "A" or char == "K" or char == "Q" or char == "J" or char == "T":
            player1summary += 10
        else:
            player1summary += int(char)

    for char in player2:
        if char == "A" or char == "K" or char == "Q" or char == "J" or char == "T":
            player2summary += 10
        else:
            player2summary += int(char)

    if player1summary >= player2summary:
        return True
    else:
        return False



if __name__ == '__main__':
    print(f("AJ972","AQT72"))
    print(f("9532","K8"))
