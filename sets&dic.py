# 1. Input two sets and print union, intersection, and difference
print("\n--- 1. Set Operations ---")
s1 = set(input("Enter set 1 elements: ").split())
s2 = set(input("Enter set 2 elements: ").split())
print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference (s1 - s2):", s1 - s2)


# 2. Create dictionary of 5 students marks and print topper
print("\n--- 2. Topper from Dictionary ---")
students = {}
for i in range(5):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

topper = max(students, key=students.get)
print("Topper:", topper, "=>", students[topper])


# 3. Word frequency counter (using dictionary)
print("\n--- 3. Word Frequency Counter ---")
text = input("Enter a paragraph: ").lower().split()
freq = {}

for word in text:
    freq[word] = freq.get(word, 0) + 1

print("Word frequencies:", freq)


# 4. Remove a key-value pair from dictionary
print("\n--- 4. Remove Key from Dictionary ---")
d = {"a": 10, "b": 20, "c": 30, "d": 40}
print("Original:", d)
key = input("Enter key to remove: ")

if key in d:
    del d[key]
    print("Updated:", d)
else:
    print("Key not found!")


# 5. Convert two lists (keys & values) into a dictionary
print("\n--- 5. Lists to Dictionary ---")
keys = input("Enter keys: ").split()
values = input("Enter values: ").split()
d = dict(zip(keys, values))
print("Dictionary:", d)


# 6. Reverse a dictionary (swap keys & values)
print("\n--- 6. Reverse Dictionary ---")
d = {}
n = int(input("Enter number of items: "))
for i in range(n):
    k = input("Key: ")
    v = input("Value: ")
    d[k] = v

rev = {v: k for k, v in d.items()}
print("Reversed:", rev)


# 7. Find common values between two dictionaries
print("\n--- 7. Common Values Between Dictionaries ---")
d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"x": 3, "y": 2, "z": 5}
common = set(d1.values()) & set(d2.values())
print("Common values:", common)


# 8. Count how many unique values exist across dictionary items
print("\n--- 8. Count Unique Values ---")
d = {}
n = int(input("Enter number of dictionary items: "))
for i in range(n):
    k = input("Key: ")
    v = input("Value: ")
    d[k] = v

unique_values = len(set(d.values()))
print("Unique values count:", unique_values)


# 9. Print unique elements of a list using a set
print("\n--- 9. Unique Elements Using Set ---")
lst = input("Enter list elements: ").split()
unique = set(lst)
print("Unique elements:", unique)
