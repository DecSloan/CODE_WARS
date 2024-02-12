import math

# Make an empty list for both multiples of 3 and 5
multiples_of_3 = []
multiples_of_5 = []

def solution(number):
    # For the range of numbers but not including the chosen number
    for i in range(number):
        # If its a multiple of 3 add it to the empty multiples_of_3 list 
        if i % 3 == 0:
            multiples_of_3.append(i)
        # If it is a multiple of 5 AND NOT a multiple of 3 add to multiples_of_5 list
        elif i % 5 == 0 and not i % 3 == 0:
            multiples_of_5.append(i)
    
    # Get sum for both lists
    # Add them together to get the grand_total
    # Print statement with total of all multiples below chosen number 
    total_3 = sum(multiples_of_3)
    total_5 = sum(multiples_of_5)
    grand_total = (total_3 + total_5)
    print(f"\nThe sum of all the multiples of 3 or 5 below {number}, only " +
          f"including numbers that appear in both lists once, is {grand_total}!")

# Try/except block with while loop to reduce user errors
# If no integer entered, error message displayed and promted to enter valid number
while True:
    try:
        number = int(input("Please enter any whole number: "))
        break

    except ValueError:
        print("\nPlease enter a valid number.\n")

solution_test = solution(number)