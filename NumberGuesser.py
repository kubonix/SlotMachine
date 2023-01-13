import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number next time.")
    quit()

print("Now guess the number between 0 and", top_of_range)

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess > top_of_range:
            print("Please type a number between 0 and ", top_of_range)
            continue
    else:
        print("Please type a number next time.")
        continue
    #guesses += 1

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You are abowe the number!")
    else:
        print("You are below the number!")

    # Inny sposób na uzyskanie tego samego efektu
    # if+else(if+else) --> wersja z elif jest bardziej przejrzysta :)
    #if user_guess == random_number:
    #    print("You got it!")
    #    break
    #else:  
    #   if user_guess > random_number:
    #        print("You are abowe the number!")
    #    else:
    #        print("You are below the number!")            
     
print(random_number)
print("You got it in", guesses, "guesses.")