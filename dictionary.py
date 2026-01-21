# Step 1: Create an empty dictionary
student_marks = {}

# Step 2: Add students and their marks
student_marks["Alice"] = 85
student_marks["Bob"] = 90
student_marks["Charlie"] = 78

# Step 3: Display all students with their marks
print("Student Marks:")
for name, marks in student_marks.items():
    print(name, ":", marks)

# Step 4: Find marks of a specific student
student_name = "Bob"
if student_name in student_marks:
    print("\nMarks of", student_name, ":", student_marks[student_name])
else:
    print("\nStudent not found")

# Step 5: Update a student's marks
student_marks["Charlie"] = 82
print("\nUpdated marks of Charlie:", student_marks["Charlie"])

# Step 6: Remove a student
del student_marks["Alice"]

# Step 7: Display dictionary after deletion
print("\nFinal Student Marks:")
print(student_marks)
