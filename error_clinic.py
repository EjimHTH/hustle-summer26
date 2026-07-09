#Snippet 1
# I predict an error because i is dividing by 0 so it will be a zero division error
x = 10
y = 0
if y != 0:
    result = x/y
    print("Result:", result)
else:
    print("Cannot divide by zero.")

#Snippet 2
 #This is an idex error due range
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
 print(numbers[i])

#Snippet 3
# I think this falls under a syntax error because its missing a :
def calculate_area(radius):
 area = 3.14 * radius ** 2
 return area
radius = 5
print(calculate_area(radius))

#Snippet 4
# I think this is a syntax error because missing ":" & spacing so IndentationError
def is_even(number):
 if number % 2 == 0:
    return True
 else:
    return False
print(is_even(4))
print(is_even(7))

#Snippet 5
#it will be another syntax error
for i in range(5):
 print(i)

 #Snippet 6
 #I think this will fall syntax error due to string being seperated
def greet(name):
 return "Hello, "+ name
print(greet("Alice"))

#Snippet 7
#IndentationError due to an indent spacing missing in line 4
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number
print("Sum of numbers:", total)

#Snippet 8
#I predict it being a program that does not stop
def factorial(n):
 if n == 0:
    return 1
 else:
    return n * factorial(n - 1)
print(factorial(5))

#Snippet 9
# it is logic error 
name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
 print("Hello, " + name)
else:
 print("Hello, stranger!")

#Snippet 10
#zero division due to it trying to divide 10 by 0
def divide_numbers(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    result = x / y
    return result
num1 = 10
num2 = 0
print(divide_numbers(num1, num2))
