def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

num_students = int(input("Enter the number of students: "))

for _ in range(num_students):
    name = input("Enter the student's name: ")
    score = int(input(f"Enter {name}'s score (0-100): "))
    grade = check_grade(score)
    print(f"{name}'s grade is: {grade}")
