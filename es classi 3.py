class animal:
    def __init__(self,name,it_runs,number_of_legs):
        self.name=name
        self.it_runs=it_runs
        self.__number_of_legs=number_of_legs
        print("Animal object was created")
    def count_legs(self):
        print(f"the animal has {self.number_of_legs} legs")
    def runs(self):
        print("Running started")
    def return_legs(self):
        return f"The animal has {self.number_of_legs} legs"
    def private_legs(self):
        print(f"The animal has {self.__number_of_legs} legs")

cane=animal("dog",True,4)
cane.private_legs()