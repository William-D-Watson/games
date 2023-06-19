from Color import color
import random

c = color()

# Variables 
game_number = 0
wins = 0
ties = 0
Loses = 0
playing = True
while playing:
    # Game Info (Number and stats)
    game_number += 1
    print("\n")
    c.print_underline("New Game " + str(game_number))
    c.print_green("Wins: " + str(wins))
    c.print_yellow("Ties: " + str(ties))
    c.print_red("Losses: "+ str(Loses))
    print()

    result = "\n"
    # You pick rock paper or scissors
    Userpickednumber = 0
    while (Userpickednumber == 0):
        Userpickedword = input("Rock, paper, or scissors?: ").lower()
        # translate user input from words to numbers
        if (Userpickedword == "rock ✊"):
            Userpickednumber = 1
        if (Userpickedword == "paper 🖐️"):
            Userpickednumber = 2
        if (Userpickedword == "scissors ✌️"):
            Userpickednumber = 3
            # if you didnt put rock paper or scissors it will print not a valid input
        if (Userpickednumber == 0) :
            print("not a valid input")

    result += "You picked: " + Userpickedword + "\n"
        
    # Computer picks 1, 2, 3 and those correspond to rock paper or scissors
    computerpicked = random.randint(1, 3)
    result += "Computer picked: "
    if (computerpicked == 1):
        result += "rock ✊"
    if (computerpicked == 2):
        result += "paper 🖐️"
    if (computerpicked == 3):
        result += "scissors ✌️"

  # print results 
    print(result)

    # Games checks who picked what and assigns a winner
    if (Userpickednumber == computerpicked):
        c.print_yellow("You tied")
        ties += 1

    if (Userpickednumber == 1 and computerpicked == 2) or (Userpickednumber == 2 and computerpicked == 3) or (Userpickednumber == 3 and computerpicked == 1):
        c.print_red("The computer beat you loser")
        Loses += 1
    if (Userpickednumber == 1 and computerpicked == 3) or (Userpickednumber == 3 and computerpicked == 2) or (Userpickednumber == 2 and computerpicked == 1):
        c.print_green("You won")
        wins += 1

    print() # spacing

    # play again?
    valid_input = False
    while not valid_input:
        play_again = input("Play again? [y] yes  [n] no: ").lower()
        if (play_again == "y"):
            valid_input = True

        if (play_again == "n"):
            valid_input = True
            playing = False
            # prints final stats
            c.print_underline("\nFinal Scores:")
            c.print_green("Wins: " + str(wins))
            c.print_yellow("Ties: " + str(ties))
            c.print_red("Losses: "+ str(Loses))
            print()
        