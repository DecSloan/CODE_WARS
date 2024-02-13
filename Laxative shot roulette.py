import numpy

# Make an empty list to save the probabilities in 
probability_list = []

# You need to fill out 3 variables to work out the probability
# The total number of shots - total_shots
# The number of shots that have laxative in them - tainted_shots
# The number of shots you are going to drink - amount_drank
def get_chance(total_shots, tainted_shots, shots_to_drink):
    for num in range(shots_to_drink):
        ans = 1 - (tainted_shots / total_shots)
        total_shots -= 1
        probability_list.append(ans)
    
    # Multiply all the probability's that were saved in the list
    # This will give you the total probability
    # Round this answer to 2 decimal places for ease
    prob = numpy.prod(probability_list)
    rounded_prob = round(prob, 2)
    print(f"\nThe probablilty that you WILL NOT need to use the bathroom unexpectedly " +
          f"(to 2 decimal places) is {rounded_prob}")

# Get the user to enter the total number of shots
# Try/except Value error for non integers
# Break once valid input entered
while True:
    try:
        total_shots = int(input("Please enter the total number of shots: "))
        break

    except ValueError:
        print("\nPlease enter a valid integer!\n")

# Get the user to enter the number of shots with added laxative
# Laxative shots can't be more than the total - if it is error messsage displayed
# Try/except Value error for non integers
# Break once valid input entered
while True:
    try:
        tainted_shots = int(input("Please enter the number of shots that have laxative added: "))
        if tainted_shots >= total_shots:
            print("\nNumber of shots with laxative must be smaller than the total amount of shots!\n")

        else:
            break

    except ValueError:
        print("\nPlease enter a valid integer!\n")

# Get the user to enter the number of shots you are going to drink
# Shots to drink must be less than total - tainted shots - if it is error messsage displayed
# Try/except Value error for non integers
# Break once valid input entered
while True:
    try:
        shots_to_drink = int(input("Please enter the number of shots that you are going to drink: "))
        if shots_to_drink >= total_shots - tainted_shots:
            print("\nShots to drink must be smaller than total shots minus shots " +
                  "with laxative in them or you will definitely need to use the bathroom!\n") 

        else:
            break

    except ValueError:
        print("\nPlease enter a valid integer!\n")

# To get the probability that you WILL NOT need to use the bathroom
# Use the numbers entered by the user
get_chance_test = get_chance(total_shots, tainted_shots, shots_to_drink)