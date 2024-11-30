'''
Author: Joshil S Abraham
Date: 30/11/2024
Description: Inputing numbers to a list
'''
list = []
def menu():
    print("1. Add value to List")
    print("2. Print List")
    print("3. Exit")
    choice= int(input("Choice?:"))
    while True:
        if choice==1:
            value= int(input("Add value to list"))
            list.append(value)
            menu()
        elif choice==2:
            print(list)
            menu()
        elif choice==3:
            exit()
menu()
