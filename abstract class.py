from abc import ABC, abstractmethod

# 1. Abstract class with abstract and non-abstract methods
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Abstract method that must be implemented by all subclasses."""
        pass

    def sleep(self):
        """Non-abstract method with a default implementation."""
        print("The animal is sleeping")

# 2. Subclass that inherits from the abstract class and implements the abstract method
class Dog(Animal):
    def make_sound(self):
        """Implementation of the abstract method."""
        print("Woof Woof!")

# 3. Create an object in the child class for the abstract class and access the non-abstract methods
dog = Dog()
dog.sleep()  # Accessing the non-abstract method

# 4. Create an instance for the child class and call abstract and non-abstract methods
dog.make_sound()  # Calling the abstract method implemented in the subclass
dog.sleep()  # Calling the non-abstract method from the abstract class

