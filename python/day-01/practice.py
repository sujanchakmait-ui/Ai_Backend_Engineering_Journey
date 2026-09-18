# Day 01 - Python Fundamentals

Name = "sujan chakma"
Age = 25
GPA = 3.17
Is_Student = True

print(type(Name))
print(type(Age))
print(type(GPA))
print(type(Is_Student))

# f-string practice
print(f"Name: {Name}, Age: {Age}, GPA: {GPA}, Is_Student: {Is_Student}")

# Type conversion - string to integer
age = "25"
age = int(age)

print(age)
print(type(age))

# Type conversion - string to float
price = "99.50"
price = float(price)

print(price)
print(type(price))

# Boolean conversion
text = "True"
text = bool(text)

print(text)
print(type(text))

# Conversion + calculation
score = "85.5"
score = float(score)

result = score + 10

print(result)
print(type(result))
