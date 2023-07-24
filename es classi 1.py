# Let's create Animal class and then create the animal object that runs and having 4 legs

# create animal object with leg count when created print "Animal object was created" 
# and then call runs method of it and it prints "Running started"

class animal:
    def __init__(self,name,it_runs,number_of_legs):
        self.name=name
        self.it_runs=it_runs
        self.number_of_legs=number_of_legs
        print("Animal object was created")
    def leg_count(self):
        print(f"the animal has {self.number_of_legs} legs")
    def runs(self):
        print("Running started")

cane=animal("dog",True,4)
cane.runs()
cane.leg_count()