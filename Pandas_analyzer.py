import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SalesDataAnalyzer:
    """
    Sales Data Analysis and Visualization System.

    This class provides methods for:
    - Loading and exploring sales data
    - Cleaning missing data
    - DataFrame operations
    - NumPy operations
    - Searching, sorting and filtering
    - Aggregation and statistics
    - Pivot tables and groupby
    - Matplotlib visualizations
    - Seaborn visualizations
    """

    def __init__(self, file_path=None):
        """
        Initialize the SalesDataAnalyzer.
        """
        self.data = pd.DataFrame()

        if file_path:
            self.load_data(file_path)

    def __del__(self):
        """
        Destructor for cleaning resources.
        """
        pass

    # =========================================================
    # DATA LOADING
    # =========================================================

    def load_data(self, file_path):
        """
        Load sales data from a CSV file.
        """
        try:
            self.data = pd.read_csv(file_path)

            print("\nDataset loaded successfully!")
            print(f"Rows    : {self.data.shape[0]}")
            print(f"Columns : {self.data.shape[1]}")

        except FileNotFoundError:
            print("\nFile not found.")
            print("Please check the CSV file path.")

        except Exception as e:
            print("\nError while loading dataset:", e)

    # =========================================================
    # EXPLORE DATA
    # =========================================================

    def explore_data(self):
        """
        Display basic information about the dataset.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        while True:

            print("\n========== EXPLORE DATA ==========")
            print("1. Display First 5 Rows")
            print("2. Display Last 5 Rows")
            print("3. Display Column Names")
            print("4. Display Data Types")
            print("5. Display Basic Information")
            print("6. Display Statistical Description")
            print("7. Display Shape")
            print("8. Display Unique Values")
            print("9. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("\nFirst 5 Rows:")
                print(self.data.head())

            elif choice == "2":
                print("\nLast 5 Rows:")
                print(self.data.tail())

            elif choice == "3":
                print("\nColumn Names:")
                for column in self.data.columns:
                    print("-", column)

            elif choice == "4":
                print("\nData Types:")
                print(self.data.dtypes)

            elif choice == "5":
                print("\nDataset Information:")
                self.data.info()

            elif choice == "6":
                print("\nStatistical Description:")
                print(self.data.describe(include="all"))

            elif choice == "7":
                print("\nDataset Shape:")
                print(
                    f"Rows: {self.data.shape[0]}, "
                    f"Columns: {self.data.shape[1]}"
                )

            elif choice == "8":
                print("\nUnique Values:")

                for column in self.data.columns:
                    print(
                        f"\n{column}:",
                        self.data[column].unique()
                    )

            elif choice == "9":
                break

            else:
                print("Invalid choice.")

    # =========================================================
    # MISSING DATA
    # =========================================================

    def handle_missing_data(self):
        """
        Identify and handle missing values.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        print("\nMissing Values:")
        print(self.data.isnull().sum())

        print("\nChoose an option:")
        print("1. Display Rows With Missing Values")
        print("2. Fill Missing Numeric Values With Mean")
        print("3. Drop Rows With Missing Values")
        print("4. Replace Missing Values With Specific Value")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            missing_rows = self.data[
                self.data.isnull().any(axis=1)
            ]

            if missing_rows.empty:
                print("\nNo missing values found.")

            else:
                print("\nRows containing missing values:")
                print(missing_rows)

        elif choice == "2":

            numeric_columns = self.data.select_dtypes(
                include=np.number
            ).columns

            for column in numeric_columns:
                self.data[column] = self.data[column].fillna(
                    self.data[column].mean()
                )

            print("\nMissing numeric values filled with mean.")

        elif choice == "3":

            before = len(self.data)

            self.data.dropna(inplace=True)

            after = len(self.data)

            print(
                f"\nRemoved {before - after} rows."
            )

        elif choice == "4":

            value = input(
                "Enter value to replace missing values: "
            )

            self.data.fillna(value, inplace=True)

            print("\nMissing values replaced successfully.")

        elif choice == "5":
            return

        else:
            print("Invalid choice.")

    # =========================================================
    # NUMPY ARRAY OPERATIONS
    # =========================================================

    def numpy_operations(self):
        """
        Convert numeric DataFrame columns to NumPy arrays
        and demonstrate indexing, slicing and mathematical operations.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        numeric_data = self.data.select_dtypes(
            include=np.number
        )

        if numeric_data.empty:
            print("\nNo numeric columns available.")
            return

        array = numeric_data.to_numpy()

        print("\nNumeric NumPy Array:")
        print(array)

        print("\nArray Shape:", array.shape)
        print("Array Dimensions:", array.ndim)
        print("Array Size:", array.size)

        if array.ndim == 2:

            print("\nFirst Row:")
            print(array[0])

            print("\nFirst Column:")
            print(array[:, 0])

            print("\nFirst 2 Rows:")
            print(array[:2])

            print("\nFirst 2 Columns:")
            print(array[:, :2])

            if array.shape[1] >= 2:

                print("\nElement-wise Addition:")
                print(array[:, 0] + array[:, 1])

                print("\nElement-wise Multiplication:")
                print(array[:, 0] * array[:, 1])

    # =========================================================
    # DATAFRAME OPERATIONS
    # =========================================================

    def dataframe_operations(self):
        """
        Perform common Pandas DataFrame operations.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        while True:

            print("\n========== DATAFRAME OPERATIONS ==========")
            print("1. Select Columns")
            print("2. Add Calculated Column")
            print("3. Rename Column")
            print("4. Drop Column")
            print("5. Group By")
            print("6. Merge With Another CSV")
            print("7. Sort Data")
            print("8. Back")

            choice = input("Enter your choice: ")

            if choice == "1":

                print("\nAvailable columns:")
                print(list(self.data.columns))

                columns = input(
                    "Enter columns separated by comma: "
                ).split(",")

                columns = [
                    column.strip()
                    for column in columns
                ]

                valid_columns = [
                    column
                    for column in columns
                    if column in self.data.columns
                ]

                if valid_columns:
                    print(
                        self.data[valid_columns].head()
                    )

                else:
                    print("No valid columns selected.")

            elif choice == "2":

                numeric_columns = list(
                    self.data.select_dtypes(
                        include=np.number
                    ).columns
                )

                print(
                    "\nNumeric columns:",
                    numeric_columns
                )

                if len(numeric_columns) >= 2:

                    col1 = input(
                        "Enter first numeric column: "
                    )

                    col2 = input(
                        "Enter second numeric column: "
                    )

                    if (
                        col1 in self.data.columns
                        and col2 in self.data.columns
                    ):

                        new_column = input(
                            "Enter name for new column: "
                        )

                        self.data[new_column] = (
                            self.data[col1]
                            + self.data[col2]
                        )

                        print(
                            "\nCalculated column created."
                        )

                    else:
                        print("Invalid columns.")

                else:
                    print(
                        "At least two numeric columns are required."
                    )

            elif choice == "3":

                print(
                    "\nColumns:",
                    list(self.data.columns)
                )

                old_name = input(
                    "Enter column name to rename: "
                )

                if old_name in self.data.columns:

                    new_name = input(
                        "Enter new column name: "
                    )

                    self.data.rename(
                        columns={
                            old_name: new_name
                        },
                        inplace=True
                    )

                    print(
                        "\nColumn renamed successfully."
                    )

                else:
                    print("Column not found.")

            elif choice == "4":

                print(
                    "\nColumns:",
                    list(self.data.columns)
                )

                column = input(
                    "Enter column to delete: "
                )

                if column in self.data.columns:

                    self.data.drop(
                        columns=[column],
                        inplace=True
                    )

                    print(
                        "\nColumn deleted successfully."
                    )

                else:
                    print("Column not found.")

            elif choice == "5":

                print(
                    "\nColumns:",
                    list(self.data.columns)
                )

                column = input(
                    "Enter column to group by: "
                )

                if column in self.data.columns:

                    numeric_columns = self.data.select_dtypes(
                        include=np.number
                    ).columns

                    if len(numeric_columns) > 0:

                        print(
                            self.data.groupby(column)[
                                numeric_columns
                            ].sum()
                        )

                    else:
                        print(
                            "No numeric columns available."
                        )

                else:
                    print("Column not found.")

            elif choice == "6":

                path = input(
                    "Enter path of another CSV file: "
                )

                try:

                    other_data = pd.read_csv(path)

                    print(
                        "\nSecond dataset columns:"
                    )
                    print(list(other_data.columns))

                    common_columns = list(
                        set(self.data.columns)
                        & set(other_data.columns)
                    )

                    if common_columns:

                        print(
                            "Common columns:",
                            common_columns
                        )

                        key = input(
                            "Enter column to merge on: "
                        )

                        if (
                            key in self.data.columns
                            and key in other_data.columns
                        ):

                            self.data = pd.merge(
                                self.data,
                                other_data,
                                on=key,
                                how="inner"
                            )

                            print(
                                "\nDataFrames merged successfully."
                            )

                        else:
                            print(
                                "Invalid merge column."
                            )

                    else:
                        print(
                            "No common columns found."
                        )

                except Exception as e:
                    print(
                        "Error while merging:",
                        e
                    )

            elif choice == "7":

                print(
                    "\nColumns:",
                    list(self.data.columns)
                )

                column = input(
                    "Enter column to sort by: "
                )

                if column in self.data.columns:

                    print("1. Ascending")
                    print("2. Descending")

                    order = input(
                        "Enter choice: "
                    )

                    if order == "1":

                        self.data = self.data.sort_values(
                            by=column,
                            ascending=True
                        )

                    elif order == "2":

                        self.data = self.data.sort_values(
                            by=column,
                            ascending=False
                        )

                    else:
                        print("Invalid choice.")
                        continue

                    print(
                        "\nSorted Data:"
                    )
                    print(self.data.head())

                else:
                    print("Column not found.")

            elif choice == "8":
                break

            else:
                print("Invalid choice.")

    # =========================================================
    # SEARCH, SORT AND FILTER
    # =========================================================

    def search_sort_filter(self):
        """
        Search, sort and filter sales records.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        while True:

            print("\n========== SEARCH, SORT & FILTER ==========")
            print("1. Search a Value")
            print("2. Sort Data")
            print("3. Filter Data")
            print("4. Back")

            choice = input("Enter your choice: ")

            if choice == "1":

                print(
                    "\nColumns:",
                    list(self.data.columns)
                )

                column = input(
                    "Enter column to search: "
                )

                if column not in self.data.columns:
                    print("Column not found.")
                    continue

                value = input(
                    "Enter value to search: "
                )

                result = self.data[
                    self.data[column].astype(str).str.contains(
                        value,
                        case=False,
                        na=False
                    )
                ]

                if result.empty:
                    print("\nNo matching records found.")

                else:
                    print("\nSearch Results:")
                    print(result)

            elif choice == "2":

                print(
                    "\nColumns:",
                    list(self.data.columns)
                )

                column = input(
                    "Enter column to sort: "
                )

                if column not in self.data.columns:
                    print("Column not found.")
                    continue

                print("1. Ascending")
                print("2. Descending")

                order = input(
                    "Enter choice: "
                )

                if order == "1":
                    result = self.data.sort_values(
                        by=column,
                        ascending=True
                    )

                elif order == "2":
                    result = self.data.sort_values(
                        by=column,
                        ascending=False
                    )

                else:
                    print("Invalid choice.")
                    continue

                print("\nSorted Data:")
                print(result.head(20))

            elif choice == "3":

                print(
                    "\nNumeric columns:",
                    list(
                        self.data.select_dtypes(
                            include=np.number
                        ).columns
                    )
                )

                column = input(
                    "Enter numeric column to filter: "
                )

                if column not in self.data.columns:
                    print("Column not found.")
                    continue

                try:

                    threshold = float(
                        input(
                            "Enter threshold value: "
                        )
                    )

                except ValueError:
                    print("Invalid number.")
                    continue

                print("\nChoose condition:")
                print("1. Greater than")
                print("2. Less than")
                print("3. Greater than or equal")
                print("4. Less than or equal")
                print("5. Equal")

                condition = input(
                    "Enter choice: "
                )

                if condition == "1":

                    result = self.data[
                        self.data[column] > threshold
                    ]

                elif condition == "2":

                    result = self.data[
                        self.data[column] < threshold
                    ]

                elif condition == "3":

                    result = self.data[
                        self.data[column] >= threshold
                    ]

                elif condition == "4":

                    result = self.data[
                        self.data[column] <= threshold
                    ]

                elif condition == "5":

                    result = self.data[
                        self.data[column] == threshold
                    ]

                else:
                    print("Invalid condition.")
                    continue

                print("\nFiltered Data:")
                print(result)

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

    # =========================================================
    # AGGREGATE FUNCTIONS
    # =========================================================

    def aggregate_functions(self):
        """
        Apply aggregation functions such as sum, mean and count.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        numeric_data = self.data.select_dtypes(
            include=np.number
        )

        if numeric_data.empty:
            print(
                "\nNo numeric columns available."
            )
            return

        print("\n========== AGGREGATE FUNCTIONS ==========")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Minimum")
        print("5. Maximum")
        print("6. Count")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            print("\nSum:")
            print(numeric_data.sum())

        elif choice == "2":

            print("\nMean:")
            print(numeric_data.mean())

        elif choice == "3":

            print("\nMedian:")
            print(numeric_data.median())

        elif choice == "4":

            print("\nMinimum:")
            print(numeric_data.min())

        elif choice == "5":

            print("\nMaximum:")
            print(numeric_data.max())

        elif choice == "6":

            print("\nCount:")
            print(numeric_data.count())

        else:
            print("Invalid choice.")

    # =========================================================
    # STATISTICAL ANALYSIS
    # =========================================================

    def statistical_analysis(self):
        """
        Calculate standard deviation, variance and percentiles.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        numeric_data = self.data.select_dtypes(
            include=np.number
        )

        if numeric_data.empty:
            print(
                "\nNo numeric columns available."
            )
            return

        print("\n========== STATISTICAL ANALYSIS ==========")

        print("\nStandard Deviation:")
        print(numeric_data.std())

        print("\nVariance:")
        print(numeric_data.var())

        print("\n25th Percentile:")
        print(numeric_data.quantile(0.25))

        print("\n50th Percentile:")
        print(numeric_data.quantile(0.50))

        print("\n75th Percentile:")
        print(numeric_data.quantile(0.75))

        print("\n90th Percentile:")
        print(numeric_data.quantile(0.90))

        print("\nComplete Statistics:")
        print(numeric_data.describe())

    # =========================================================
    # PIVOT TABLE
    # =========================================================

    def create_pivot_table(self):
        """
        Create a pivot table for data summarization.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        print(
            "\nAvailable columns:",
            list(self.data.columns)
        )

        index_column = input(
            "Enter index/group column: "
        )

        value_column = input(
            "Enter numeric value column: "
        )

        if (
            index_column not in self.data.columns
            or value_column not in self.data.columns
        ):
            print("Invalid columns.")
            return

        pivot = pd.pivot_table(
            self.data,
            index=index_column,
            values=value_column,
            aggfunc=["sum", "mean", "count"]
        )

        print("\nPivot Table:")
        print(pivot)

    # =========================================================
    # GROUPBY TRANSFORM
    # =========================================================

    def groupby_transform(self):
        """
        Demonstrate groupby() and transform().
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        print(
            "\nAvailable columns:",
            list(self.data.columns)
        )

        group_column = input(
            "Enter grouping column: "
        )

        numeric_columns = list(
            self.data.select_dtypes(
                include=np.number
            ).columns
        )

        if group_column not in self.data.columns:
            print("Column not found.")
            return

        if not numeric_columns:
            print(
                "No numeric columns available."
            )
            return

        value_column = input(
            "Enter numeric column: "
        )

        if value_column not in numeric_columns:
            print("Invalid numeric column.")
            return

        self.data[
            f"{value_column}_group_mean"
        ] = self.data.groupby(
            group_column
        )[value_column].transform("mean")

        print(
            "\nData after groupby transform:"
        )
        print(self.data.head())

    # =========================================================
    # MATPLOTLIB VISUALIZATION
    # =========================================================

    def visualize_matplotlib(self):
        """
        Create various Matplotlib visualizations.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        while True:

            print("\n========== MATPLOTLIB VISUALIZATION ==========")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Box Plot")
            print("6. Histogram")
            print("7. Violin Plot")
            print("8. Stack Plot")
            print("9. Step Chart")
            print("10. Multiple Plots")
            print("11. Back")

            choice = input(
                "Enter your choice: "
            )

            if choice == "11":
                break

            numeric_columns = list(
                self.data.select_dtypes(
                    include=np.number
                ).columns
            )

            if choice == "1":

                if len(self.data.columns) < 2:
                    print("Not enough columns.")
                    continue

                x_column = input(
                    "Enter x-axis column name: "
                )

                y_column = input(
                    "Enter y-axis column name: "
                )

                if (
                    x_column not in self.data.columns
                    or y_column not in self.data.columns
                ):
                    print("Invalid columns.")
                    continue

                plt.figure(figsize=(9, 5))

                plt.bar(
                    self.data[x_column].astype(str),
                    self.data[y_column]
                )

                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(
                    f"{y_column} by {x_column}"
                )
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            elif choice == "2":

                x_column = input(
                    "Enter x-axis column name: "
                )

                y_column = input(
                    "Enter y-axis column name: "
                )

                if (
                    x_column not in self.data.columns
                    or y_column not in self.data.columns
                ):
                    print("Invalid columns.")
                    continue

                plt.figure(figsize=(9, 5))

                plt.plot(
                    self.data[x_column],
                    self.data[y_column],
                    marker="o"
                )

                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(
                    f"{y_column} Trend"
                )
                plt.grid(True)
                plt.tight_layout()
                plt.show()

            elif choice == "3":

                x_column = input(
                    "Enter x-axis column name: "
                )

                y_column = input(
                    "Enter y-axis column name: "
                )

                if (
                    x_column not in self.data.columns
                    or y_column not in self.data.columns
                ):
                    print("Invalid columns.")
                    continue

                plt.figure(figsize=(9, 5))

                plt.scatter(
                    self.data[x_column],
                    self.data[y_column]
                )

                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(
                    f"{x_column} vs {y_column}"
                )
                plt.tight_layout()
                plt.show()

            elif choice == "4":

                if len(numeric_columns) == 0:
                    print("No numeric columns.")
                    continue

                column = input(
                    "Enter numeric column for pie chart: "
                )

                if column not in numeric_columns:
                    print("Invalid column.")
                    continue

                values = self.data[column]

                plt.figure(figsize=(7, 7))

                plt.pie(
                    values,
                    labels=self.data.index,
                    autopct="%1.1f%%"
                )

                plt.title(
                    f"Distribution of {column}"
                )

                plt.tight_layout()
                plt.show()

            elif choice == "5":

                if not numeric_columns:
                    print("No numeric columns.")
                    continue

                column = input(
                    "Enter numeric column: "
                )

                if column not in numeric_columns:
                    print("Invalid column.")
                    continue

                plt.figure(figsize=(7, 5))

                plt.boxplot(
                    self.data[column].dropna()
                )

                plt.ylabel(column)
                plt.title(
                    f"Box Plot of {column}"
                )

                plt.tight_layout()
                plt.show()

            elif choice == "6":

                if not numeric_columns:
                    print("No numeric columns.")
                    continue

                column = input(
                    "Enter numeric column: "
                )

                if column not in numeric_columns:
                    print("Invalid column.")
                    continue

                plt.figure(figsize=(8, 5))

                plt.hist(
                    self.data[column].dropna(),
                    bins=10
                )

                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.title(
                    f"Histogram of {column}"
                )

                plt.tight_layout()
                plt.show()

            elif choice == "7":

                if not numeric_columns:
                    print("No numeric columns.")
                    continue

                column = input(
                    "Enter numeric column: "
                )

                if column not in numeric_columns:
                    print("Invalid column.")
                    continue

                plt.figure(figsize=(7, 5))

                plt.violinplot(
                    self.data[column].dropna()
                )

                plt.ylabel(column)
                plt.title(
                    f"Violin Plot of {column}"
                )

                plt.tight_layout()
                plt.show()

            elif choice == "8":

                if len(numeric_columns) < 2:
                    print(
                        "At least two numeric columns required."
                    )
                    continue

                columns = numeric_columns[:3]

                x = np.arange(
                    len(self.data)
                )

                plt.figure(figsize=(10, 5))

                plt.stackplot(
                    x,
                    *[
                        self.data[column].fillna(0)
                        for column in columns
                    ],
                    labels=columns
                )

                plt.xlabel("Index")
                plt.ylabel("Values")
                plt.title("Stack Plot")
                plt.legend()
                plt.tight_layout()
                plt.show()

            elif choice == "9":

                if len(numeric_columns) < 1:
                    print("No numeric columns.")
                    continue

                column = input(
                    "Enter numeric column: "
                )

                if column not in numeric_columns:
                    print("Invalid column.")
                    continue

                plt.figure(figsize=(9, 5))

                plt.step(
                    range(len(self.data)),
                    self.data[column],
                    where="mid"
                )

                plt.xlabel("Index")
                plt.ylabel(column)
                plt.title(
                    f"Step Chart of {column}"
                )

                plt.tight_layout()
                plt.show()

            elif choice == "10":

                if len(numeric_columns) < 2:
                    print(
                        "At least two numeric columns required."
                    )
                    continue

                fig, axes = plt.subplots(
                    2,
                    2,
                    figsize=(12, 8)
                )

                first = numeric_columns[0]
                second = numeric_columns[1]

                axes[0, 0].plot(
                    self.data[first]
                )
                axes[0, 0].set_title(
                    f"Line - {first}"
                )

                axes[0, 1].hist(
                    self.data[first].dropna(),
                    bins=10
                )
                axes[0, 1].set_title(
                    f"Histogram - {first}"
                )

                axes[1, 0].scatter(
                    self.data[first],
                    self.data[second]
                )
                axes[1, 0].set_title(
                    f"{first} vs {second}"
                )

                axes[1, 1].boxplot(
                    self.data[numeric_columns].dropna()
                )
                axes[1, 1].set_title(
                    "Numeric Data Box Plot"
                )

                plt.tight_layout()
                plt.show()

            else:
                print("Invalid choice.")

    # =========================================================
    # SEABORN VISUALIZATION
    # =========================================================

    def visualize_seaborn(self):
        """
        Create enhanced Seaborn visualizations.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        while True:

            print("\n========== SEABORN VISUALIZATION ==========")
            print("1. Heatmap")
            print("2. Pair Plot")
            print("3. Box Plot")
            print("4. Violin Plot")
            print("5. Bar Plot")
            print("6. Back")

            choice = input(
                "Enter your choice: "
            )

            if choice == "6":
                break

            numeric_data = self.data.select_dtypes(
                include=np.number
            )

            if choice == "1":

                if numeric_data.empty:
                    print("No numeric data available.")
                    continue

                plt.figure(figsize=(10, 7))

                sns.heatmap(
                    numeric_data.corr(),
                    annot=True,
                    fmt=".2f"
                )

                plt.title(
                    "Correlation Heatmap"
                )

                plt.tight_layout()
                plt.show()

            elif choice == "2":

                if len(numeric_data.columns) < 2:
                    print(
                        "At least two numeric columns required."
                    )
                    continue

                sns.pairplot(
                    numeric_data.dropna()
                )

                plt.show()

            elif choice == "3":

                if numeric_data.empty:
                    print("No numeric data.")
                    continue

                column = input(
                    "Enter numeric column: "
                )

                if column not in numeric_data.columns:
                    print("Invalid column.")
                    continue

                plt.figure(figsize=(8, 5))

                sns.boxplot(
                    y=self.data[column]
                )

                plt.title(
                    f"Seaborn Box Plot - {column}"
                )

                plt.tight_layout()
                plt.show()

            elif choice == "4":

                if numeric_data.empty:
                    print("No numeric data.")
                    continue

                column = input(
                    "Enter numeric column: "
                )

                if column not in numeric_data.columns:
                    print("Invalid column.")
                    continue

                plt.figure(figsize=(8, 5))

                sns.violinplot(
                    y=self.data[column]
                )

                plt.title(
                    f"Seaborn Violin Plot - {column}"
                )

                plt.tight_layout()
                plt.show()

            elif choice == "5":

                print(
                    "\nAvailable columns:",
                    list(self.data.columns)
                )

                x_column = input(
                    "Enter categorical column: "
                )

                y_column = input(
                    "Enter numeric column: "
                )

                if (
                    x_column not in self.data.columns
                    or y_column not in self.data.columns
                ):
                    print("Invalid columns.")
                    continue

                plt.figure(figsize=(9, 5))

                sns.barplot(
                    data=self.data,
                    x=x_column,
                    y=y_column
                )

                plt.title(
                    f"{y_column} by {x_column}"
                )

                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            else:
                print("Invalid choice.")

    # =========================================================
    # SAVE VISUALIZATION
    # =========================================================

    def save_visualization(self):
        """
        Create and save a visualization as PNG/JPG/PDF.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        numeric_columns = list(
            self.data.select_dtypes(
                include=np.number
            ).columns
        )

        if not numeric_columns:
            print(
                "\nNo numeric columns available."
            )
            return

        column = input(
            "Enter numeric column for visualization: "
        )

        if column not in numeric_columns:
            print("Invalid column.")
            return

        print("\nChoose visualization:")
        print("1. Histogram")
        print("2. Line Plot")
        print("3. Box Plot")

        choice = input(
            "Enter your choice: "
        )

        plt.figure(figsize=(9, 5))

        if choice == "1":

            plt.hist(
                self.data[column].dropna(),
                bins=10
            )

            plt.xlabel(column)
            plt.ylabel("Frequency")
            plt.title(
                f"Histogram of {column}"
            )

        elif choice == "2":

            plt.plot(
                self.data[column],
                marker="o"
            )

            plt.xlabel("Index")
            plt.ylabel(column)
            plt.title(
                f"Line Plot of {column}"
            )

        elif choice == "3":

            plt.boxplot(
                self.data[column].dropna()
            )

            plt.ylabel(column)
            plt.title(
                f"Box Plot of {column}"
            )

        else:

            print("Invalid choice.")
            plt.close()
            return

        plt.tight_layout()

        filename = input(
            "\nEnter file name to save the plot "
            "(example: sales_plot.png): "
        )

        try:

            plt.savefig(
                filename,
                dpi=300,
                bbox_inches="tight"
            )

            print(
                f"\nVisualization saved successfully: "
                f"{filename}"
            )

        except Exception as e:

            print(
                "Error while saving visualization:",
                e
            )

        plt.show()

    # =========================================================
    # DATA SUMMARY
    # =========================================================

    def display_summary(self):
        """
        Display a complete sales dataset summary.
        """

        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        print("\n" + "=" * 60)
        print("                 DATASET SUMMARY")
        print("=" * 60)

        print(
            "\nNumber of Rows:",
            len(self.data)
        )

        print(
            "Number of Columns:",
            len(self.data.columns)
        )

        print(
            "\nColumns:",
            list(self.data.columns)
        )

        print("\nMissing Values:")
        print(self.data.isnull().sum())

        numeric_data = self.data.select_dtypes(
            include=np.number
        )

        if not numeric_data.empty:

            print("\nNumeric Summary:")
            print(
                numeric_data.describe()
            )

        print("\nFirst 5 Records:")
        print(self.data.head())


# =============================================================
# MAIN PROGRAM
# =============================================================

print("=" * 65)
print("        DATA ANALYSIS & VISUALIZATION PROGRAM")
print("=" * 65)

analyzer = SalesDataAnalyzer()

while True:

    print("\n" + "=" * 65)
    print("Main Menu")
    print("=" * 65)

    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. NumPy Array Operations")
    print("6. Search, Sort, or Filter Data")
    print("7. Generate Aggregate Functions")
    print("8. Generate Descriptive Statistics")
    print("9. Create Pivot Table")
    print("10. GroupBy and Transform")
    print("11. Matplotlib Visualization")
    print("12. Seaborn Visualization")
    print("13. Save Visualization")
    print("14. Display Complete Summary")
    print("15. Exit")

    choice = input(
        "\nEnter your choice: "
    )

    # ---------------------------------------------------------
    # LOAD DATASET
    # ---------------------------------------------------------

    if choice == "1":

        path = input(
            "\nEnter the path of the dataset (CSV file): "
        )

        analyzer.load_data(path)

    # ---------------------------------------------------------
    # EXPLORE DATA
    # ---------------------------------------------------------

    elif choice == "2":

        analyzer.explore_data()

    # ---------------------------------------------------------
    # DATAFRAME OPERATIONS
    # ---------------------------------------------------------

    elif choice == "3":

        analyzer.dataframe_operations()

    # ---------------------------------------------------------
    # HANDLE MISSING DATA
    # ---------------------------------------------------------

    elif choice == "4":

        analyzer.handle_missing_data()

    # ---------------------------------------------------------
    # NUMPY OPERATIONS
    # ---------------------------------------------------------

    elif choice == "5":

        analyzer.numpy_operations()

    # ---------------------------------------------------------
    # SEARCH SORT FILTER
    # ---------------------------------------------------------

    elif choice == "6":

        analyzer.search_sort_filter()

    # ---------------------------------------------------------
    # AGGREGATION
    # ---------------------------------------------------------

    elif choice == "7":

        analyzer.aggregate_functions()

    # ---------------------------------------------------------
    # STATISTICS
    # ---------------------------------------------------------

    elif choice == "8":

        analyzer.statistical_analysis()

    # ---------------------------------------------------------
    # PIVOT TABLE
    # ---------------------------------------------------------

    elif choice == "9":

        analyzer.create_pivot_table()

    # ---------------------------------------------------------
    # GROUPBY TRANSFORM
    # ---------------------------------------------------------

    elif choice == "10":

        analyzer.groupby_transform()

    # ---------------------------------------------------------
    # MATPLOTLIB
    # ---------------------------------------------------------

    elif choice == "11":

        analyzer.visualize_matplotlib()

    # ---------------------------------------------------------
    # SEABORN
    # ---------------------------------------------------------

    elif choice == "12":

        analyzer.visualize_seaborn()

    # ---------------------------------------------------------
    # SAVE VISUALIZATION
    # ---------------------------------------------------------

    elif choice == "13":

        analyzer.save_visualization()

    # ---------------------------------------------------------
    # SUMMARY
    # ---------------------------------------------------------

    elif choice == "14":

        analyzer.display_summary()

    # ---------------------------------------------------------
    # EXIT
    # ---------------------------------------------------------

    elif choice == "15":

        print("\nExiting the program.")
        print(
            "Thank you for using the Sales Data "
            "Analysis & Visualization Program!"
        )
        print("Goodbye!")

        break

    # ---------------------------------------------------------
    # INVALID CHOICE
    # ---------------------------------------------------------

    else:

        print(
            "\nInvalid choice. "
            "Please select an option from 1 to 15."
        )