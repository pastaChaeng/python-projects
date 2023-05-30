from tkinter.messagebox import YES


print("Welcome to py mini quiz!")

playing = input("Do you wanna play? ")

if playing.lower() != "yes":
    quit()

print("Brilliant! Let's get started! ps. type your answer in lowercase :)")
score = 0

answer = input("Is python a snake? ")
if answer.lower() == "no":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the extension for python? ")
if answer.lower() == ".py":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Who created python? ")
if answer.lower() == "guido van rossum":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Is python, a programming language? ")
if answer.lower() == "yes":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("Was python's name, inspired by a snake? ")
if answer.lower() == "no":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Your score is " + str(score) + " = " + str((score / 5) * 100) + "%." )