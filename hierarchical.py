class A:
    def method_A(self):
        print("it is class a")
class B(A):
    def method_B(self):
        print("it is class b")
class C(A):
    def method_C(self):
        print("it is class c")
class D(B,C):
    def method_D(self):
        print("it is class d")
d=D()
d.method_A()
d.method_B()
d.method_C()
d.method_D()
class E:
    def method_E(self):
        print("it is class e")
class F(E):
    def method_F(self):
        print("it is class f")
f=F()
f.method_E()
f.method_F()