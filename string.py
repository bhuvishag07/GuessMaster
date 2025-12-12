#STRINGS

# 1. Count vowels, consonants, digits, spaces
s = input("Enter a string: ")

v = c = d = sp = 0

for ch in s:
    if ch.lower() in "aeiou":
        v += 1
    elif ch.isalpha():
        c += 1
    elif ch.isdigit():
        d += 1
    elif ch == " ":
        sp += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Spaces:", sp)


# 2. Check if string is palindrome
s = input("Enter a string: ")
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 3. Replace spaces with '-'
s = input("Enter a sentence: ")
print(s.replace(" ", "-"))


# 4. Print characters at even index positions
s = input("Enter a string: ")
for i in range(0, len(s), 2):
    print(s[i])


# 5. Print each word on new line
s = input("Enter a sentence: ")
for word in s.split():
    print(word)


# 6. Count occurrences of a character
s = input("Enter a string: ")
ch = input("Enter character: ")
print("Count =", s.count(ch))


# 7. Find longest word in sentence
s = input("Enter a sentence: ")
words = s.split()
longest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
print("Longest word:", longest)


# 8. Remove duplicate characters
s = input("Enter a string: ")
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("Without duplicates:", result)