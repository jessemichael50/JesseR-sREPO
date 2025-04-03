def main( ):
    difficulty = input("Difficul or casual?")
    players = input("Multiplayer or singleplayer?")
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("League of Legends")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Minecraft")
    elif difficulty == "Difficult" and players == "Singleplayer":
        recommend("Dark Souls")
    elif difficulty == "Casual" and players == "Singleplayer":
        recommend("Stardew Valley")
    else:
        print("I'm sorry, I don't have a recommendation for you.")



def recommend(game):
    print("I recommend playing", game)



main( )