import random 

choices = ["rock","paper","scissor"]
print(f"### ROCK, PAPER, SCISSOR GAME ###\nChoice = {choices}")
while True:
    
    choice = input("Enter your choice: ").lower()

    if choice == "Exit":
        print("Program finished!")
        break

    if choice not in choices:
        print("Invalid choices! please try again")
        pass
    computer = random.choice(choices)

    if choice == computer:
        print("Draw")
    elif (choice == "rock" and computer == "scissor")or\
    (choice == "scissor" and computer == "paper")or\
    (choice == "paper" and computer == "rock"):
        print("User wins")
        break
    else:
        print("Computer wins")
    print(f"User choice {choice} and computer choice{computer}")    


        

