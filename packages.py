/my_project
    /mypackage
        /package_a
            __init__.py
            class_a.py
        /package_b
            __init__.py
            class_b.py
    main.py



# class_a.py
class ClassA:
    def __init__(self):
        print("Constructor of ClassA is called.")

    def method_a(self):
        print("Method of ClassA is called.")


# class_b.py
class ClassB:
    def __init__(self):
        print("Constructor of ClassB is called.")

    def method_b(self):
        print("Method of ClassB is called.")


# __init__.py for package_a
from .class_a import ClassA
# __init__.py for package_b
from .class_b import ClassB
# __init__.py for mypackage
from .package_a import ClassA
from .package_b import ClassB



# main.py
from mypackage import ClassA, ClassB

# Create objects of each class
obj_a = ClassA()
obj_b = ClassB()

# Call methods of each class
obj_a.method_a()
obj_b.method_b()

