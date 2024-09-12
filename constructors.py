class ExampleClass:
    # Default constructor
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default constructor called")
        elif arg2 is None:
            print(f"One argument constructor called with arg1: {arg1}")
        else:
            print(f"Two arguments constructor called with arg1: {arg1} and arg2: {arg2}")

# Main class to instantiate the constructors
def main():
    obj1 = ExampleClass()  # Calls default constructor
    obj2 = ExampleClass(10)  # Calls one argument constructor
    obj3 = ExampleClass(10, 20)  # Calls two arguments constructor

if __name__ == "__main__":
    main()





class SuperClass:
    def __init__(self):
        print("Superclass default constructor called")
    
    def __init__(self, arg1):
        print(f"Superclass one-argument constructor called with arg1: {arg1}")

class ChildClass(SuperClass):
    def __init__(self):
        super().__init__("Hello from child")  # Calls the one-argument constructor of the superclass
        print("Child class constructor called")

def main():
    child = ChildClass()

if __name__ == "__main__":
    main()









class AccessModifiers:
    def __init__(self):
        print("Public constructor called")

    def _protected_constructor(self):
        print("Protected constructor called")

    def __private_constructor(self):
        print("Private constructor called")

# Instantiating and calling methods
obj = AccessModifiers()
obj._protected_constructor()  # Protected constructor
# obj.__private_constructor()  # Will raise an error, as it's private

# Accessing the private constructor (not recommended but possible)
obj._AccessModifiers__private_constructor()









class Person:
    def __init__(self, name, age):
        # These are the attributes of the constructor
        self.name = name
        self.age = age
        print(f"Person object created with name: {self.name} and age: {self.age}")

def main():
    person1 = Person("Alice", 30)
    person2 = Person("Bob", 25)

if __name__ == "__main__":
    main()

