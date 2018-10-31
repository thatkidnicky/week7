from random import randint

computerhealth = 3
playerhealth = 3
X = 0

# available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choices[randint(0, 2)]

# show the computer's choices in the terminal window
print("Computer chooses: ", computer)

while player is False:
    print("Choose your weapon!\n")
    player = input("Rock, Paper, Scissors?\n")
    print("Player chooses:", player)
    print("Player Health " + str(playerhealth))
    print("Computers Health " + str(computerhealth))

    if (player == computer):
        print("Computer chooses: ", computer)
        print("Tie! Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            print("Computer chooses: ", computer)
            print("You lose the round,", computer, "covers", player)
            playerhealth = playerhealth - 1
        else:
            print("Computer chooses: ", computer)
            print("You win the round,", player, "smashes", computer)
            computerhealth = computerhealth - 1

    elif player == "Paper":
        if computer == "Scissors":
            print("Computer chooses: ", computer)
            print("You lose the round,", computer, "cuts", player)
            playerhealth = playerhealth - 1

        else:
            print("Computer chooses: ", computer)
            print("You win the round,", player, "covers", computer)
            computerhealth = computerhealth - 1
         

    elif player == "Scissors":
        if computer == "Rock":
            print("Computer chooses: ", computer)
            print("You lose the round,", computer, "smashes", player)
            playerhealth = playerhealth - 1
           
        else:
            print("Computer chooses: ", computer)
            print("You win the round,", player, "cuts", computer)
            computerhealth = computerhealth - 1      

    elif player == "quit":
        exit()


    else:
        print("Not a valid option. Check again, and check your spelling!\n")

    player = False
    computer = choices[randint(0, 2)]

    if computerhealth is X:
        print("You Win!")
        player = input("Would you like to play again? y / n\n")
        computerhealth = computerhealth + 3
        playerhealth = computerhealth
        if player == "y":
            player = False
        if player == "n":
            break

    if playerhealth is X:
        print("You Lose!")
        player = input("Would you like to play again? y / n\n")
        playerhealth = playerhealth + 3
        computerhealth = playerhealth
        if player == "y":
            player = False
        if player == "n":
            break
