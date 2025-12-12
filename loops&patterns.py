# 1. Print a right-angle star pattern
print("\n--- 1. Right-Angle Star Pattern ---")
n = int(input("Enter rows: "))
for i in range(1, n + 1):
    print("*" * i)


# 2. Print a pyramid pattern
print("\n--- 2. Pyramid Pattern ---")
n = int(input("Enter rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


# 3. Sum of digits of a number using loop
print("\n--- 3. Sum of Digits ---")
num = int(input("Enter number: "))
s = 0
while num > 0:
    s += num % 10
    num //= 10
print("Sum of digits:", s)


# 4. Factorial of a number using loop
print("\n--- 4. Factorial ---")
num = int(input("Enter number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)


# 5. Print numbers 1 to 100 skipping multiples of 3
print("\n--- 5. Skip Multiples of 3 ---")
for i in range(1, 101):
    if i % 3 == 0:
        continue
    print(i, end=" ")


# 6. Print prime numbers between 1 and 100
print("\n--- 6. Prime Numbers (1 to 100) ---")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")


# 7. Print Fibonacci series up to n terms
print("\n--- 7. Fibonacci Series ---")
n = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


# 8. Count digits in a number (no string conversion)
print("\n--- 8. Count Digits ---")
num = int(input("Enter number: "))
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10
print("Total digits:", count)
