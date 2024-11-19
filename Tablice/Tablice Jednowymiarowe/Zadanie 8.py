computer_games = [
   "Minecraft", "Fortnite", "Cyberpunk 2077", "The Witcher 3",
   "League of Legends", "Valorant", "Grand Theft Auto V", 
   "Elden Ring", "Apex Legends", "Call of Duty: Warzone"
]

number = len(computer_games)
computer_games.sort()
index = 0

while number > 0:
    print(index,computer_games[index])
    index += 1
    number -= 1