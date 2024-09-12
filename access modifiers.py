class ParentClass:
    def __init__(self):
        # Private field (only accessible within this class)
        self.__private_field = "I am a private field"

    # Private method (only accessible within this class)
    def __private_method(self):
        return "I am a private method"

    # A main method to show how to access private members
    def main(self):
        print("Accessing private field from within the class:", self.__private_field)
        print("Calling private method from within the class:", self.__private_method())


# A child class that tries to access private members from the parent class
class SubClass(ParentClass):
    def access_private(self):
        # Trying to access the private field
        try:
            print("Trying to access private field from subclass:", self.__private_field)
        except AttributeError as e:
            print("Cannot access private field from subclass:", e)

        # Trying to call the private method
        try:
            print("Trying to call private method from subclass:", self.__private_method())
        except AttributeError as e:
            print("Cannot call private method from subclass:", e)


# Create an object of the parent class and run its main method
parent_obj = ParentClass()
parent_obj.main()

# Create an object of the child class and try to access private members
subclass_obj = SubClass()
subclass_obj.access_private()

-----------------------------------------------------------------------------------

base.py

# base.py

class BaseClass:
    def __init__(self):
        # Protected field (single underscore)
        self._protected_field = "I am a protected field"

    # Protected method
    def _protected_method(self):
        return "I am a protected method"
    
    # Method to print protected members
    def show_protected(self):
        print("BaseClass: Accessing protected field:", self._protected_field)
        print("BaseClass: Calling protected method:", self._protected_method())


same_package.py

# same_package.py

from base import BaseClass

class SamePackageClass:
    def __init__(self):
        base_instance = BaseClass()
        print("SamePackageClass: Accessing protected field:", base_instance._protected_field)
        print("SamePackageClass: Calling protected method:", base_instance._protected_method())

# Create an instance of SamePackageClass to test access
if __name__ == "__main__":
    obj = SamePackageClass()



different_package_child.py

# different_package_child.py

from base import BaseClass

class DifferentPackageChild(BaseClass):
    def access_protected(self):
        print("DifferentPackageChild: Accessing protected field:", self._protected_field)
        print("DifferentPackageChild: Calling protected method:", self._protected_method())

# Create an instance of DifferentPackageChild to test access
if __name__ == "__main__":
    child = DifferentPackageChild()
    child.access_protected()


different_package.py

# different_package.py

from base import BaseClass

class DifferentPackageClass:
    def __init__(self):
        base_instance = BaseClass()
        try:
            print("DifferentPackageClass: Accessing protected field:", base_instance._protected_field)
        except AttributeError as e:
            print("DifferentPackageClass: Cannot access protected field:", e)

        try:
            print("DifferentPackageClass: Calling protected method:", base_instance._protected_method())
        except AttributeError as e:
            print("DifferentPackageClass: Cannot call protected method:", e)

# Create an instance of DifferentPackageClass to test access
if __name__ == "__main__":
    obj = DifferentPackageClass()


 ---------------------------------------------------------------------------------------------



base.py
# base.py

class BaseClass:
    def __init__(self):
        # Public field
        self.public_field = "I am a public field"

    # Public method
    def public_method(self):
        return "I am a public method"
    
    # Method to print public members
    def show_public(self):
        print("BaseClass: Accessing public field:", self.public_field)
        print("BaseClass: Calling public method:", self.public_method())


same_package.py
# same_package.py

from base import BaseClass

class SamePackageClass:
    def __init__(self):
        base_instance = BaseClass()
        print("SamePackageClass: Accessing public field:", base_instance.public_field)
        print("SamePackageClass: Calling public method:", base_instance.public_method())

# Create an instance of SamePackageClass to test access
if __name__ == "__main__":
    obj = SamePackageClass()


different_package.py
# different_package.py

from base import BaseClass

class DifferentPackageClass:
    def __init__(self):
        base_instance = BaseClass()
        print("DifferentPackageClass: Accessing public field:", base_instance.public_field)
        print("DifferentPackageClass: Calling public method:", base_instance.public_method())

# Create an instance of DifferentPackageClass to test access
if __name__ == "__main__":
    obj = DifferentPackageClass()




