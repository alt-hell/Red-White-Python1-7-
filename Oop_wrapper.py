# ============================================================
# PROJECT: OOP WRAPPER
# Employee Management System
# ============================================================

class Employee:
    """
    Base class for creating and managing employee information.
    Demonstrates constructor, destructor, encapsulation,
    getter/setter methods, __str__, and operator overloading.
    """

    def __init__(self, name="Unknown", age=0, employee_id="Not Assigned", salary=0):
        self.name = name
        self.age = age
        self.__employee_id = employee_id
        self.__salary = salary

    # Getter for employee ID
    def get_employee_id(self):
        return self.__employee_id

    # Setter for employee ID
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

    def display(self):
        """
        Display employee information.
        """
        print(f"Name      : {self.name}")
        print(f"Age       : {self.age}")
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary    : ₹{self.__salary:.2f}")

    def __str__(self):
        """
        Return a string representation of the employee.
        """
        return (
            f"Employee(Name={self.name}, "
            f"Age={self.age}, "
            f"ID={self.__employee_id}, "
            f"Salary=₹{self.__salary:.2f})"
        )

    def __eq__(self, other):
        """
        Compare two employees based on salary.
        """
        if isinstance(other, Employee):
            return self.__salary == other.__salary
        return False

    def __lt__(self, other):
        """
        Check whether this employee earns less than another employee.
        """
        if isinstance(other, Employee):
            return self.__salary < other.__salary
        return NotImplemented

    def __gt__(self, other):
        """
        Check whether this employee earns more than another employee.
        """
        if isinstance(other, Employee):
            return self.__salary > other.__salary
        return NotImplemented

    def __del__(self):
        """
        Destructor to clean up employee resources.
        """
        pass


# ============================================================
# MANAGER CLASS
# ============================================================

class Manager(Employee):
    """
    Derived class representing a Manager.
    """

    def __init__(
        self,
        name="Unknown",
        age=0,
        employee_id="Not Assigned",
        salary=0,
        department="General"
    ):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        """
        Override display method to include department information.
        """
        print("Manager Details:")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Salary     : ₹{self.get_salary():.2f}")
        print(f"Department : {self.department}")


# ============================================================
# DEVELOPER CLASS
# ============================================================

class Developer(Employee):
    """
    Derived class representing a Developer.
    """

    def __init__(
        self,
        name="Unknown",
        age=0,
        employee_id="Not Assigned",
        salary=0,
        programming_language="Python"
    ):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        """
        Override display method to include programming language.
        """
        print("Developer Details:")
        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Salary     : ₹{self.get_salary():.2f}")
        print(f"Language   : {self.programming_language}")


# ============================================================
# INPUT FUNCTIONS
# ============================================================

def get_basic_details():
    """
    Get basic employee information from the user.
    """
    name = input("Enter Name: ")

    while True:
        try:
            age = int(input("Enter Age: "))

            if age < 0:
                print("Age cannot be negative.")
                continue

            break
        except ValueError:
            print("Please enter a valid age.")

    return name, age


def get_employee_details():
    """
    Get complete employee information from the user.
    """
    name, age = get_basic_details()

    employee_id = input("Enter Employee ID: ")

    while True:
        try:
            salary = float(input("Enter Salary: "))

            if salary < 0:
                print("Salary cannot be negative.")
                continue

            break
        except ValueError:
            print("Please enter a valid salary.")

    return name, age, employee_id, salary


# ============================================================
# CREATE PERSON
# ============================================================

def create_person():
    """
    Create a basic person-like Employee object.
    """
    name, age = get_basic_details()

    person = Employee(name, age)

    print(f"\nPerson created with name: {name} and age: {age}.")
    return person


# ============================================================
# CREATE EMPLOYEE
# ============================================================

def create_employee():
    """
    Create an Employee object using constructor parameters.
    """
    name, age, employee_id, salary = get_employee_details()

    employee = Employee(
        name,
        age,
        employee_id,
        salary
    )

    print(
        f"\nEmployee created with name: {name}, "
        f"age: {age}, ID: {employee_id}, "
        f"and salary: ₹{salary:.2f}."
    )

    return employee


# ============================================================
# CREATE MANAGER
# ============================================================

def create_manager():
    """
    Create a Manager object.
    """
    name, age, employee_id, salary = get_employee_details()

    department = input("Enter Department: ")

    manager = Manager(
        name,
        age,
        employee_id,
        salary,
        department
    )

    print(
        f"\nManager created with name: {name}, "
        f"age: {age}, ID: {employee_id}, "
        f"salary: ₹{salary:.2f}, "
        f"and department: {department}."
    )

    return manager


# ============================================================
# CREATE DEVELOPER
# ============================================================

def create_developer():
    """
    Create a Developer object.
    """
    name, age, employee_id, salary = get_employee_details()

    language = input(
        "Enter Programming Language: "
    )

    developer = Developer(
        name,
        age,
        employee_id,
        salary,
        language
    )

    print(
        f"\nDeveloper created with name: {name}, "
        f"age: {age}, ID: {employee_id}, "
        f"salary: ₹{salary:.2f}, "
        f"and language: {language}."
    )

    return developer


# ============================================================
# SHOW DETAILS
# ============================================================

def show_details(person, employee, manager, developer):
    """
    Display details of the selected object.
    """
    print("\nChoose details to show:")
    print("1. Person")
    print("2. Employee")
    print("3. Manager")
    print("4. Developer")

    choice = input("Enter your choice: ")

    if choice == "1":

        if person is None:
            print("\nNo person has been created.")
        else:
            print("\nPerson Details:")
            print(f"Name: {person.name}")
            print(f"Age: {person.age}")

    elif choice == "2":

        if employee is None:
            print("\nNo employee has been created.")
        else:
            print()
            employee.display()
            print("\nString Representation:")
            print(employee)

    elif choice == "3":

        if manager is None:
            print("\nNo manager has been created.")
        else:
            print()
            manager.display()
            print("\nString Representation:")
            print(manager)

    elif choice == "4":

        if developer is None:
            print("\nNo developer has been created.")
        else:
            print()
            developer.display()
            print("\nString Representation:")
            print(developer)

    else:
        print("\nInvalid choice.")


# ============================================================
# COMPARE SALARIES
# ============================================================

def compare_salaries(employees):
    """
    Compare salaries of two employees using overloaded operators.
    """

    if len(employees) < 2:
        print("\nAt least two employees are required.")
        return

    print("\nAvailable Employees:")

    for employee_id, employee in employees.items():
        print(
            f"ID: {employee_id} | "
            f"Name: {employee.name} | "
            f"Salary: ₹{employee.get_salary():.2f}"
        )

    first_id = input(
        "\nEnter the first employee's ID: "
    )

    second_id = input(
        "Enter the second employee's ID: "
    )

    if first_id not in employees:
        print("First employee not found.")
        return

    if second_id not in employees:
        print("Second employee not found.")
        return

    first = employees[first_id]
    second = employees[second_id]

    print("\nComparing salaries:")
    print("-" * 40)

    print(
        f"{first.name}: ₹{first.get_salary():.2f}"
    )

    print(
        f"{second.name}: ₹{second.get_salary():.2f}"
    )

    if first > second:
        print(
            f"\n{first.name} has a higher salary."
        )

    elif first < second:
        print(
            f"\n{second.name} has a higher salary."
        )

    else:
        print("\nBoth employees have the same salary.")

    if first == second:
        print("Salary comparison using == : Equal")
    else:
        print("Salary comparison using == : Not Equal")


# ============================================================
# OOP CHECKS
# ============================================================

def demonstrate_oop_features():
    """
    Demonstrate super() and issubclass().
    """

    print("\n--- OOP Feature Demonstration ---")

    print(
        "Manager is subclass of Employee:",
        issubclass(Manager, Employee)
    )

    print(
        "Developer is subclass of Employee:",
        issubclass(Developer, Employee)
    )

    print(
        "Employee is subclass of Manager:",
        issubclass(Employee, Manager)
    )

    print("\nsuper() is used in Manager and Developer constructors")
    print("to initialize attributes inherited from Employee.")


# ============================================================
# MAIN PROGRAM
# ============================================================

employees = {}

person = None
employee = None
manager = None
developer = None

print("=" * 60)
print("        PYTHON OOP PROJECT: EMPLOYEE MANAGEMENT")
print("=" * 60)

while True:

    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Compare Salaries")
    print("7. Demonstrate OOP Features")
    print("8. Update Employee Salary")
    print("9. Exit")

    choice = input("\nEnter your choice: ")

    # --------------------------------------------------------
    # CREATE PERSON
    # --------------------------------------------------------
    if choice == "1":

        person = create_person()

    # --------------------------------------------------------
    # CREATE EMPLOYEE
    # --------------------------------------------------------
    elif choice == "2":

        employee = create_employee()

        employees[
            employee.get_employee_id()
        ] = employee

    # --------------------------------------------------------
    # CREATE MANAGER
    # --------------------------------------------------------
    elif choice == "3":

        manager = create_manager()

        employees[
            manager.get_employee_id()
        ] = manager

    # --------------------------------------------------------
    # CREATE DEVELOPER
    # --------------------------------------------------------
    elif choice == "4":

        developer = create_developer()

        employees[
            developer.get_employee_id()
        ] = developer

    # --------------------------------------------------------
    # SHOW DETAILS
    # --------------------------------------------------------
    elif choice == "5":

        show_details(
            person,
            employee,
            manager,
            developer
        )

    # --------------------------------------------------------
    # COMPARE SALARIES
    # --------------------------------------------------------
    elif choice == "6":

        compare_salaries(employees)

    # --------------------------------------------------------
    # OOP FEATURES
    # --------------------------------------------------------
    elif choice == "7":

        demonstrate_oop_features()

    # --------------------------------------------------------
    # UPDATE SALARY
    # --------------------------------------------------------
    elif choice == "8":

        if not employees:
            print("\nNo employees available.")
            continue

        print("\nAvailable Employees:")

        for employee_id, emp in employees.items():
            print(
                f"{employee_id} - "
                f"{emp.name} - "
                f"₹{emp.get_salary():.2f}"
            )

        employee_id = input(
            "\nEnter Employee ID to update salary: "
        )

        if employee_id not in employees:
            print("Employee not found.")
            continue

        while True:

            try:
                new_salary = float(
                    input("Enter new salary: ")
                )

                if new_salary < 0:
                    print("Salary cannot be negative.")
                    continue

                break

            except ValueError:
                print("Please enter a valid salary.")

        employees[
            employee_id
        ].set_salary(new_salary)

        print(
            f"Salary updated successfully to "
            f"₹{new_salary:.2f}"
        )

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------
    elif choice == "9":

        print("\nExiting the system.")
        print("All resources have been released.")
        print("Goodbye!")

        employees.clear()
        person = None
        employee = None
        manager = None
        developer = None

        break

    # --------------------------------------------------------
    # INVALID CHOICE
    # --------------------------------------------------------
    else:

        print("\nInvalid choice. Please select 1 to 9.")