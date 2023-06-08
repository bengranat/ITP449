"""
    Ben Granat
    ITP-449
    Assignment 1

    Script that calculates age using branched if statements
    User inputs day, month, and year in numeric format
    Output will result in user's current age
    Improper inputs will prompt an error message for the user

    Note: I was not exactly sure what the correct format of this assignment is
    given the restrictions we have - no loops or lists/dictionaries/etc specifically.

    Issue: The program only takes numeric figures. Since we cannot use loops,
    I am not sure how to avoid the program crashing when user inputs a string.
    Please only input integers.

    Issue: The code is very convaluted with lots of branched if statements. I know how to set up an age calculator
    with the use of lists/dictionaries and loops - would make suffix printing and user input checking a lot easier.
    Given our restrictions, I wasn't sure how to make the code cleaner. However, the assignment passed all tests
    and matched the example output. Please let me know if I was supposed to do this assignment differently.
    I would like the opportunity to redo/clean up the code.

    """


def main():
    # User input for name
    name = input("Hello! Enter your name: ")

    # Boolean variable to make sure future inputs are correctly formatted
    quit = False

    # Next section of if statements is to check valid format of user inputs
    # Changes value of boolean variable if user input is not correctly formatted or illogical

    # Birth year inputs and if statements
    birth_year = int(input("Enter the year you were born: "))
    if not birth_year < 2023:
        quit = True

    # Birth month inputs and if statements
    birth_month = int(input("Enter the month of the year you were born: "))
    if not birth_month < 13 or birth_month == 0:
        quit = True

    # Birth day inputs and if statements
    birth_day = int(input("Enter the day of the month you were born: "))
    if birth_month == 1 or birth_month == 3 or birth_month == 5 or birth_month == 7 or birth_month == 8 or birth_month == 10 or birth_month == 12:
        if not birth_day < 32:
            quit = True
    elif birth_month == 4 or birth_month == 6 or birth_month == 9 or birth_month or 11:
        if not birth_day < 31:
            quit = True
    elif birth_month == 2:
        if not birth_day < 29:
            quit = True

    # Check if birthday happened in 2023 but before January 21 - assignment's due date
    if birth_year == 2023 and birth_month > 1 or birth_year == 2023 and birth_month == 1 and birth_day > 21:
        quit = True

        # Next section will output error print statements based on values associated with birth_year,month,day

    if quit == True:

        # Error message if birthday happens in 2023 but after January 21
        if birth_year == 2023 and birth_month > 1 or birth_year == 2023 and birth_month == 1 and birth_day > 21:
            print("\n" + "You have entered a birthdate which has not yet happened.")
            print("Please restart the program.")

            # Error message if birth year is after 2023
        elif not birth_year < 2024:
            print("\n" + "You have entered a birthdate which has not yet happened.")
            print("Please restart the program.")

            # Error message if birth_month is 0 or greater than 12
        elif not birth_month < 13 or birth_month == 0:
            print("\n" + str(birth_month) + " is an invalid month. (It doesn't exist.)")
            print("Please restart the program.")

            # Error message(s) if birth_day doesn't correspond with birth_month
        # Example: February 30 doesn't exist
        elif birth_month == 1:
            if not birth_day < 32:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in January.)")
                print("Please restart the program.")
        elif birth_month == 3:
            if not birth_day < 32:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in March.)")
                print("Please restart the program.")
        elif birth_month == 5:
            if not birth_day < 32:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in May.)")
                print("Please restart the program.")
        elif birth_month == 7:
            if not birth_day < 32:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in July.)")
                print("Please restart the program.")
        elif birth_month == 8:
            if not birth_day < 32:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in August.)")
                print("Please restart the program.")
        elif birth_month == 10:
            if not birth_day < 32:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in October.)")
                print("Please restart the program.")
        elif birth_month == 12:
            if not birth_day < 32:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in December.)")
                print("Please restart the program.")
        elif birth_month == 4:
            if not birth_day < 31:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in April.)")
                print("Please restart the program.")
        elif birth_month == 6:
            if not birth_day < 31:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in June.)")
                print("Please restart the program.")
        elif birth_month == 9:
            if not birth_day < 31:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in September.)")
                print("Please restart the program.")
        elif birth_month == 11:
            if not birth_day < 31:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in November.)")
                print("Please restart the program.")
        elif birth_month == 2:
            if not birth_day < 29:
                print("\n" + str(birth_day) + " is an invalid day. (It doesn't exist in February.)")
                print("Please restart the program.")

                # If birthday figures are properlly formatted...
    if quit != True:
        # Calculates year difference as age
        year_difference = 2023 - birth_year
        # Checks for case when birthday date is before due date of assignment
        # Assignment due date = January 21, 2023
        # Example:
        # A person born on January 5, 2001 is 22 ->
        # A person born on January 30, 2001 is 21
        if birth_month != 1:
            if not birth_day < 21:
                year_difference -= 1

        # Numerous if statements based on birth month value.
        # Each month's if statement has other if statements dpending on suffix of day.
        # Each day, month, year will output with correct suffix and month name.
        if birth_month == 1:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of January.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n" + "Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of January.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of January.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of January.")
                print("You are " + str(year_difference) + " years old.")

        elif birth_month == 2:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of February.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of February.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of February.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of February.")
                print("You are " + str(year_difference) + " years old.")

        elif birth_month == 3:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of March.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of March.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of March.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of March.")
                print("You are " + str(year_difference) + " years old.")

        elif birth_month == 4:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of April.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of April.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of April.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of April.")
                print("You are " + str(year_difference) + " years old.")

        elif birth_month == 5:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of May.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of May.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of May.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of May.")
                print("You are " + str(year_difference) + " years old.")

        elif birth_month == 6:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of June.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of June.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of June.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of June.")
                print("You are " + str(year_difference) + " years old.")

        elif birth_month == 7:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of July.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of July.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of July.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of July.")
                print("You are " + str(year_difference) + " years old.")

        elif birth_month == 8:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of August.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of August.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of August.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of August.")
                print("You are " + str(year_difference) + " years old.")

        elif birth_month == 9:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of September.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of September.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of September.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of September.")
                print("You are " + str(year_difference) + " years old.")

        elif birth_month == 10:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of October.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of October.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of October.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of October.")
                print("You are " + str(year_difference) + " years old.")

        elif birth_month == 11:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of November.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of November.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of November.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of November.")
                print("You are " + str(year_difference) + " years old.")

        elif birth_month == 12:
            if birth_day == 1 or birth_day == 21 or birth_day == 31:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "st of December.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 2 or birth_day == 22:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "nd of December.")
                print("You are " + str(year_difference) + " years old.")
            elif birth_day == 3 or birth_day == 23:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "rd of December.")
                print("You are " + str(year_difference) + " years old.")
            else:
                print("\n")
                print("Hello " + name + "!")
                print("You were born in " + str(birth_year) + " on the " + str(birth_day) + "th of December.")
                print("You are " + str(year_difference) + " years old.")


if __name__ == '__main__':
    main()