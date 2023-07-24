# Now continue with the Animal class we had used before

# Add a method to count the legs count_legs which prints the number of legs

# Add a method to count the legs return_legs which returns the number of legs

# print number of legs directly from number_of_legs variable of the object

class animal:
    def __init__(self,name,it_runs,number_of_legs):
        self.name=name
        self.it_runs=it_runs
        self.number_of_legs=number_of_legs
        print("Animal object was created")
    def count_legs(self):
        print(f"the animal has {self.number_of_legs} legs")
    def runs(self):
        print("Running started")
    def return_legs(self):
        return f"The animal has {self.number_of_legs} legs"
    
cane=animal("dog",True,4)
print(cane.number_of_legs)