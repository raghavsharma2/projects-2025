#inheritance
class animal:
    def speak():
        print("Animal speaks")
class dog(animal):
    def bark():
        print("Dog barks")
dog.speak()
dog.bark()
#multiple inheritance
class cat:
    def meow():
        print("Cat meows")
class kitten(dog,cat):
    def play():
        print("Kitten plays")
kitten.speak()
kitten.meow()
kitten.play()
class puppy(kitten):
    def cuddle():
        print("Puppy cuddles")
puppy.speak()
puppy.cuddle()
puppy.play()