'''
Write a program to play a sticks game in which there are 16 sticks.
Two players take turns to play the game.
Each player picks one set of sticks (needn’t be adjacent) during his turn.
A set contains 1, 2, or 3 sticks.
The player who takes the last stick is the loser.
The number of sticks in the set is to be input.
'''
player1=input("Enter Name of Player-1:")
player2=input("Enter Name of Player-2:")
count=0
number_of_sticks=16
while number_of_sticks!=0:
    if number_of_sticks!=0:
        print(f"{player1}'s Turn")
        sticks_taken = int(input("Number of sticks to be taken?"))
        count+=1
        number_of_sticks = number_of_sticks - sticks_taken
    if number_of_sticks!=0:
        print(f"{player2}'s Turn")
        sticks_taken = int(input("Number of sticks to be taken?"))
        count+=1
        number_of_sticks = number_of_sticks - sticks_taken
    if number_of_sticks==0:
        if count%2==0:
            print(f"{player2} Wins!")
        else:
            print(f"{player1} Wins!")
