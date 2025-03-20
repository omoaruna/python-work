import random, sys, time
# import necessary modules
def spintheball(number):
    # this function takes a number and..
    if number == 1:
        return "It will happen soon."
    elif number == 2:
        return "It will never happen."
    elif number == 3:
        return "Make an attempt."
    elif number == 4:
        return "Don't make unnesessary journeys."
    elif number == 5:
        return "Don't worry too much."
    elif number == 6:
        return "You are weird and that's NOT okay."
    # ..returns a different response based on the number

while True:
    user_response = input("Do you want to know your fortune: 'y 'for yes and 'n' for no 'q' for exit ")  
    # prompt the user for a yes, no or quit response
    if user_response == 'q':
        sys.exit()  
        # immediately exit the program if user decides to quit
    elif user_response == 'y':
        print("Alright, the ball says...")
        # r = random.randint(1,6)
        # response = spintheball(r)
        time.sleep(1)
        print(spintheball(random.randint(1,6)))
        # using the random module and randint function, let the computer generate 
        # a random number between 1 and 6 and pass that as an argument in the 
        # spintheball() function.
    elif user_response == 'n':
        print("Alright, you'll be back")
        break
    # if the user responds no, break out of the while loop
    else: 
        print("Enter a valid response")
        # this runs when the user enters a response other than the ones mentioned
    
