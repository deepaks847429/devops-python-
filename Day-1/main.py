age=25
price =19.99
name="Deepak Kumar"
is_student=True
print("Hello, Deepak!")
print("Age:", age)
print("price:", price)
print("Name:", name)
print("Is Student:", is_student)

#Typecasting

age= 2
print ("Age:", age)
y= float(age)
print("Age after typecasting:", y)

# Type checking 

print("Type of age:", type(age))
print("Type of y:", type(y))

# local and global scope
gretting= "welcome"
def greet():
  gretting="hello deepak" 
  print(gretting)


greet()
print(gretting)

# operators
# Arithmetic operators
a = 10
b = 5 
print("Addition:", a + b)
print("Subtraction:", a - b)  
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
# Comparison operators
print("Is a equal to b?", a == b)
print("Is a not equal to b?", a != b)
print("Is a greater than b?", a > b)
print("Is a less than b?", a < b)
print("Is a greater than or equal to b?", a >= b)
print("Is a less than or equal to b?", a <= b)

# Logical operators
print("Logical AND:", a > 5 and b < 10)
print("Logical OR:", a > 5 or b > 10)
print("Logical NOT:", not (a > 5))
# Bitwise operators
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)
# Assignment operators
c = a  # Assignment
c += b  # c = c + b
print("c after +=:", c)
# Identity operators
print("Is a identical to b?", a is b)
print("Is a not identical to b?", a is not b)
# Membership operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list)
print("Is 6 not in my_list?", 6 not in my_list)
# Identity operators
print("Is a identical to b?", a is b)
print("Is a not identical to b?", a is not b)
# Membership operators
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list) 
print("Is 6 not in my_list?", 6 not in my_list)
# Assignment operators
c = a  # Assignment
c += b  # c = c + b
print("c after +=:", c)
#


# functions to learn python
#function to calculate discount
def calculate_discount(price, discount_rate):
  discount= price * (discount_rate / 100)
  final_price=price-discount
  return final_price

# age validation function
def valid_age(age):
  if age<0:
    return "Inavalid age"
  elif age<18:
    return "You are a minor"
  elif age<60:
    return "You are an adult"
  else:
    return "You are a senior citizen"

# Function to check if a number is prime
def is_prime(num):
  if num<=1:
    return false
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False