""" Your name
    ITP-449
    Assignment 2
    Program will print the number of possible combinations of changes
    for a given amount of money.
"""

# Function asks user for monetary amount and makes sure user enters valid number
# Returns user input amount (float)
def get_user_input():
    print("This program calculates the number of coin combinations")
    print("you can create from a given amount of money." + "\n")
    user_input = 0
    # Try except function to check user input is a float.
    # Except statement uses ValueError
    while True:
        try:
            user_input = float(input("Enter an amount of money: "))
        except ValueError:
            print("That is not a valid number.", end = " ")
        else:
            break
    return user_input

# Function creates coin and counter lists to track number of combinations
# Returns final number of combinations
def get_total_combinations(user_input):
    coin_list = [1, 5, 10, 25]
    # Converts user input into cents and int
    user_input_cents = 100*user_input
    user_input_int = int(user_input_cents)
    # Initializes counter list to hold
    counter_list = [0]*(user_input_int + 1)
    counter_list[0] = 1
    # Iterates through coins in coin_list
    for coin in coin_list:
        # Iterates through counter_list starting from the current coin
        for i in range(coin, user_input_int + 1):
            # Adds value at i-coin index to value at i index
            # untill desired sum is achieved.
            counter_list[i] += counter_list[i - coin]
    # Returns value located at the index associated with total change sum
    return counter_list[user_input_int]

def main():
    # User input variable
    user_input = get_user_input()
    # Total count variable
    counter = get_total_combinations(user_input)
    print("The total number of combinations for $" + str(user_input) + " is " + str(counter) + ".")


if __name__ == '__main__':
    main()