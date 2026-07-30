# grade_manager.py
students = []

# Step 1: Data entry
print("===== Grade Manager =====")
for i in range(5):
    print(f"\nStudent {i + 1}")
    name = input("Enter student's name: ")
    
    while True:
        try:
            grade = float(input("Enter grade (out of 20): "))
            if 0 <= grade <= 20:
                break
            print("Invalid grade! Please enter a value between 0 and 20.")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")
            
    students.append({"name": name, "grade": grade})

# Step 2: Display the Table
print("\n===== Students Summary =====")
print("{:<20} {:<10}".format("Name", "Grade"))
print("-" * 30)
for student in students:
    print("{:<20} {:<10}".format(student["name"], student["grade"]))

# Step 3: Statistics
total = sum(student["grade"] for student in students)
average = total / len(students)
highest = max(students, key=lambda x: x["grade"])
lowest = min(students, key=lambda x: x["grade"])

print("\n===== Statistics =====")
print(f"Class Average: {average:.2f}")
print(f"Highest Grade: {highest['grade']} (Student: {highest['name']})")
print(f"Lowest Grade: {lowest['grade']} (Student: {lowest['name']})")

# Step 4: Display Grades
print("\n===== Student Performance =====")
for student in students:
    grade = student["grade"]
    # Fixed conditional gaps using continuous >= check boundaries
    if grade >= 16:
        remark = "Very Good"
    elif grade >= 14:
        remark = "Good"
    elif grade >= 12:
        remark = "Fair"
    elif grade >= 10:
        remark = "Pass"
    else:
        remark = "Fail"
        
    print(f"{student['name']}: {grade} --> {remark}")
