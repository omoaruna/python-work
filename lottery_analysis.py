# LOTTERY ANALYSIS
# FIRST PULL THE 4 WINNING NUMBERS FROM A SERIES OF POSSIBILITIES
import random,time
def pull_ticket(possiblities):
    ticket = []

    while len(ticket) < 4:
        pulled_ticket = random.choice(possiblities)
        if pulled_ticket not in ticket:
            ticket.append(pulled_ticket)
    return ticket

#DUPLICATE
# def pull_random_ticket(possibilities):
#     random_ticket = []
#     while len(random_ticket) < 4:
#         pulled_ticket = random.choice(possibilities)
#         if pulled_ticket not in random_ticket:
#             random_ticket.append(pulled_ticket)
#     return random_ticket  
#DUPLICATE
 
# This is to compare the values and return true if the tickets are equal
def check_tickets(winning_ticket,random_ticket):
    if all(x in random_ticket for x in winning_ticket) and len(random_ticket) == 4:
        #you could also use if sorted(winning_ticket) == sorted(random_ticket)
        return True
    else:
        return False
   
possibilities = ["a","b","c","d","e","f","g","h","i",1,2,3,4,5]
winning_ticket = pull_ticket(possibilities)
print("This is a secret, the winning ticket is: ")
print(winning_ticket)
count = 0   

while True:
    print("Let's play")
    your_ticket = pull_ticket(possibilities)
    count += 1
    print("Moment of truth...")
    # time.sleep(1.3) this was just for suspense
    result = check_tickets(winning_ticket,your_ticket)
    if result == True:
        print("And we have a winner!")
        print(f"Congrats, you got it in {count} tries.")
        print(f"Your ticket, {your_ticket} is the winner")
        break
    else:
        print("Better luck next time")
        # response = input("Do you want to try again (y/n)")
        # if response == "n":
        #     break