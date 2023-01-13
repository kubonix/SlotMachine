print('Welcome to my Quiz!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':    #.lower sprawia że wszystkie symbole w stringu są zmniejszone do małej litery
    quit()                      #nawet przy funkcji input() gdy w konsoli wpisze się duże litery
print("OK! Let's play") 

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')    

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')    

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')            

if score == 0:
    print("All questions incorrect! You need to learn more!")
elif score == 1:
    print("You got " + str(score) + " question correct!")
else:    
    print("You got " + str(score) + " questions correct!")    

print("You got " + str((score / 3) * 100) + "%")