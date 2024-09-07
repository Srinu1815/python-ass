name = "srinu"
print(name)


print("single line commend")
print(""" multi line
           multi line line
              lines """)


integer=10
boolean=True
char= 'A'
float=2.33
double=3.23450987
print("Integer value:", integer)
print("Type of Integer value:",type(integer))
print("bool value:", boolean)
print("Type of boolean value::",type(boolean))
print("char value:", char)
print("Type of char value::",type(char))
print("float value:", float)
print("Type of float value::",type(float))
print("double value:", double)
print("Type of double value::",type(double))




a = 0  # Define a as a global variable
def f():
    print('global value:', a)
f();


def g():
    a = 1  # Define a as a local variable
    print('local value in g():', a)
g();


def h():
    global a
    a = 3  # Define a as a local variable
    print('local value in h():', a)
h();

print("value of a:",a)
