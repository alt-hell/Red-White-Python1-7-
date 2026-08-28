students = {}

print("=" * 60)
print("        WELCOME TO THE STUDENT DATA ORGANIZER")
print("=" * 60)

while True:

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # --------------------------------------------------
    # ADD STUDENT
    # --------------------------------------------------
    if choice == "1":

        print("\n--- Add Student ---")

        student_id = input("Enter Student ID: ")

        if student_id in students:
            print("Student ID already exists!")
            continue

        name = input("Enter Name: ")

        while True:
            try:
                age = int(input("Enter Age: "))

                if age <= 0:
                    print("Age must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Please enter a valid age.")

        grade = input("Enter Grade: ")

        dob = input("Enter Date of Birth (YYYY-MM-DD): ")

        subjects_input = input(
            "Enter Subjects (comma-separated): "
        )

        subjects = set()

        for subject in subjects_input.split(","):
            subject = subject.strip()

            if subject:
                subjects.add(subject)

        # Tuple for immutable information
        student_id_and_dob = (student_id, dob)

        # Dictionary containing student information
        students[student_id] = {
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects,
            "id_dob": student_id_and_dob
        }

        print("\nStudent added successfully!")


    # --------------------------------------------------
    # DISPLAY ALL STUDENTS
    # --------------------------------------------------
    elif choice == "2":

        print("\n--- Display All Students ---")

        if not students:
            print("No student records available.")
            continue

        for student_id, data in students.items():

            print("\n" + "-" * 60)

            print(
                f"Student ID: {student_id} | "
                f"Name: {data['name']} | "
                f"Age: {data['age']} | "
                f"Grade: {data['grade']}"
            )

            print(
                f"Date of Birth: {data['id_dob'][1]}"
            )

            print(
                "Subjects:",
                ", ".join(sorted(data["subjects"]))
            )

            print(
                "ID and DOB Tuple:",
                data["id_dob"]
            )

        print("-" * 60)


    # --------------------------------------------------
    # UPDATE STUDENT
    # --------------------------------------------------
    elif choice == "3":

        print("\n--- Update Student Information ---")

        student_id = input("Enter Student ID to update: ")

        if student_id not in students:
            print("Student not found!")
            continue

        student = students[student_id]

        print("\nLeave input blank to keep the existing value.")

        new_name = input(
            f"Enter Name [{student['name']}]: "
        )

        if new_name:
            student["name"] = new_name

        while True:

            new_age = input(
                f"Enter Age [{student['age']}]: "
            )

            if new_age == "":
                break

            try:
                new_age = int(new_age)

                if new_age <= 0:
                    print("Age must be greater than 0.")
                    continue

                student["age"] = new_age
                break

            except ValueError:
                print("Please enter a valid age.")

        new_grade = input(
            f"Enter Grade [{student['grade']}]: "
        )

        if new_grade:
            student["grade"] = new_grade

        new_subjects = input(
            "Enter new Subjects (comma-separated, blank to keep existing): "
        )

        if new_subjects:
            subjects = set()

            for subject in new_subjects.split(","):
                subject = subject.strip()

                if subject:
                    subjects.add(subject)

            student["subjects"] = subjects

        print("Student information updated successfully!")


    # --------------------------------------------------
    # DELETE STUDENT
    # --------------------------------------------------
    elif choice == "4":

        print("\n--- Delete Student ---")

        student_id = input("Enter Student ID to delete: ")

        if student_id in students:

            del students[student_id]

            print("Student deleted successfully!")

        else:
            print("Student not found!")


    # --------------------------------------------------
    # DISPLAY UNIQUE SUBJECTS
    # --------------------------------------------------
    elif choice == "5":

        print("\n--- Subjects Offered ---")

        all_subjects = set()

        for student in students.values():
            all_subjects.update(student["subjects"])

        if all_subjects:
            print("Unique Subjects:")

            for subject in sorted(all_subjects):
                print("-", subject)

        else:
            print("No subjects available.")


    # --------------------------------------------------
    # EXIT
    # --------------------------------------------------
    elif choice == "6":

        print("\nThank you for using the Student Data Organizer!")
        print("Exiting the program. Goodbye!")

        break


    # --------------------------------------------------
    # INVALID OPTION
    # --------------------------------------------------
    else:

        print("Invalid choice! Please select between 1 and 6.")