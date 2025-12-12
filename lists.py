#LISTS/TUPLES
# 1. Input 10 numbers and print the second largest
lst = []
for i in range(10):
    lst.append(int(input("Enter number: ")))

lst.sort()
print("Second largest:", lst[-2])


# 2. Remove duplicates from a list (without set)
lst = [int(x) for x in input("Enter numbers: ").split()]
new_list = []
for x in lst:
    if x not in new_list:
        new_list.append(x)
print("Without duplicates:", new_list)


# 3. Count how many times each item appears
lst = [int(x) for x in input("Enter numbers: ").split()]
for x in lst:
    print(x, "=", lst.count(x))


# 4. Merge two lists and sort
l1 = [int(x) for x in input("Enter list 1: ").split()]
l2 = [int(x) for x in input("Enter list 2: ").split()]
merged = l1 + l2
merged.sort()
print("Merged & sorted:", merged)


# 5. Convert list to tuple and tuple to list
lst = [int(x) for x in input("Enter numbers: ").split()]
t = tuple(lst)
print("Tuple:", t)
lst2 = list(t)
print("Back to list:", lst2)


# 6. Sum of all elements (without sum())
lst = [int(x) for x in input("Enter numbers: ").split()]
total = 0
for x in lst:
    total += x
print("Sum =", total)


# 7. Reverse a list using slicing
lst = [int(x) for x in input("Enter numbers: ").split()]
print("Reversed:", lst[::-1])


# 8. Print numbers greater than 50 from tuple
t = tuple(int(x) for x in input("Enter numbers: ").split())
for x in t:
    if x > 50:
        print(x)


# 9. Find index of a value (handle not found)
t = tuple(int(x) for x in input("Enter numbers: ").split())
value = int(input("Enter value to find: "))

if value in t:
    print("Index:", t.index(value))
else:
    print("Value not found")


# 10. Multiply all elements of a list
lst = [int(x) for x in input("Enter numbers: ").split()]
product = 1
for x in lst:
    product *= x
print("Product =", product)