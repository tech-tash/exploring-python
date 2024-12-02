import random

def play_game():
    options = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors.")
    print("Choose 'rock', 'paper' or 'scissors' to play.")
    print("Type 'exit' to quit the game.")
     
    
    while True:
        pick = input("Make your pick: ")
        
        if pick not in options:
            print("Pick 'rock', 'paper' or 'scissors'.")
            continue
        
        if pick == 'exit':
            print("Thank you for playing.")
            break
        
        random_pick = random.choice(options)
        
        print("Computer chose: {}".format(random_pick))
        
        if pick == random_pick:
            print("It's a tie!")
            
        elif (pick == "rock" and random_pick == "scissors") or (pick == "paper" and random_pick == "rock") or (pick == "scissors" and random_pick == "paper"):
            print("You win!")
            
        else:
            print("You lose!")
            
            
play_game()           