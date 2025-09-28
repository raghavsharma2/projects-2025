class Bird:
    def fly(self):
        print("Bird can fly")
class Airplane:
    def fly(self):
        print("Airplane can fly")
def lets_fly(flying_object):
    flying_object.fly()
Bird = Bird()
plane = Airplane()
lets_fly(Bird)
lets_fly(plane)
