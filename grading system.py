# Program to calculate average marks and assign grade

def calculate_grade(avg):
    if 91 <= avg <= 100:
        return "A1"
    elif 81 <= avg <= 90:
        return "A2"
    elif 71 <= avg <= 80:
        return "B1"
    elif 61 <= avg <= 70:
        return "B2"
    elif 51 <= avg <= 60:
        return "C1"
    elif 41 <= avg <= 50:
        return "C2"
    elif 33 <= avg <= 40:
        return "D"
    elif 21 <= avg <= 32:
        return "E1"
    else:
        return "E2"

# Input marks for 5 subjects
marks = []
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i}: "))
    marks.append(mark)

# Calculate average
average = sum(marks) / 5

# Get grade
grade = calculate_grade(average)

# Display result
print("\n--- Result ---")
print("Marks:", marks)
print("Average Marks:", average)
print("Grade:", grade)
