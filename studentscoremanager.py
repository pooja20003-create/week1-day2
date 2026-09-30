students = {}


def calculate_grade(average):
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


def add_student():
    name = input("Enter student name: ")

    math = float(input("Enter Mathematics mark: "))
    science = float(input("Enter Science mark: "))
    english = float(input("Enter English mark: "))

    average = (math + science + english) / 3
    grade = calculate_grade(average)

    students[name] = {
        "Math": math,
        "Science": science,
        "English": english,
        "Average": average,
        "Grade": grade
    }

    print("\nStudent added successfully!")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")


def display_students():
    if not students:
        print("\nNo students available.")
        return

    print("\n--- Student List ---")

    for name, details in students.items():
        print(f"\nName: {name}")
        print(f"Math: {details['Math']}")
        print(f"Science: {details['Science']}")
        print(f"English: {details['English']}")
        print(f"Average: {details['Average']:.2f}")
        print(f"Grade: {details['Grade']}")


def search_student():
    name = input("Enter student name to search: ")

    if name in students:
        details = students[name]

        print("\n--- Student Details ---")
        print(f"Name: {name}")
        print(f"Math: {details['Math']}")
        print(f"Science: {details['Science']}")
        print(f"English: {details['English']}")
        print(f"Average: {details['Average']:.2f}")
        print(f"Grade: {details['Grade']}")
    else:
        print("Student not found.")


def main():
    while True:
        print("\n===== Student Grade Manager =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            print("Thank you for using Student Grade Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
