import random
while True:
    options=['rock','paper','scissors']
    choice=(input("Your Options are Rock, Paper or Scissors\n[Type 'exit' to Quit]\nChoose!!:"))
    choice=choice.lower()
    if choice=="exit":
        break
    selection=random.choice(options)
    print("The Computer chooses",selection)
    if choice=='scissors' and selection=='paper':
        print("You Win!!") 
    elif choice=='paper' and selection=='rock':
        print("You Win!!")
    elif choice=='rock' and selection=='scissors':
        print("You Win!!")
    elif selection==choice:
        print("It's a Tie!")
    else:
        print("You Lose :(")    
