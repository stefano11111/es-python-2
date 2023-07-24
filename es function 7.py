# Create a lambda function that returns 2nd power of given number if its even
# and run it on the given list
# then print the result to the screen

my_list= [*range(5)] 
power=lambda x:x**2 if x%2==0 else ("is not even") 
z=[power(y) for y in my_list]
print(z)