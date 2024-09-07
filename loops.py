for i in range(10):
    print("Bright IT Career")



number = 1
while number <= 20:
    print(number)
    number += 1



a = 10
b = 20
if a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is not equal to {b}")
if a != b:
    print(f"{a} is not equal to {b}")
else:
    print(f"{a} is equal to {b}")



for number in range(1, 21):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")




a = 10
b = 25
c = 15
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print(f"The largest number among {a}, {b}, and {c} is {largest}.")





number = 10
while number <= 20:
    if number % 2 == 0:
        print(number)
    number += 1




number = 1
while True:
    print(number)
    number += 1
    if number > 10:
        break


def is_armstrong_number(number):
    digits = str(number)
    num_digits = len(digits)
    total_sum = sum(int(digit) ** num_digits for digit in digits)
    return total_sum == number
input_number = 153
if is_armstrong_number(input_number):
    print(f'{input_number} is an Armstrong number.')
else:
    print(f'{input_number} is not an Armstrong number.')




def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
input_number = 29
if is_prime(input_number):
    print(f'{input_number} is a prime number.')
else:
    print(f'{input_number} is not a prime number.')




def is_palindrome_number(number):
    number_str = str(number)
    if number_str == number_str[::-1]:
        return True
    else:
        return False
input_number = 121
if is_palindrome_number(input_number):
    print(f'{input_number} is a palindrome.')
else:
    print(f'{input_number} is not a palindrome.')



def check_even_odd(number):
    switch = {
        0: "Even",
        1: "Odd"
    }
    result = switch.get(number % 2)
    print(f"The number {number} is {result}.")
check_even_odd(10)
check_even_odd(7)




def print_gender(gender_code):
    switch = {
        'M': "Male",
        'F': "Female"
    }
    print(switch.get(gender_code.upper(), "Invalid code"))
print_gender('M')
print_gender('F')
print_gender('X')
