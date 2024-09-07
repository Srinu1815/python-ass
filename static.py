class MyClass:
    static_variable = "This is a static variable"
print(MyClass.static_variable)



class MyClass:
    static_variable = "This is a static variable"
instance = MyClass()
print(instance.static_variable)



class MyClass:
    static_variable = "This is a static variable"
instance = MyClass()
instance.static_variable = "Changed in instance"
print("Instance access:", instance.static_variable)
print("Class access:", MyClass.static_variable)



class MyClass:
    static_variable = "This is a static variable"
MyClass.static_variable = "Changed in class"
instance = MyClass()
print("Class access:", MyClass.static_variable)
print("Instance access:", instance.static_variable)
