import random

while True:

    print('''
    Welcome to the game
    Let's play Rock, Paper and Scissors!
    ''')

    position = input('''
    R for Rock,
    P for paper,
    S for Scissors.
    Choose your position: 
    ''')
    print("\tMay the force be with you..")

    while position != "R" and position != "P" and position != "S":
        position = input("enter valid input: ")

    if position.lower == "r":
        name = "Rock"
    elif position.lower == "p":
        name = "Paper"
    else: 
        name = "Scissors"

    print("\tYour choice is: " + name)
    print("\n\tits time for the computer to pick..")
    game_list = ["r", "p", "s"]
    com = random.choice(game_list) 
    if com == "r":
        com_choice = "Rock" 
    elif com == "p":
        com_choice = "Paper" 
    else:
        com_choice = "Scissors" 

    print("\tThe computer chose "+ com_choice)
    print("\n\tPlayer (" + name + ")" + ": CPU (" + com_choice + ") " )

    if ((name == "Rock" and com_choice =="Scissors") or (name == "Paper" and com_choice =="Rock") or (name == "Scissors" and com_choice=="Paper")):
        print("You Win")
        winner = "you"
    elif ((name =="Scissors" and com_choice =="Rock") or (name == "Rock" and com_choice =="Paper") or (name == "Paper" and com_choice=="Scissors")):
        print("\tComputer Wins... You Lose")
        winner = "com"
    else:
        print("It's a Draw")
        winner = "draw"

    if winner != "draw":
        break


    
    