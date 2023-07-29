# Again let's keep talking on Animal class we have.
# with 3 methods we just reached the number of legs
# to prevent direct interacting with the class variables
# most of the other programming languages have encapsulation.
# But in python we don't have it instead we use _ prefix for it as convention
# it is also same for the methods

# _legs this shows us not to touch this variable its up to you if you want to change it you can but _ asks you politely not to do it.

# Change the number_of_legs to conventional private variable and call from another method
class animal:
    def __init__(self,name,it_runs,number_of_legs):
        self.name=name
        self.it_runs=it_runs
        self._number_of_legs=number_of_legs
        print("Animal object was created")
    def count_legs(self):
        print(f"the animal has {self._number_of_legs} legs")
    def runs(self):
        print("Running started")
    def return_legs(self):
        return f"The animal has {self._number_of_legs} legs"
    def private_legs(self):
        print(f"The animal has {self._number_of_legs} legs")

cane=animal("dog",True,4)
cane.private_legs()