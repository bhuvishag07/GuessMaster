#Take two numbers and print sum, difference, product
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)


# 2. Check if number is positive, negative, or zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 3. Check whether number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 4. Input marks of 5 subjects: total, average, percentage
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = (total / 500) * 100

print("Total =", total)
print("Average =", average)
print("Percentage =", percentage) 

# 5. Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)


# 6. Swap two variables without using a third variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)


# 7. Reverse a three-digit number
num = int(input("Enter a 3-digit number: "))
reverse = (num % 10) * 100 + (num // 10 % 10) * 10 + (num // 100)
print("Reversed number =", reverse)


# 8. Check voting eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


# 9. Print multiplication table (1–10)
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "*", i, "=", num * i)


# 10. Print largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest is:", a)
elif b >= a and b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)#