#Using Single Quotes
string1 = 'Hello'
print(string1)
#Using Double Quotes
string2 = "World"
print(string2)
#Using Triple Quotes
string3 = '''Hello World'''
print(string3)
# Triple Quotes with Multi-line string
string4 = '''Hello
World'''
print(string4)
#Using the str() Function
num = 123
string = str(num)
print(string)
boolean = True
string = str(boolean)
print(string)
#Using format() Method
string = "Hello, {}!".format("Alice")
print(string)
#Using f-Strings
name = "Alice"
string8 = f"Hello, {name}!"
print(string8)
#Using Concatenation
string9 = "Hello" + " " + "World"
print(string9)




str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)



string = "Hello"
length = len(string)
print(length)


string = "Hello World"
substring1 = string[0:5]  
print(substring1)
substring2 = string[6:]  
print(substring2)  # Output: World
substring3 = string[-5:]  
print(substring3)  # Output: World



text = "Hello, world!"
result = text.index("world")
print(result) 



import re
string = "Hello123"
match = re.match(r"\w+", string)
if match:
    print("Match found:", match.group())


str1 = "apple"
str2 = "banana"
print(str1 == str2)
print(str1 != str2)
print(str1 < str2)
print(str1 > str2)


#8

text = "Hello, world!"
print(text.startswith("Hello"))  
print(text.startswith("world", 7))   
print(text.startswith("Hello", 7))     

text = "Hello, world!"
print(text.endswith("world!"))  
print(text.endswith("Hello"))          
print(text.endswith("world", 0, 12))   

str1 = "apple"
str2 = "banana"
result = (str1 > str2) - (str1 < str2)  
print(result)
result = (str2 > str1) - (str2 < str1)  
print(result)
result = (str1 > "apple") - (str1 < "apple")  
print(result)

#9

text = "   Hello, world!   "
trimmed_text = text.strip()
print(trimmed_text)




string = "Hello World"
new_string = string.replace("World", "Python")
print(new_string)




string = "Hello,World,Python"
split_string = string.split(",")
print(split_string)




num = 123
str_num = str(num)
print(str_num)
print(type(str_num))




string = "Hello World"
upper_string = string.upper()
lower_string = string.lower()
print(upper_string)
print(lower_string)
