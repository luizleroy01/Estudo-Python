#use of dictionaries with python
# Creating a dictionary
student = {
    'name': 'John Doe',
    'age': 20,
    'major': 'Computer Science',
    'GPA': 3.5
}

# Accessing values using keys
print("Name:", student['name'])
print("Age:", student['age'])
print("Major:", student['major'])
print("GPA:", student['GPA'])

# Adding a new key-value pair
student['email'] = 'john.doe@example.com'

# Modifying a value
student['GPA'] = 3.7

# Removing a key-value pair
del student['age']

# Iterating over keys
print("Keys:")
for key in student.keys():
    print(key)

# Iterating over values
print("Values:")
for value in student.values():
    print(value)

# Iterating over key-value pairs
print("Key-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)
