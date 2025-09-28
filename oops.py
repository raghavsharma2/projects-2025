class car:
    def __init__(self, brand, color, model):
        self.brand = brand
        self.color = color
        self.model = model
    def display(self):
        print("the brand is:", self.brand, "the color is:", self.color, "the model is:", self.model)
s1 = car("bmw", "black", 2020)
s2 = car("thar","red",2020)
s1.display()
s2.display()
class employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print("the name is:", self.name,"", "the age is:", self.age, "the salary is:", self.salary)
        