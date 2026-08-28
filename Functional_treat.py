# ============================================================
# PROJECT: FUNCTIONAL TREAT
# Data Analyzer and Transformer
# ============================================================

dataset_summary = {
    "total": 0,
    "average": 0
}

data = []


# ------------------------------------------------------------
# BUILT-IN FUNCTIONS
# ------------------------------------------------------------
def display_data_summary(values):
    """
    Display basic statistics of the dataset using built-in functions.
    """
    if not values:
        print("\nNo data available.")
        return

    print("\nData Summary:")
    print("-" * 35)
    print("Total elements :", len(values))
    print("Minimum value  :", min(values))
    print("Maximum value  :", max(values))
    print("Sum of values  :", sum(values))
    print("Average value  :", round(sum(values) / len(values), 2))


# ------------------------------------------------------------
# USER-DEFINED FUNCTION
# ------------------------------------------------------------
def calculate_average(values):
    """
    Calculate and return the average of a list.
    """
    if not values:
        return 0

    return sum(values) / len(values)


def find_duplicates(values):
    """
    Find duplicate values from a list.
    """
    duplicates = []

    for value in values:
        if values.count(value) > 1 and value not in duplicates:
            duplicates.append(value)

    return duplicates


def display_unique_values(values):
    """
    Display unique values using a set.
    """
    return set(values)


# ------------------------------------------------------------
# ARGS, KWARGS AND DOC
# ------------------------------------------------------------
def dataset_information(*args, **kwargs):
    """
    Display dataset information using *args and **kwargs.
    """
    print("\nDataset Information:")

    if args:
        print("Values passed using *args:")
        for value in args:
            print(value)

    if kwargs:
        print("\nInformation passed using **kwargs:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")


# ------------------------------------------------------------
# RECURSION
# ------------------------------------------------------------
def factorial(number):
    """
    Calculate factorial of a number using recursion.
    """
    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


def fibonacci(number):
    """
    Calculate Fibonacci number using recursion.
    """
    if number <= 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


# ------------------------------------------------------------
# LAMBDA + MAP + FILTER
# ------------------------------------------------------------
def filter_data(values):
    """
    Filter data using lambda and filter().
    Also uses map() to demonstrate data transformation.
    """

    while True:
        try:
            threshold = float(
                input("\nEnter a threshold value: ")
            )
            break

        except ValueError:
            print("Please enter a valid number.")

    print("\nChoose filtering option:")
    print("1. Values greater than threshold")
    print("2. Values less than threshold")
    print("3. Values greater than or equal to threshold")
    print("4. Values less than or equal to threshold")

    choice = input("Enter your choice: ")

    if choice == "1":
        filtered = list(
            filter(lambda x: x > threshold, values)
        )

    elif choice == "2":
        filtered = list(
            filter(lambda x: x < threshold, values)
        )

    elif choice == "3":
        filtered = list(
            filter(lambda x: x >= threshold, values)
        )

    elif choice == "4":
        filtered = list(
            filter(lambda x: x <= threshold, values)
        )

    else:
        print("Invalid choice.")
        return

    # map() transformation
    transformed = list(
        map(lambda x: x * 1, filtered)
    )

    print("\nFiltered Data:")
    print(transformed)


# ------------------------------------------------------------
# GLOBAL VARIABLE
# ------------------------------------------------------------
def update_global_summary(values):
    """
    Update the global dataset summary variable.
    """
    global dataset_summary

    if values:
        dataset_summary["total"] = len(values)
        dataset_summary["average"] = sum(values) / len(values)
    else:
        dataset_summary["total"] = 0
        dataset_summary["average"] = 0


# ------------------------------------------------------------
# RETURN MULTIPLE VALUES
# ------------------------------------------------------------
def get_statistics(values):
    """
    Return minimum, maximum, sum and average values.
    """
    if not values:
        return 0, 0, 0, 0

    minimum = min(values)
    maximum = max(values)
    total = sum(values)
    average = total / len(values)

    return minimum, maximum, total, average


# ------------------------------------------------------------
# INPUT 1D DATA
# ------------------------------------------------------------
def input_1d_data():
    """
    Accept a one-dimensional list of numbers from the user.
    """
    global data

    while True:
        try:
            values = input(
                "\nEnter data for a 1D array (separated by spaces): "
            )

            data = [float(x) for x in values.split()]

            if not data:
                print("Please enter at least one value.")
                continue

            print("\nData has been stored successfully!")

            update_global_summary(data)

            break

        except ValueError:
            print("Please enter numbers only.")


# ------------------------------------------------------------
# INPUT 2D DATA
# ------------------------------------------------------------
def input_2d_data():
    """
    Accept a two-dimensional list from the user.
    """
    global data

    while True:
        try:
            rows = int(input("\nEnter number of rows: "))
            columns = int(input("Enter number of columns: "))

            if rows <= 0 or columns <= 0:
                print("Rows and columns must be positive.")
                continue

            matrix = []

            for i in range(rows):

                while True:
                    row_input = input(
                        f"Enter {columns} values for row {i + 1}: "
                    )

                    row = [float(x) for x in row_input.split()]

                    if len(row) != columns:
                        print(
                            f"Please enter exactly {columns} values."
                        )
                        continue

                    matrix.append(row)
                    break

            data = matrix

            print("\n2D Data has been stored successfully!")

            break

        except ValueError:
            print("Please enter valid numbers.")


# ------------------------------------------------------------
# DISPLAY 2D ARRAY
# ------------------------------------------------------------
def display_2d_data(matrix):
    """
    Display a two-dimensional list in formatted structure.
    """
    print("\n2D Array:")

    for row in matrix:
        print(row)


# ------------------------------------------------------------
# SORT 1D DATA
# ------------------------------------------------------------
def sort_1d_data(values):
    """
    Sort a one-dimensional list using sort().
    """
    if not values:
        print("\nNo data available.")
        return

    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")

    choice = input("Enter your choice: ")

    sorted_data = values.copy()

    if choice == "1":
        sorted_data.sort()
        print("\nSorted Data in Ascending Order:")
        print(sorted_data)

    elif choice == "2":
        sorted_data.sort(reverse=True)
        print("\nSorted Data in Descending Order:")
        print(sorted_data)

    else:
        print("Invalid choice.")


# ------------------------------------------------------------
# SORT 2D DATA
# ------------------------------------------------------------
def sort_2d_data(matrix):
    """
    Sort rows of a two-dimensional list using sorted().
    """
    if not matrix:
        print("\nNo 2D data available.")
        return

    print("\nChoose sorting option:")
    print("1. Sort rows by first value")
    print("2. Sort rows by sum of values")
    print("3. Reverse row order")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = sorted(matrix, key=lambda row: row[0])

    elif choice == "2":
        result = sorted(matrix, key=lambda row: sum(row))

    elif choice == "3":
        result = sorted(matrix, reverse=True)

    else:
        print("Invalid choice.")
        return

    print("\nSorted 2D Data:")

    for row in result:
        print(row)


# ------------------------------------------------------------
# DISPLAY GLOBAL SUMMARY
# ------------------------------------------------------------
def display_global_summary():
    """
    Display the dataset summary stored using the global keyword.
    """
    print("\nGlobal Dataset Summary:")
    print("-" * 35)
    print("Total values :", dataset_summary["total"])
    print(
        "Overall average :",
        round(dataset_summary["average"], 2)
    )


# ------------------------------------------------------------
# MAIN PROGRAM
# ------------------------------------------------------------
print("=" * 60)
print("       WELCOME TO THE DATA ANALYZER AND")
print("             TRANSFORMER PROGRAM")
print("=" * 60)

while True:

    print("\nMain Menu:")
    print("1. Input 1D Data")
    print("2. Input 2D Data")
    print("3. Display Data Summary (Built-in Functions)")
    print("4. Calculate Factorial (Recursion)")
    print("5. Calculate Fibonacci (Recursion)")
    print("6. Filter Data by Threshold (Lambda)")
    print("7. Display Dataset Information (*args, **kwargs)")
    print("8. Sort 1D Data")
    print("9. Sort 2D Data")
    print("10. Display Dataset Statistics (Return Multiple Values)")
    print("11. Display Global Dataset Summary")
    print("12. Find Duplicate Values")
    print("13. Display Unique Values")
    print("14. Display 2D Data")
    print("15. Exit")

    choice = input("\nPlease enter your choice: ")

    # --------------------------------------------------------
    # INPUT 1D
    # --------------------------------------------------------
    if choice == "1":
        input_1d_data()

    # --------------------------------------------------------
    # INPUT 2D
    # --------------------------------------------------------
    elif choice == "2":
        input_2d_data()

    # --------------------------------------------------------
    # BUILT-IN FUNCTIONS
    # --------------------------------------------------------
    elif choice == "3":

        if data and isinstance(data[0], list):
            flat_data = [
                value
                for row in data
                for value in row
            ]

            display_data_summary(flat_data)

        else:
            display_data_summary(data)

    # --------------------------------------------------------
    # FACTORIAL
    # --------------------------------------------------------
    elif choice == "4":

        while True:
            try:
                number = int(
                    input("\nEnter a number to calculate factorial: ")
                )

                if number < 0:
                    print("Factorial is not defined for negative numbers.")
                    continue

                print(
                    f"\nFactorial of {number} is:",
                    factorial(number)
                )

                break

            except ValueError:
                print("Please enter a valid integer.")

    # --------------------------------------------------------
    # FIBONACCI
    # --------------------------------------------------------
    elif choice == "5":

        while True:
            try:
                number = int(
                    input("\nEnter the Fibonacci position: ")
                )

                if number < 0:
                    print("Please enter a non-negative number.")
                    continue

                print(
                    f"\nFibonacci value at position {number}:",
                    fibonacci(number)
                )

                break

            except ValueError:
                print("Please enter a valid integer.")

    # --------------------------------------------------------
    # LAMBDA FILTER
    # --------------------------------------------------------
    elif choice == "6":

        if data and isinstance(data[0], list):

            flat_data = [
                value
                for row in data
                for value in row
            ]

            filter_data(flat_data)

        elif data:
            filter_data(data)

        else:
            print("\nPlease enter data first.")

    # --------------------------------------------------------
    # ARGS AND KWARGS
    # --------------------------------------------------------
    elif choice == "7":

        if data:

            if isinstance(data[0], list):
                flat_data = [
                    value
                    for row in data
                    for value in row
                ]
            else:
                flat_data = data

            dataset_information(
                *flat_data,
                total=len(flat_data),
                minimum=min(flat_data),
                maximum=max(flat_data),
                average=round(
                    calculate_average(flat_data), 2
                )
            )

        else:
            print("\nPlease enter data first.")

    # --------------------------------------------------------
    # SORT 1D
    # --------------------------------------------------------
    elif choice == "8":

        if data and isinstance(data[0], list):
            print(
                "\nCurrent data is 2D. "
                "Please enter 1D data first."
            )
        elif data:
            sort_1d_data(data)
        else:
            print("\nPlease enter 1D data first.")

    # --------------------------------------------------------
    # SORT 2D
    # --------------------------------------------------------
    elif choice == "9":

        if data and isinstance(data[0], list):
            sort_2d_data(data)
        else:
            print("\nPlease enter 2D data first.")

    # --------------------------------------------------------
    # RETURN MULTIPLE VALUES
    # --------------------------------------------------------
    elif choice == "10":

        if data:

            if isinstance(data[0], list):
                flat_data = [
                    value
                    for row in data
                    for value in row
                ]
            else:
                flat_data = data

            minimum, maximum, total, average = get_statistics(
                flat_data
            )

            print("\nDataset Statistics:")
            print("-" * 35)
            print("Minimum value :", minimum)
            print("Maximum value :", maximum)
            print("Sum of all values :", total)
            print("Average value :", round(average, 2))

        else:
            print("\nPlease enter data first.")

    # --------------------------------------------------------
    # GLOBAL VARIABLE
    # --------------------------------------------------------
    elif choice == "11":

        if data:
            update_global_summary(
                [
                    value
                    for row in data
                    for value in row
                ]
                if isinstance(data[0], list)
                else data
            )

            display_global_summary()

        else:
            print("\nPlease enter data first.")

    # --------------------------------------------------------
    # DUPLICATES
    # --------------------------------------------------------
    elif choice == "12":

        if data:

            if isinstance(data[0], list):
                flat_data = [
                    value
                    for row in data
                    for value in row
                ]
            else:
                flat_data = data

            duplicates = find_duplicates(flat_data)

            if duplicates:
                print("\nDuplicate Values:")
                print(duplicates)
            else:
                print("\nNo duplicate values found.")

        else:
            print("\nPlease enter data first.")

    # --------------------------------------------------------
    # UNIQUE VALUES
    # --------------------------------------------------------
    elif choice == "13":

        if data:

            if isinstance(data[0], list):
                flat_data = [
                    value
                    for row in data
                    for value in row
                ]
            else:
                flat_data = data

            unique_values = display_unique_values(flat_data)

            print("\nUnique Values:")
            print(unique_values)

        else:
            print("\nPlease enter data first.")

    # --------------------------------------------------------
    # DISPLAY 2D
    # --------------------------------------------------------
    elif choice == "14":

        if data and isinstance(data[0], list):
            display_2d_data(data)
        else:
            print("\nPlease enter 2D data first.")

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------
    elif choice == "15":

        print("\nThank you for using the Data Analyzer and")
        print("Transformer Program!")
        print("Exiting the program. Goodbye!")

        break

    # --------------------------------------------------------
    # INVALID CHOICE
    # --------------------------------------------------------
    else:
        print("\nInvalid choice. Please select a valid option.")