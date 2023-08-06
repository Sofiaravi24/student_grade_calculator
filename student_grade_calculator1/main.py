import csv
import os
from student_grade_calculator1.utils import Student


def load_student_data(filename):
    students = []
    if not os.path.exists(filename):
        # If the file doesn't exist, create a new one with header
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Mathematics', 'Science', 'English'])  # Header row
    else:
        # If the file exists, load student data from it
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                name, *grades = row
                grades = [float(grade) for grade in grades]
                student = Student(name, grades)
                students.append(student)

    return students


def save_student_data(filename, students):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Mathematics', 'Science', 'English'])  # Header row
        for student in students:
            writer.writerow([student.name, *student.grades])


def get_class_average_grade(students):
    students_grade_sum = sum([sum(student.grades) for student in students])
    total_students_grades = len(students) * 3
    get_class_average_grade = round(students_grade_sum / total_students_grades, 2)
    return get_class_average_grade


def get_highest_lowest_students_info(students):
    hg = -101
    lg = 101
    hgs = None
    lgs = None
    for student in students:
        avg_grade = student.calculate_average_grades()
        if avg_grade >= hg:
            hg = avg_grade
            hgs = student.name
        if avg_grade >= lg:
            lg = avg_grade
            lgs = student.name
    return hg, hgs, lg, lgs

def get_existing_students_name(students):
    return get_existing_students_name


def main():
    print("Welcome to the Student grade calculator!\n")

    filename = "grade.csv"
    students = load_student_data(filename)

    filename = "grades.csv"
    students = load_student_data(filename)

    while True:
        print("\n1. Add New Student")
        print("2. Update Grades")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Class Statistics")
        print("6. Save and Exit")

        choice = input("\n Enter your choice: ")
        if choice == "1":
            name = input("Enter the students name:")
            existing_students = get_existing_students_name(students)
            if name in existing_students:
                print("Students already exist in database:")
            else:
             name = input("Enter the students name: ")
             math_grade = float(input("Enter Mathematics Grade: "))
             sci_grade = float(input("Enter Science Grade: "))
             eng_grade = float(input("Enter English Grade: "))
             new_student = Student(name, [math_grade, sci_grade, eng_grade])
             students.append(new_student)
             save_student_data(filename, students)
             print(f"added {name} to the students")

        elif choice == "2":
            name = input("Enter student name , to update grades")
            found = False
            for student in students:
                if student.name == name:
                    found = True
                    print("Student found, please add updated grades below:")
                    math_grade = float(input("Enter Mathematics Grade: "))
                    sci_grade = float(input("Enter Science Grade: "))
                    eng_grade = float(input("Enter English Grade: "))
                    student.grades = [math_grade, sci_grade, eng_grade]
                    save_student_data(filename, students)
                    print("updated students grades data:")
                    break
                if not found:
                    print("student name is not found in database!")

        elif choice == "3":
            name = input("Enter student name , to update grades:")
            found = False
            for student in students:
                if student.name == name:
                    found = True
                    students.remove(student)
                    save_student_data(filename, students)
                    print("deleted student from database!")
                    break
                if not found:
                    print("student name is not found in database!")


        elif choice == "4":
            print("\n----- All Students -----")
            for idx, student in enumerate(students, 1):
                avg_grade = student.calculate_average_grades()
                print(f"{idx}. {student.name} - Average Grade: {avg_grade:.2f}")

        elif choice == "5":
            class_averge_grade = get_class_average_grade(students)
            hg, hgs, lg, lgs = get_highest_lowest_students_info(students)
            print("--------Class statistics--------\n")
            print("Overall Class Average Grade: ", class_averge_grade)
            print(f"Class Highest Grade:{hg} student name: {hgs}")
            print(f"Class Lowest Grade:{lg} student name: {lgs}")



        elif choice == "6":
            save_student_data(filename, students)
            print("students data saved!")
        else:
            print("invalid")


if __name__ == '__main__':
    main()
