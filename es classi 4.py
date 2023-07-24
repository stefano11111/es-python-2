class animal:
    def __init__(self,it_runs,number_of_legs):
        self.it_runs=it_runs
        self.__number_of_legs=number_of_legs
        print("Animal object was created")
    def runs(self):
        print("Running started")
    def private_legs(self):
        print(f"The animal has {self.__number_of_legs} legs")

class dog(animal):
    def __init__(self,it_runs,number_of_legs,name):
        super().__init__(it_runs,number_of_legs)
        self.__name=name
    def tell_name(self):
        print(f"My name is {self.__name}")
    def bark(self):
        print("woof woof")

new_dog=dog(True,4,"rex")
new_dog.tell_name()
new_dog.bark()
new_dog.private_legs()
