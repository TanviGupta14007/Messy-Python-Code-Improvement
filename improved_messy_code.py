NUM_SUBJECTS = 3

students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88],
]


def get_marks(student):
    """Return the list of subject marks (everything after the name)."""
    return student[1:]


def marks_are_valid(marks):
    """Marks must be numbers from 0 to 100."""
    for mark in marks:
        if mark < 0 or mark > 100:
            return False
    return True


def calculate_total(marks):
    total = 0
    for mark in marks:
        total = total + mark
    return total


def calculate_average(marks):
    return calculate_total(marks) / NUM_SUBJECTS


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


def valid_students(all_students):
    """Keep students with valid marks and print a warning for the rest."""
    accepted = []
    for student in all_students:
        name = student[0]
        marks = get_marks(student)
        if len(marks) != NUM_SUBJECTS or not marks_are_valid(marks):
            print(f"Skipping {name}: marks must be {NUM_SUBJECTS} numbers between 0 and 100.")
        else:
            accepted.append(student)
    return accepted


def find_class_average(all_students):
    total_of_averages = 0
    for student in all_students:
        total_of_averages = total_of_averages + calculate_average(get_marks(student))
    return total_of_averages / len(all_students)


def find_topper(all_students):
    topper_name = ""
    highest_average = -1

    for student in all_students:
        average = calculate_average(get_marks(student))
        if average > highest_average:
            highest_average = average
            topper_name = student[0]

    return topper_name, highest_average


def count_above_class_average(all_students):
    """Return how many students have an average higher than the class average."""
    class_avg = find_class_average(all_students)
    count = 0
    for student in all_students:
        if calculate_average(get_marks(student)) > class_avg:
            count = count + 1
    return count


def print_report(all_students):
    print("STUDENT MARKS REPORT")
    print("-" * 44)
    print(f"{'Name':<10}{'Total':>8}{'Average':>12}{'Grade':>10}")
    print("-" * 44)

    for student in all_students:
        name = student[0]
        marks = get_marks(student)
        total = calculate_total(marks)
        average = calculate_average(marks)
        grade = get_grade(average)
        print(f"{name:<10}{total:>8}{average:>12.2f}{grade:>10}")

    print("-" * 44)
    class_avg = find_class_average(all_students)
    topper_name, topper_average = find_topper(all_students)
    above_average = count_above_class_average(all_students)
    print(f"Class average: {class_avg:.2f}")
    print(f"Topper: {topper_name} ({topper_average:.2f})")
    print(f"Students above class average: {above_average}")


accepted_students = valid_students(students)

if len(accepted_students) == 0:
    print("No valid student records to report.")
else:
    print_report(accepted_students)
