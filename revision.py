class animal:
    def speak(self):
        print("Animal speaks")
class dog(animal):
    def bark(self):
        print("Dog barks")
d = dog()
d.speak()
d.bark()
