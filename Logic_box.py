print("=" * 55)
print("     WELCOME TO THE PATTERN GENERATOR AND")
print("           NUMBER ANALYZER PROJECT")
print("=" * 55)

while True:

    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # --------------------------------------------------
    # PATTERN GENERATOR
    # --------------------------------------------------
    if choice == "1":

        while True:
            print("\nChoose a pattern type:")
            print("1. Right-angled Triangle")
            print("2. Pyramid")
            print("3. Left-angled Triangle")
            print("4. Back to Main Menu")

            pattern_choice = input("Enter your choice: ")

            if pattern_choice == "4":
                break

            if pattern_choice not in ["1", "2", "3"]:
                print("Invalid pattern choice. Please try again.")
                continue

            while True:
                try:
                    rows = int(input("Enter the number of rows for the pattern: "))

                    if rows <= 0:
                        print("Row count must be greater than 0.")
                        continue

                    break

                except ValueError:
                    print("Please enter a valid integer.")

            print("\nPattern:")

            # Right-angled Triangle
            if pattern_choice == "1":

                for i in range(1, rows + 1):
                    for j in range(i):
                        print("*", end="")
                    print()

            # Pyramid
            elif pattern_choice == "2":

                for i in range(1, rows + 1):

                    # Spaces
                    for j in range(rows - i):
                        print(" ", end="")

                    # Stars
                    for j in range(2 * i - 1):
                        print("*", end="")

                    print()

            # Left-angled Triangle
            elif pattern_choice == "3":

                for i in range(1, rows + 1):

                    # Spaces
                    for j in range(rows - i):
                        print(" ", end="")

                    # Stars
                    for j in range(i):
                        print("*", end="")

                    print()

    # --------------------------------------------------
    # NUMBER ANALYZER
    # --------------------------------------------------
    elif choice == "2":

        while True:
            try:
                start = int(input("\nEnter the start of the range: "))
                end = int(input("Enter the end of the range: "))

                if end < start:
                    print("Invalid range! End number must be greater than or equal to start number.")
                    continue

                break

            except ValueError:
                print("Please enter valid numbers.")

        print("\nNumber Analysis:")
        print("-" * 35)

        total = 0

        for number in range(start, end + 1):

            # Odd or Even
            if number % 2 == 0:
                print(f"Number {number} is Even")
            else:
                print(f"Number {number} is Odd")

            # Sum of numbers
            total += number

        print("-" * 35)
        print(f"Sum of all numbers from {start} to {end} is: {total}")

    # --------------------------------------------------
    # EXIT
    # --------------------------------------------------
    elif choice == "3":

        print("\nExiting the program. Goodbye!")
        break

    # --------------------------------------------------
    # INVALID MENU OPTION
    # --------------------------------------------------
    else:
        print("\nInvalid choice. Please select 1, 2, or 3.")
        continue