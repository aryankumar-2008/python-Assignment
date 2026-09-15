# Student Data Management Using Dictionary, Tuple and List

students = {
    101: ["Rahul", "CSE", 85],
    102: ["Aman", "AI&DS", 90],
    103: ["Riya", "IT", 88]
}

# Add a new student
students[104] = ["Neha", "AI&DS", 92]

# Delete an existing student
del students[102]

# Update details of a student
students[101][2] = 95

# Tuple containing student attributes
student_tuple = (105, "Karan", "CSE", 87)

# List of student roll numbers
roll_numbers = list(students.keys())

# Display final student records
print("Final Student Records:")

for roll, details in students.items():
    print("Roll Number:", roll)
    print("Name:", details[0])
    print("Branch:", details[1])
    print("Marks:", details[2])
    print()
