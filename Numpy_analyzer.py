import numpy as np


class DataAnalytics:
    """
    NumPy Analyzer class for array creation, mathematical operations,
    searching, sorting, filtering, aggregation, and statistics.
    """

    total_arrays_created = 0

    def __init__(self, array=None):
        """
        Initialize the DataAnalytics object with a NumPy array.
        """
        self.array = array
        DataAnalytics.total_arrays_created += 1

    # ========================================================
    # ARRAY CREATION
    # ========================================================

    def create_array(self, dimensions):
        """
        Create a 1D, 2D, or 3D NumPy array based on user input.
        """

        if dimensions == 1:
            while True:
                try:
                    values = input(
                        "Enter elements separated by space: "
                    )
                    self.array = np.array(
                        [float(x) for x in values.split()]
                    )

                    if self.array.size == 0:
                        print("Array cannot be empty.")
                        continue

                    break

                except ValueError:
                    print("Please enter valid numbers.")

        elif dimensions == 2:
            while True:
                try:
                    rows = int(input("Enter number of rows: "))
                    columns = int(input("Enter number of columns: "))

                    if rows <= 0 or columns <= 0:
                        print("Rows and columns must be positive.")
                        continue

                    values = input(
                        f"Enter {rows * columns} elements separated by space: "
                    )

                    numbers = [
                        float(x) for x in values.split()
                    ]

                    if len(numbers) != rows * columns:
                        print(
                            f"Please enter exactly "
                            f"{rows * columns} elements."
                        )
                        continue

                    self.array = np.array(numbers).reshape(
                        rows, columns
                    )

                    break

                except ValueError:
                    print("Please enter valid numbers.")

        elif dimensions == 3:
            while True:
                try:
                    layers = int(input("Enter number of layers: "))
                    rows = int(input("Enter number of rows: "))
                    columns = int(input("Enter number of columns: "))

                    if layers <= 0 or rows <= 0 or columns <= 0:
                        print("All dimensions must be positive.")
                        continue

                    total = layers * rows * columns

                    values = input(
                        f"Enter {total} elements separated by space: "
                    )

                    numbers = [
                        float(x) for x in values.split()
                    ]

                    if len(numbers) != total:
                        print(
                            f"Please enter exactly {total} elements."
                        )
                        continue

                    self.array = np.array(numbers).reshape(
                        layers, rows, columns
                    )

                    break

                except ValueError:
                    print("Please enter valid numbers.")

        else:
            print("Invalid dimension.")

        if self.array is not None:
            print("\nArray created successfully:")
            print(self.array)

    # ========================================================
    # INDEXING
    # ========================================================

    def indexing(self):
        """
        Demonstrate indexing for NumPy arrays.
        """

        if self.array is None:
            print("Please create an array first.")
            return

        print("\nArray:")
        print(self.array)

        if self.array.ndim == 1:

            try:
                index = int(input("Enter index: "))
                print("Value:", self.array[index])
            except (ValueError, IndexError):
                print("Invalid index.")

        else:

            try:
                row = int(input("Enter row index: "))
                column = int(input("Enter column index: "))

                print(
                    "Value:",
                    self.array[row, column]
                )

            except (ValueError, IndexError):
                print("Invalid index.")

    # ========================================================
    # SLICING
    # ========================================================

    def slicing(self):
        """
        Demonstrate slicing of a NumPy array.
        """

        if self.array is None:
            print("Please create an array first.")
            return

        print("\nOriginal Array:")
        print(self.array)

        if self.array.ndim == 1:

            try:
                start = int(
                    input("Enter start index: ")
                )
                end = int(
                    input("Enter end index: ")
                )

                print(
                    "\nSliced Array:",
                    self.array[start:end]
                )

            except ValueError:
                print("Please enter valid indices.")

        else:

            try:
                row_start = int(
                    input("Enter row start index: ")
                )
                row_end = int(
                    input("Enter row end index: ")
                )

                col_start = int(
                    input("Enter column start index: ")
                )
                col_end = int(
                    input("Enter column end index: ")
                )

                print("\nSliced Array:")
                print(
                    self.array[
                        row_start:row_end,
                        col_start:col_end
                    ]
                )

            except ValueError:
                print("Please enter valid indices.")

    # ========================================================
    # MATHEMATICAL OPERATIONS
    # ========================================================

    def mathematical_operations(self):
        """
        Perform element-wise addition, subtraction,
        multiplication, and division.
        """

        if self.array is None:
            print("Please create an array first.")
            return

        if self.array.ndim != 1:
            print(
                "Mathematical operations in this menu "
                "require a 1D array."
            )
            return

        while True:

            print("\nChoose a mathematical operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Matrix Multiplication")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "6":
                break

            if choice not in ["1", "2", "3", "4", "5"]:
                print("Invalid choice.")
                continue

            try:

                values = input(
                    f"Enter {self.array.size} elements "
                    f"separated by space: "
                )

                numbers = [
                    float(x) for x in values.split()
                ]

                if len(numbers) != self.array.size:
                    print(
                        f"Please enter exactly "
                        f"{self.array.size} elements."
                    )
                    continue

                second_array = np.array(numbers)

                print("\nOriginal Array:")
                print(self.array)

                print("\nSecond Array:")
                print(second_array)

                if choice == "1":
                    result = self.array + second_array
                    print("\nResult of Addition:")
                    print(result)

                elif choice == "2":
                    result = self.array - second_array
                    print("\nResult of Subtraction:")
                    print(result)

                elif choice == "3":
                    result = self.array * second_array
                    print("\nResult of Multiplication:")
                    print(result)

                elif choice == "4":

                    if np.any(second_array == 0):
                        print(
                            "Division by zero is not allowed."
                        )
                        continue

                    result = self.array / second_array

                    print("\nResult of Division:")
                    print(result)

                elif choice == "5":

                    print(
                        "Matrix multiplication requires "
                        "2D arrays."
                    )

            except ValueError:
                print("Please enter valid numbers.")

    # ========================================================
    # MATRIX MULTIPLICATION
    # ========================================================

    def matrix_multiplication(self):
        """
        Calculate the matrix product of two 2D arrays.
        """

        if self.array is None:
            print("Please create an array first.")
            return

        if self.array.ndim != 2:
            print(
                "Current array must be 2D for matrix multiplication."
            )
            return

        print("\nFirst Matrix:")
        print(self.array)

        rows = int(
            input("Enter rows of second matrix: ")
        )

        columns = int(
            input("Enter columns of second matrix: ")
        )

        if self.array.shape[1] != rows:
            print(
                "Matrix multiplication is not possible."
            )
            print(
                "Columns of first matrix must equal "
                "rows of second matrix."
            )
            return

        values = input(
            f"Enter {rows * columns} elements: "
        )

        numbers = [
            float(x) for x in values.split()
        ]

        if len(numbers) != rows * columns:
            print("Invalid number of elements.")
            return

        second_array = np.array(numbers).reshape(
            rows, columns
        )

        result = np.dot(
            self.array,
            second_array
        )

        print("\nSecond Matrix:")
        print(second_array)

        print("\nMatrix Product:")
        print(result)

    # ========================================================
    # COMBINE ARRAYS
    # ========================================================

    def combine_arrays(self):
        """
        Combine two arrays using NumPy vstack.
        """

        if self.array is None:
            print("Please create an array first.")
            return

        if self.array.ndim != 2:
            print(
                "Combining requires a 2D array."
            )
            return

        rows, columns = self.array.shape

        print(
            f"\nCurrent array has {rows * columns} elements."
        )

        values = input(
            f"Enter {rows * columns} elements "
            f"for another array: "
        )

        numbers = [
            float(x) for x in values.split()
        ]

        if len(numbers) != rows * columns:
            print(
                f"Please enter exactly "
                f"{rows * columns} elements."
            )
            return

        second_array = np.array(numbers).reshape(
            rows, columns
        )

        combined = np.vstack(
            (self.array, second_array)
        )

        print("\nOriginal Array:")
        print(self.array)

        print("\nSecond Array:")
        print(second_array)

        print("\nCombined Array (Vertical Stack):")
        print(combined)

    # ========================================================
    # SPLIT ARRAY
    # ========================================================

    def split_array(self):
        """
        Split a NumPy array into smaller arrays.
        """

        if self.array is None:
            print("Please create an array first.")
            return

        print("\nOriginal Array:")
        print(self.array)

        try:
            parts = int(
                input("Enter number of parts: ")
            )

            if parts <= 0:
                print("Number of parts must be positive.")
                return

            result = np.array_split(
                self.array,
                parts
            )

            print("\nSplit Arrays:")

            for i, part in enumerate(result, start=1):
                print(f"\nPart {i}:")
                print(part)

        except ValueError:
            print("Please enter a valid number.")

    # ========================================================
    # SEARCH
    # ========================================================

    def search_value(self):
        """
        Search for a specific value in the array.
        """

        if self.array is None:
            print("Please create an array first.")
            return

        try:
            value = float(
                input("Enter value to search: ")
            )

            positions = np.argwhere(
                self.array == value
            )

            if positions.size > 0:

                print(
                    f"\nValue {value} found."
                )

                print("Positions:")

                for position in positions:
                    print(tuple(position))

            else:
                print(
                    f"\nValue {value} not found."
                )

        except ValueError:
            print("Please enter a valid number.")

    # ========================================================
    # SORT
    # ========================================================

    def sort_array(self):
        """
        Sort array in ascending or descending order.
        """

        if self.array is None:
            print("Please create an array first.")
            return

        print("\nOriginal Array:")
        print(self.array)

        print("\nChoose sorting option:")
        print("1. Ascending")
        print("2. Descending")

        choice = input("Enter your choice: ")

        if self.array.ndim == 1:

            if choice == "1":
                result = np.sort(self.array)

            elif choice == "2":
                result = np.sort(
                    self.array
                )[::-1]

            else:
                print("Invalid choice.")
                return

        else:

            if choice == "1":
                result = np.sort(
                    self.array,
                    axis=-1
                )

            elif choice == "2":
                result = np.sort(
                    self.array,
                    axis=-1
                )[:, ::-1]

            else:
                print("Invalid choice.")
                return

        print("\nSorted Array:")
        print(result)

    # ========================================================
    # FILTER
    # ========================================================

    def filter_array(self):
        """
        Filter array values using a user-defined condition.
        """

        if self.array is None:
            print("Please create an array first.")
            return

        try:
            threshold = float(
                input("Enter threshold value: ")
            )

        except ValueError:
            print("Please enter a valid number.")
            return

        print("\nChoose condition:")
        print("1. Greater than")
        print("2. Less than")
        print("3. Greater than or equal")
        print("4. Less than or equal")
        print("5. Equal to")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = self.array[
                self.array > threshold
            ]

        elif choice == "2":
            result = self.array[
                self.array < threshold
            ]

        elif choice == "3":
            result = self.array[
                self.array >= threshold
            ]

        elif choice == "4":
            result = self.array[
                self.array <= threshold
            ]

        elif choice == "5":
            result = self.array[
                self.array == threshold
            ]

        else:
            print("Invalid choice.")
            return

        print("\nFiltered Values:")
        print(result)

    # ========================================================
    # AGGREGATE FUNCTIONS
    # ========================================================

    def aggregate_functions(self):
        """
        Calculate sum, mean, median, standard deviation,
        and variance.
        """

        if self.array is None:
            print("Please create an array first.")
            return

        print("\nOriginal Array:")
        print(self.array)

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")

        choice = input("Enter your choice: ")

        if choice == "1":
            result = np.sum(self.array)
            name = "Sum"

        elif choice == "2":
            result = np.mean(self.array)
            name = "Mean"

        elif choice == "3":
            result = np.median(self.array)
            name = "Median"

        elif choice == "4":
            result = np.std(self.array)
            name = "Standard Deviation"

        elif choice == "5":
            result = np.var(self.array)
            name = "Variance"

        else:
            print("Invalid choice.")
            return

        print(
            f"\n{name} of Array: "
            f"{result:.2f}"
        )

    # ========================================================
    # STATISTICAL FUNCTIONS
    # ========================================================

    def statistics(self):
        """
        Calculate minimum, maximum, percentiles,
        and correlation coefficient.
        """

        if self.array is None:
            print("Please create an array first.")
            return

        print("\nStatistical Analysis:")
        print("-" * 40)

        print(
            "Minimum:",
            np.min(self.array)
        )

        print(
            "Maximum:",
            np.max(self.array)
        )

        print(
            "25th Percentile:",
            np.percentile(self.array, 25)
        )

        print(
            "50th Percentile:",
            np.percentile(self.array, 50)
        )

        print(
            "75th Percentile:",
            np.percentile(self.array, 75)
        )

        print(
            "90th Percentile:",
            np.percentile(self.array, 90)
        )

        if self.array.ndim == 1 and self.array.size >= 2:

            correlation = np.corrcoef(
                self.array,
                np.arange(self.array.size)
            )[0, 1]

            print(
                "Correlation with index:",
                round(float(correlation), 4)
            )

        elif self.array.ndim == 2 and self.array.shape[0] >= 2:

            correlation = np.corrcoef(
                self.array,
                rowvar=False
            )

            print("\nCorrelation Coefficient Matrix:")
            print(correlation)

        else:
            print(
                "\nCorrelation requires sufficient data."
            )

    # ========================================================
    # INDEX AND SLICE MENU
    # ========================================================

    def indexing_slicing_menu(self):
        """
        Provide indexing and slicing operations.
        """

        while True:

            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.indexing()

            elif choice == "2":
                self.slicing()

            elif choice == "3":
                break

            else:
                print("Invalid choice.")

    # ========================================================
    # CLASS METHOD
    # ========================================================

    @classmethod
    def array_count(cls):
        """
        Return the number of DataAnalytics objects created.
        """
        return cls.total_arrays_created

    # ========================================================
    # STATIC METHOD
    # ========================================================

    @staticmethod
    def is_numpy_array(value):
        """
        Check whether a value is a NumPy array.
        """
        return isinstance(value, np.ndarray)


# ============================================================
# MAIN PROGRAM
# ============================================================

print("=" * 60)
print("              WELCOME TO THE NUMPY ANALYZER")
print("=" * 60)

analyzer = DataAnalytics()

while True:

    print("\n" + "=" * 60)
    print("Main Menu")
    print("=" * 60)

    print("1. Create a NumPy Array")
    print("2. Indexing and Slicing")
    print("3. Perform Mathematical Operations")
    print("4. Matrix Multiplication")
    print("5. Combine Arrays")
    print("6. Split Arrays")
    print("7. Search, Sort, or Filter Arrays")
    print("8. Compute Aggregates and Statistics")
    print("9. Display OOP Information")
    print("10. Exit")

    choice = input("\nEnter your choice: ")

    # --------------------------------------------------------
    # CREATE ARRAY
    # --------------------------------------------------------

    if choice == "1":

        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        array_type = input("Enter your choice: ")

        if array_type == "1":
            analyzer.create_array(1)

        elif array_type == "2":
            analyzer.create_array(2)

        elif array_type == "3":
            analyzer.create_array(3)

        else:
            print("Invalid choice.")

    # --------------------------------------------------------
    # INDEXING / SLICING
    # --------------------------------------------------------

    elif choice == "2":

        analyzer.indexing_slicing_menu()

    # --------------------------------------------------------
    # MATHEMATICAL OPERATIONS
    # --------------------------------------------------------

    elif choice == "3":

        analyzer.mathematical_operations()

    # --------------------------------------------------------
    # MATRIX MULTIPLICATION
    # --------------------------------------------------------

    elif choice == "4":

        analyzer.matrix_multiplication()

    # --------------------------------------------------------
    # COMBINE ARRAYS
    # --------------------------------------------------------

    elif choice == "5":

        analyzer.combine_arrays()

    # --------------------------------------------------------
    # SPLIT ARRAYS
    # --------------------------------------------------------

    elif choice == "6":

        analyzer.split_array()

    # --------------------------------------------------------
    # SEARCH / SORT / FILTER
    # --------------------------------------------------------

    elif choice == "7":

        while True:

            print("\nSearch, Sort, and Filter:")
            print("1. Search a Value")
            print("2. Sort the Array")
            print("3. Filter Values")
            print("4. Go Back")

            sub_choice = input(
                "Enter your choice: "
            )

            if sub_choice == "1":
                analyzer.search_value()

            elif sub_choice == "2":
                analyzer.sort_array()

            elif sub_choice == "3":
                analyzer.filter_array()

            elif sub_choice == "4":
                break

            else:
                print("Invalid choice.")

    # --------------------------------------------------------
    # AGGREGATES / STATISTICS
    # --------------------------------------------------------

    elif choice == "8":

        while True:

            print("\nAggregates and Statistics:")
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. Statistical Analysis")
            print("7. Go Back")

            sub_choice = input(
                "Enter your choice: "
            )

            if sub_choice in ["1", "2", "3", "4", "5"]:
                analyzer.aggregate_functions()

            elif sub_choice == "6":
                analyzer.statistics()

            elif sub_choice == "7":
                break

            else:
                print("Invalid choice.")

    # --------------------------------------------------------
    # OOP INFORMATION
    # --------------------------------------------------------

    elif choice == "9":

        print("\n--- OOP Information ---")

        print(
            "Current array type:",
            type(analyzer.array)
        )

        print(
            "Current array dimensions:",
            analyzer.array.ndim
            if analyzer.array is not None
            else "No array"
        )

        print(
            "DataAnalytics objects created:",
            DataAnalytics.array_count()
        )

        print(
            "Is current object a NumPy array:",
            DataAnalytics.is_numpy_array(
                analyzer.array
            )
        )

        print("\nPrivate-style encapsulation is provided")
        print("through class attributes and methods.")

    # --------------------------------------------------------
    # EXIT
    # --------------------------------------------------------

    elif choice == "10":

        print("\nThank you for using the NumPy Analyzer!")
        print("Goodbye!")

        break

    # --------------------------------------------------------
    # INVALID MAIN MENU CHOICE
    # --------------------------------------------------------

    else:

        print(
            "\nInvalid choice. "
            "Please select an option from 1 to 10."
        )