import random

print("\nWelcome to the <<< Rock x Paper x Scissors >>> game!\nPlay versus the Computer up to 3 wins!\n")



options = ["rock", "paper", "scissors"]

def main():
    user_wins = 0
    computer_wins = 0
    draws = 0
    while True:
        user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if user_input == 'q':
            print("Ok BYE")
            #break
            quit()
        if user_input not in options:
            print("Wrong type, try again.")
            continue


        random_number = random.randint(0, 2)
        # rock: 0, paper: 1, scissors: 2
        computer_pick = options[random_number]
        print("Computer picked", computer_pick + ".")

        if user_input == "rock" and computer_pick == "scissors":
            print("You won!")
            user_wins += 1
            #print(f"You: {user_wins} : {computer_wins} Computer")
        elif user_input == "paper" and computer_pick == "rock":
            print("You won!")
            user_wins += 1
        elif user_input == "scissors" and computer_pick == "paper":
            print("You won!")
            user_wins += 1
        elif user_input == computer_pick:
            print("Draw!")    
            draws += 1
        else:
            print("You lost!")
            computer_wins += 1  

        print(f"You {user_wins} : {computer_wins} Computer")          

        if computer_wins >= 3 or user_wins >= 3:
            print("----------------------------")
            print(f"You won             {user_wins} times.")
            print(f"The computer won    {computer_wins} times.")
            print(f"Draws               {draws} times.\n")

            if user_wins > computer_wins:
                print("You are better than the computer!")
            elif user_wins < computer_wins:
                print("AI defeted You!")    
            else:
                print("Draw game!") 
            break    
        else:
            continue             

main()


# JAK SPRAWIC ABY GRA SIĘ URUCHAMIAŁA OD NOWA????? --> DOKOŃCZYĆ !!!!!
if input("Wanna play again (Y/N) ? ").lower() == "y":
    print("OK! Next round!")
    main()
else:
    print("Thanks for the game!\n")