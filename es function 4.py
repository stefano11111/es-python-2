# Now create a function for John Doe and his family that greets every one in the family.
# Since it will usually John Doe the name and surname parameter must be defaulted
# and when someone else comes it has to greet the new comer with name surname parameters which were overwritten. Make it possible.
# The function have to print "Hello John Doe" where John and Doe is parametric
# Greet each our John first then the people in the list with for loop and the function
# What you have to use

# for loop
# function
# string operation
# list index
# Output format

# Hello John Doe!
# Hello Tristram Mcbride!
# Hello Baldwin Preston!
# Hello Wally Collins!
members=["Tristram Mcbride","john Doe","Baldwin Preston","Wally Collins"]
lista=[]
for x in members:
    lista.append(x.split())
print(lista)

def saluta(name="john", surname="Doe"):
    print(f"Hello {name} {surname}")
    for name,surname in lista:
        if name!="john":
            print(f"Hello {name} {surname}")

saluta()