# reference 

myVar = 10
print(myVar, id(myVar))
myVar2 = 10
print(myVar2, id(myVar2))
myVar3 = 19
print(myVar3, id(myVar3))

#output - if value is same then python points the same reference to save memory location
# 10 139888762321456
# 10 139888762321456
# 19 139888762321744

# Arithmetic Opeartors
a = 10
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", int(a / b)) # using int() to get integer result
print("Modulus:", a % 6) # gives remainder
print("Exponentiation:", a ** 2) # a raised to the power of 2
print("Floor Division:", a // b) # gives quotient without remainder

# Assignment Operator 
c = 10
c+=5
print("Assign",c)
c-=5
print("Assign",c)
c*=5
print("Assign",c)
c/=5
print("Assign",c)
c%=5
print("Assign",c)
c**=5
print("Assign",c)
c//=5
print("Assign",c)

# Comparitive Operators 
num1 = 10
num2 = 20
print(num1 == num2) # False
print(num1 != num2) # True
print(num1 > num2) # False
print(num1 < num2) # True
print(num1 >= num2) # False
print(num1 <= num2) # True

# Logical Operators
print(3 == 3 and 5 == 5)
print(3 == 3 or 5 == 5)
print(not 5 >3)