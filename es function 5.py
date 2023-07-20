# Import random function
# Create a function random_list_summer creates n elemented list
#  with min value = -100 max value = 100 
# it has to print the list first and sum all the elements of it default element number is 15
# Don't forget to call the function
# for some features and functions you might have to search on the internet do it don't lose your courage


import random
def random_list_summer(n):
    list=[random.randint(-100,100) for _ in range (n)]
    print(list)
    print(f"The sum of the list is {sum(list)}")

random_list_summer(15)