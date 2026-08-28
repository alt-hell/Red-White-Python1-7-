# Python Projects Collection

A collection of Python projects designed to demonstrate programming
fundamentals, data structures, functions, Object-Oriented Programming,
NumPy, Pandas, data analysis, and data visualization.

------------------------------------------------------------------------

## Projects Included

  -----------------------------------------------------------------------
  \#                      Project                 Main Concepts
  ----------------------- ----------------------- -----------------------
  1                       Fundamental Booster     `print()`, `input()`,
                                                  variables, data types,
                                                  operators, type
                                                  casting, `id()`,
                                                  `type()`

  2                       Logic Box               Loops, `range()`,
                                                  nested loops, `break`,
                                                  `continue`, `pass`,
                                                  pattern generation,
                                                  number analysis

  3                       Collection Manipulator  Lists, tuples, sets,
                                                  dictionaries,
                                                  mutability, type
                                                  casting, `del`, CRUD
                                                  operations

  4                       Functional Treat        Functions, `*args`,
                                                  `**kwargs`, `__doc__`,
                                                  recursion, lambda,
                                                  `map()`, `filter()`,
                                                  `global`, multiple
                                                  return values

  5                       OOP Wrapper             Classes, objects,
                                                  constructors,
                                                  destructors,
                                                  inheritance,
                                                  encapsulation,
                                                  overriding, `super()`,
                                                  `issubclass()`, dunder
                                                  methods, operator
                                                  overloading

  6                       NumPy Analyzer          NumPy arrays, indexing,
                                                  slicing, mathematical
                                                  operations,
                                                  combining/splitting,
                                                  search, sorting,
                                                  filtering, statistics

  7                       Pandas Analyzer & Data  Pandas, NumPy,
                          Visualization           Matplotlib, Seaborn,
                                                  data cleaning,
                                                  DataFrame operations,
                                                  aggregation,
                                                  statistics, pivot
                                                  tables, visualization
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# 1. Fundamental Booster

## Description

An interactive Personal Data Collector application that captures and
processes information entered by the user.

## Concepts Covered

-   `print()`
-   `input()`
-   Variables
-   Strings
-   Integers
-   Floats
-   Arithmetic operators
-   Type casting
-   `type()`
-   `id()`
-   Formatted output

## Main Features

-   Collect personal information
-   Perform basic calculations
-   Convert values between data types
-   Display variable types
-   Display memory/object IDs
-   Generate a formatted summary

## Example Information

-   Name
-   Age
-   Height
-   Favourite number

------------------------------------------------------------------------

# 2. Logic Box

## Description

A menu-driven Pattern Generator and Number Analyzer that focuses on
control flow and loops.

## Concepts Covered

-   `if`, `elif`, `else`
-   `while` loops
-   `for` loops
-   Nested loops
-   `range()`
-   `break`
-   `continue`
-   `pass`
-   Input validation

## Pattern Generator

The project provides:

1.  Right-angled triangle
2.  Pyramid
3.  Left-angled triangle

## Number Analyzer

The program can:

-   Analyze a range of numbers
-   Check whether numbers are odd or even
-   Calculate the sum of numbers in a range

------------------------------------------------------------------------

# 3. Collection Manipulator

## Description

A Student Data Organizer that demonstrates Python collection data types
and CRUD operations.

## Concepts Covered

-   List
-   Tuple
-   Set
-   Dictionary
-   Mutability
-   Immutability
-   Type casting
-   `del`
-   String formatting
-   CRUD operations

## Student Information

Each student record can contain:

-   Student ID
-   Name
-   Age
-   Grade
-   Date of Birth
-   Subjects

## Data Structures Used

### List

Used for managing multiple student records.

### Tuple

Used to store immutable information such as:

``` python
(student_id, date_of_birth)
```

### Set

Used for storing unique subjects.

### Dictionary

Used to organize each student's information.

## Main Operations

1.  Add Student
2.  Display All Students
3.  Update Student Information
4.  Delete Student
5.  Display Subjects Offered
6.  Exit

------------------------------------------------------------------------

# 4. Functional Treat

## Description

A Data Analyzer and Transformer program demonstrating Python functions
and functional programming concepts.

## Concepts Covered

-   User-defined functions
-   Built-in functions
-   `*args`
-   `**kwargs`
-   `__doc__`
-   Recursion
-   Lambda functions
-   `map()`
-   `filter()`
-   `global`
-   Multiple return values
-   1D lists
-   2D lists
-   Sorting

## Main Features

-   Enter 1D data
-   Enter 2D data
-   Display data statistics
-   Calculate factorial recursively
-   Calculate Fibonacci recursively
-   Filter values using lambda
-   Use `map()` for transformation
-   Sort data
-   Find duplicate values
-   Display unique values
-   Use `*args` and `**kwargs`
-   Demonstrate global variables
-   Return multiple statistical values

------------------------------------------------------------------------

# 5. OOP Wrapper

## Description

An Employee Management System demonstrating Object-Oriented Programming
concepts.

## Classes

### Employee

Base class containing:

-   Name
-   Age
-   Employee ID
-   Salary

### Manager

Inherited from `Employee`.

Additional attribute:

-   Department

### Developer

Inherited from `Employee`.

Additional attribute:

-   Programming language

## OOP Concepts Covered

-   Classes
-   Objects
-   `self`
-   Constructors
-   Destructors
-   Inheritance
-   Method overriding
-   Encapsulation
-   Getter methods
-   Setter methods
-   `super()`
-   `issubclass()`
-   `__str__`
-   `__eq__`
-   `__lt__`
-   `__gt__`
-   Operator overloading

## Main Operations

1.  Create a Person
2.  Create an Employee
3.  Create a Manager
4.  Create a Developer
5.  Show Details
6.  Compare Salaries
7.  Demonstrate OOP Features
8.  Update Employee Salary
9.  Exit

------------------------------------------------------------------------

# 6. NumPy Analyzer

## Description

A NumPy-based Data Analyzer that performs array manipulation,
mathematical operations, searching, sorting, filtering, aggregation, and
statistical analysis.

## Technology

-   Python
-   NumPy

## Concepts Covered

-   NumPy arrays
-   1D arrays
-   2D arrays
-   3D arrays
-   Indexing
-   Slicing
-   Array creation
-   Array combining
-   Array splitting
-   Element-wise operations
-   Matrix multiplication
-   Searching
-   Sorting
-   Filtering
-   Aggregation
-   Statistics
-   OOP

## Mathematical Operations

-   Addition
-   Subtraction
-   Multiplication
-   Division
-   Matrix multiplication

## Aggregation

-   Sum
-   Mean
-   Median
-   Standard deviation
-   Variance

## Statistical Analysis

-   Minimum
-   Maximum
-   Percentiles
-   Correlation coefficient

## OOP Features

The project uses a `DataAnalytics` class with:

-   Constructor
-   Class method
-   Static method
-   Encapsulated functionality

------------------------------------------------------------------------

# 7. Pandas Analyzer & Data Visualization

## Description

A comprehensive Sales Data Analysis and Visualization application using
Pandas, NumPy, Matplotlib, and Seaborn.

The project is designed to analyze sales datasets and create meaningful
visualizations for business insights.

## Technologies

-   Python
-   Pandas
-   NumPy
-   Matplotlib
-   Seaborn

## Dataset

The program works with CSV datasets.

A typical sales dataset may contain:

``` text
SalesID
Product
Region
Sales
Year
```

Other compatible columns can also be used depending on the analysis.

## Class

The main class is:

``` python
SalesDataAnalyzer
```

It encapsulates the data and analysis functionality.

## Main Features

### Data Acquisition

-   Load CSV datasets
-   Validate file paths
-   Handle loading errors

### Data Exploration

-   Display first rows
-   Display last rows
-   Display column names
-   Display data types
-   Display dataset information
-   Display statistical description
-   Display dataset shape
-   Display unique values

### Data Cleaning

-   Detect missing values
-   Display rows containing missing values
-   Fill numeric missing values with mean
-   Drop rows with missing values
-   Replace missing values

### NumPy Operations

-   Convert DataFrame data to NumPy arrays
-   Display array shape
-   Display dimensions
-   Display size
-   Index arrays
-   Slice arrays
-   Perform element-wise operations

### DataFrame Operations

-   Select columns
-   Create calculated columns
-   Rename columns
-   Drop columns
-   Group data
-   Merge DataFrames
-   Sort DataFrames

### Search, Sort & Filter

-   Search for values
-   Sort ascending
-   Sort descending
-   Filter using thresholds
-   Filter using comparison conditions

### Aggregation

-   Sum
-   Mean
-   Median
-   Minimum
-   Maximum
-   Count

### Statistical Analysis

-   Standard deviation
-   Variance
-   Percentiles
-   Descriptive statistics

### Advanced Pandas Operations

-   Pivot tables
-   `groupby()`
-   `transform()`

### Matplotlib Visualizations

The project supports:

-   Bar plot
-   Line plot
-   Scatter plot
-   Pie chart
-   Box plot
-   Histogram
-   Violin plot
-   Stack plot
-   Step chart
-   Multiple plots

### Seaborn Visualizations

The project supports:

-   Heatmap
-   Pair plot
-   Box plot
-   Violin plot
-   Bar plot

### Export

Visualizations can be saved as image files such as:

``` text
.png
.jpg
.pdf
```

------------------------------------------------------------------------

# Installation

## Requirements

Python 3.x is recommended.

Install the required packages using:

``` bash
pip install -r requirements.txt
```

For the Pandas Analyzer project, the main external libraries are:

``` text
numpy
pandas
matplotlib
seaborn
```

------------------------------------------------------------------------

# Creating requirements.txt Automatically

If you want to generate a requirements file based on the packages
imported by your Python files, install `pipreqs`:

``` bash
pip install pipreqs
```

Then navigate to the project folder:

``` bash
cd "C:\Users\HELL\OneDrive\Desktop\Python (RednWhite 1-7)"
```

Generate the file:

``` bash
pipreqs . --force
```

This creates or updates:

``` text
requirements.txt
```

Another option is:

``` bash
pip freeze > requirements.txt
```

However, `pipreqs` is generally better when you want the requirements
based on the imports used by the project rather than every package
installed in the Python environment.

------------------------------------------------------------------------

# How to Run the Projects

Navigate to the folder containing the Python file.

Example:

``` bash
python Fundamental_booster.py
```

For the Logic Box project:

``` bash
python Logic_Box.py
```

For the Collection Manipulator:

``` bash
python Collection_Manipulator.py
```

For the Functional Treat project:

``` bash
python Functional_Treat.py
```

For the OOP Wrapper:

``` bash
python OOP_Wrapper.py
```

For the NumPy Analyzer:

``` bash
python Numpy_Analyzer.py
```

For the Pandas Analyzer:

``` bash
python Pandas_Analyzer.py
```

Use the actual filename if your filenames are different.

------------------------------------------------------------------------

# Recommended Project Structure

``` text
Python-Projects/
│
├── Fundamental_Booster/
│   └── Fundamental_booster.py
│
├── Logic_Box/
│   └── Logic_Box.py
│
├── Collection_Manipulator/
│   └── Collection_Manipulator.py
│
├── Functional_Treat/
│   └── Functional_Treat.py
│
├── OOP_Wrapper/
│   └── OOP_Wrapper.py
│
├── NumPy_Analyzer/
│   └── Numpy_Analyzer.py
│
├── Pandas_Analyzer/
│   ├── Pandas_Analyzer.py
│   ├── sales_data.csv
│   └── visualizations/
│
├── requirements.txt
└── README.md
```

------------------------------------------------------------------------

# Learning Progression

These projects are designed to progress from basic Python concepts to
practical data analysis.

``` text
Fundamental Booster
        ↓
Logic Box
        ↓
Collection Manipulator
        ↓
Functional Treat
        ↓
OOP Wrapper
        ↓
NumPy Analyzer
        ↓
Pandas Analyzer & Data Visualization
```

The progression covers:

``` text
Python Basics
    ↓
Control Flow
    ↓
Data Structures
    ↓
Functions
    ↓
Object-Oriented Programming
    ↓
NumPy
    ↓
Pandas
    ↓
Data Analysis
    ↓
Data Visualization
```

------------------------------------------------------------------------

# Learning Outcomes

After completing these projects, the learner should be able to:

-   Write Python programs using variables and data types
-   Use conditional statements and loops
-   Work with lists, tuples, sets, and dictionaries
-   Create reusable functions
-   Use functional programming concepts
-   Implement recursive functions
-   Build classes and objects
-   Apply inheritance and encapsulation
-   Use operator overloading
-   Work with NumPy arrays
-   Perform mathematical and statistical operations
-   Manipulate Pandas DataFrames
-   Clean missing data
-   Search, filter, sort, and aggregate datasets
-   Create pivot tables and grouped analysis
-   Create professional data visualizations
-   Save visualizations for reporting
-   Build menu-driven Python applications

------------------------------------------------------------------------

# General Troubleshooting

## Python is not recognized

Check Python installation:

``` bash
python --version
```

or:

``` bash
python3 --version
```

## Package is missing

Install the package:

``` bash
pip install package_name
```

For all project dependencies:

``` bash
pip install -r requirements.txt
```

## File not found

Make sure you are inside the correct project directory:

``` bash
cd "path\to\your\project"
```

Then run:

``` bash
python filename.py
```

## Pandas Analyzer cannot find CSV

Provide the correct CSV path when prompted.

Example:

``` text
sales_data.csv
```

or:

``` text
data/sales_data.csv
```

------------------------------------------------------------------------

# Author

Sohail Ansari

------------------------------------------------------------------------

# License

This project collection is intended for educational and learning
purposes.
