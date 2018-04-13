# lists, if statements and other goodies
students = [
    "Mark", "John", "Hakan", "Alexis", "Eden"
]

print(students[-1])
print(len(students))
students.append(6)
print(students[1:])

if "Hakan" in students:
    print("var")
else:
    print("yok")

a = 3
b = 2
name = "text"
print(name.upper()) if a > b else print(name.lower())