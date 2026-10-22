NUM_SUBJECTS = 3

students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88],
]


def calculate_total(student):
    """Return the sum of a student's subject marks."""
    total = 0
    for mark_index in range(1, len(student)):
        total = total + student[mark_index]
    return total


def calculate_average(student):
    """Return the student's average using a fixed number of subjects."""
    return calculate_total(student) / NUM_SUBJECTS


def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


print("REPORT")

for student in students:
    total = calculate_total(student)
    average = calculate_average(student)
    grade = get_grade(average)
    print(f"{student[0]}{total}{average}{grade}")

sum_of_averages = 0

for student in students:
    average = calculate_average(student)
    sum_of_averages = sum_of_averages + average

print(f"Class average:{sum_of_averages / len(students)}")

highest_average = 0
topper_name = ""

for student in students:
    average = calculate_average(student)
    if average > highest_average:
        highest_average = average
        topper_name = student[0]

print(f"Topper:{topper_name}{highest_average}")
