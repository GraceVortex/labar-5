import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

#1. Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
a = re.findall(r"ed*", text)
if a:
    print(a)
else:
    print("None")

#2. Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
b = re.findall(r"ab{2,3}", text)
print(b)

#3. Write a Python program to find sequences of lowercase letters joined with a underscore.
c = re.findall(r"[a-z]+_[a-z]+", text)
print(c)

#4. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
d = re.findall(r"[A-Z][a-z]+", text)
print(d)

#5. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'
e = re.findall(r"a.*b", text)
print(e)

#6. Write a Python program to replace all occurrences of space, comma, or dot with a colon.
f = re.sub(r"[ .,]", ":", text)
print(f)

#7. Write a python program to convert snake case string to camel case string.
g = re.sub(r'_([a-z])', lambda match: match.group(1).upper(), text)
print(g)

#8. Write a Python program to split a string at uppercase letters.
h = re.split("[A-Z]", text)
print(h)

#9. Write a Python program to insert spaces between words starting with capital letters.
i = re.sub(r"([A-Z])", r" \1", text)
print(i)

#10. Write a Python program to convert a given camel case string to snake case
j = re.sub(r'([a-z0-9])([A-Z])', r'\1:\2', text)
k = j.lower()
print(k)

