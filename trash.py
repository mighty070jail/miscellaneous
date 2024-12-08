def max(x,y,z):
    '''function to find the maximum of three numbers.'''
    if (x>y) & (x>z):
        return x
    elif (x<y) & (y>z):
        return y
    elif (z>x) & (z>y):
        return z
num_1= int(input("Enter the first number: "))
num_2= int(input("Enter the second number: "))
num_3= int(input("Enter the third number: "))
print(max(num_1,num_2,num_3))
def sum_of_list(numbers):
    ''' function to sum all the numbers in a list.'''
    sum = 0
    for i in numbers:
        sum += i
        return sum
    print(sum)
print(f"sum= {sum((2,3,4,5))}")





----------------------------------------

