from libs.game import*

def main():
    difficulty = input("Choose the difficulty between 'easy', 'medium' and 'expert'. 'quit' if you want to quit the game. ")
    if difficulty == 'quit': return
    if difficulty not in ("easy", "medium", "expert"): 
        main()
        return

    Game(*Game.DIFFICULTY[difficulty])   
    
if __name__ == "__main__":
    main()
