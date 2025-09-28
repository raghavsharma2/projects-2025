from abc import ABC, abstractmethod
class shape(ABC):
    pass
class rectangle(shape):
        def __init__(self,width,height):
            self.width=width
            self.height=height
        def area(self):
            print(self.width*self.height)
rect=rectangle(5,7)
rect.area()