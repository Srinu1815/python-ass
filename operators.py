a=10
b=10
print(a+b);
print(a-b);
print(a*b);
print(a/b);


def increment(value):
    return value + 1
value = 5
value = increment(value)
print(value)



def are_numbers_equal(num1, num2):
    if num1 == num2:
        return "they are equal"
    else:
        return "they are not equal"
num1 = 10
num2 = 10
result = are_numbers_equal(num1, num2)
print(result)



def relational_operators(num1, num2):
    print(num1 < num2)
    print(num1 <= num2)
    print(num1 > num2)
    print(num1 >= num2)
num1 = 5
num2 = 10
relational_operators(num1, num2)



def print_smaller_larger(num1, num2):
    if num1 < num2:
        smaller = num1
        larger = num2
    else:
        smaller = num2
        larger = num1
    print("Smaller number:", smaller)
    print("Larger number:", larger)
num1 = 5
num2 = 10
print_smaller_larger(num1, num2)
