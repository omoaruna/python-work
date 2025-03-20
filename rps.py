import random, sys, time
# Import necessary modules
moves = {
    "r" : "ROCK",
    "p" : "PAPER",
    "s" : "SCISSORS",
}
# Store possible moves in a dictionary so each move can be easily identified using it's key
computer_moves = {
    1 : "ROCK",
    2 : "PAPER",
    3 : "SCISSORS",
}
# Use numbers to represent computer moves to avoid mistakes
wins = 0
losses = 0
ties = 0
# Initialize counters for wins, losses and ties

while True:
    # main loop
    print(f"{wins} wins, {losses} losses, {ties} ties")
    user_response = input("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit: ")
    # continue to prompt user for a response till they decide to quit.

    # BLOCK FOR WHEN USER ENTERS ROCK
    if user_response == "r":
        print(f"{moves['r']} vs...")
        # display user's reponse 
        computer_response = computer_moves[random.randint(1,3)]
        # create a variable that stores the computer's response.
        # The computer's response is gotten from the computer_moves dictionary above
        # It takes a random number between 1 and 3, which correspond to the dictionary keys
        time.sleep(1)
        print(computer_response)
        # display computer's response

        # Evaluate all possible outcomes 
        if computer_response == "ROCK":
            print("It's a tie")
            ties += 1
        elif computer_response == "SCISSORS":
            print("You win!")
            wins += 1
        else: 
            print("You lose!")
            losses += 1

    # BLOCK WHEN USER ENTERS PAPER

    elif user_response == "p":
        print(f"{moves['p']} vs...")
        computer_response = computer_moves[random.randint(1,3)]
        time.sleep(1)
        print(computer_response)
        if computer_response == "ROCK":
            print("You win!")
            wins += 1
        elif computer_response == "SCISSORS":
            print("You lose!")
            losses += 1
        else: 
            print("It's a tie!")
            ties += 1

    # BLOCK FOR WHEN USER ENTERS SCISSORS
    elif user_response == "s":
        print(f"{moves['s']} vs...")
        computer_response = computer_moves[random.randint(1,3)]
        time.sleep(1)
        print(computer_response)
        if computer_response == "ROCK":
            print("You lose!")
            losses += 1
        elif computer_response == "SCISSORS":
            print("It's a tie!")
            ties += 1
        else: 
            print("You win!")
            wins += 1

    # BLOCK FOR WHEN USER WANTS TO QUIT
    # If the user selects 'q', prompt them to confirm if they want to stop playing
    # if yes, then exit
    # if no, the while loop starts from the beginning
    elif user_response == "q":
        check = input("Are you sure you want to quit? y/n  ")
        if check == "n":
            continue
        else: 
            sys.exit()
    # This checks for invalid moves from the user
    else: 
        print("Please enter a valid response.")    
