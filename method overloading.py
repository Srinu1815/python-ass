class Example:
    def method(self, a):
        print(f"Method with 1 parameter: {a}")

    def method(self, a, b=None):
        if b is not None:
            print(f"Method with 2 parameters: {a} and {b}")
        else:
            print(f"Method with 1 parameter: {a}")
example = Example()
example.method(10)
example.method(10, 20)


#2
class Example:
    def method(self, a, b=None):
        if b is None:
            if isinstance(a, int):
                print(f"Method with 1 integer parameter: {a}")
            elif isinstance(a, str):
                print(f"Method with 1 string parameter: {a}")
            else:
                print(f"Method with 1 parameter of unknown type: {a}")
        else:
            if isinstance(a, int) and isinstance(b, str):
                print(f"Method with 1 integer and 1 string: {a}, {b}")
            elif isinstance(a, str) and isinstance(b, int):
                print(f"Method with 1 string and 1 integer: {a}, {b}")
            else:
                print(f"Method with parameters of different types: {a}, {b}")
example.method(10)
example.method("Hello")
example.method(10, "world")
example.method("Hello", 20)





#3
class Example:
    def method(self, a):
        if 0 <= a <= 10:
            print(f"Method executed for a small number: {a}")
        elif 10 < a <= 20:
            print(f"Method executed for a medium number: {a}")
        else:
            print(f"Method executed for a large number: {a}")
example = Example()
example.method(5)  
example.method(15)
example.method(25) 
