print("=" * 55)
print("        WELCOME TO FUNDAMENTAL BOOSTER")
print("       PERSONAL DATA COLLECTOR PROJECT")
print("=" * 55)

print("\nPlease enter your personal information.")
print("-" * 55)

# Taking input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in feet: "))
favorite_number = int(input("Enter your favourite number: "))

# Additional calculations using operators
next_age = age + 1
height_cm = height * 30.48
double_number = favorite_number * 2
number_plus_age = favorite_number + age

# Type casting
age_float = float(age)
height_int = int(height)

print("\n" + "=" * 55)
print("             PERSONAL INFORMATION")
print("=" * 55)

print("Name            :", name)
print("Age             :", age)
print("Height (feet)   :", height)
print("Height (cm)     :", height_cm)
print("Favourite Number:", favorite_number)

print("\n" + "-" * 55)
print("             CALCULATIONS")
print("-" * 55)

print("Your age next year will be:", next_age)
print("Double your favourite number:", double_number)
print("Favourite number + age:", number_plus_age)

# Demonstrating type casting
print("\n" + "-" * 55)
print("             TYPE CASTING")
print("-" * 55)

print("Original age:", age, "| Type:", type(age))
print("Age converted to float:", age_float, "| Type:", type(age_float))

print("Original height:", height, "| Type:", type(height))
print("Height converted to integer:", height_int, "| Type:", type(height_int))

# Demonstrating id() and type()
print("\n" + "-" * 55)
print("             TYPE AND MEMORY INFORMATION")
print("-" * 55)

print("Name")
print("  Value :", name)
print("  Type  :", type(name))
print("  ID    :", id(name))

print("\nAge")
print("  Value :", age)
print("  Type  :", type(age))
print("  ID    :", id(age))

print("\nHeight")
print("  Value :", height)
print("  Type  :", type(height))
print("  ID    :", id(height))

print("\nFavourite Number")
print("  Value :", favorite_number)
print("  Type  :", type(favorite_number))
print("  ID    :", id(favorite_number))

# Summary
print("\n" + "=" * 55)
print("                  SUMMARY")
print("=" * 55)

print(f"Hello {name}!")
print(f"You are {age} years old and your height is {height} feet.")
print(f"Your favourite number is {favorite_number}.")
print(f"Next year, you will be {next_age} years old.")
print(f"Your height in centimeters is {height_cm:.2f} cm.")

print("\nThank you for using Fundamental Booster!")
print("=" * 55)