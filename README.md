# CODE_WARS
## A collection of my completed code wars tasks...

---

# Multiples of 3 or 5 

DESCRIPTION:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0.
Note: If the number is a multiple of both 3 and 5, only count it once.

    def solution(number):
        return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)

I wrote some code to get the answer when a user enters the number, with some additional defensive programming.

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
  
---
# Laxative shot roulette

Description
Peter enjoys taking risks, and this time he has decided to take it up a notch!
Peter asks his local barman to pour him n shots, after which Peter then puts laxatives in x of them.
He then turns around and lets the barman shuffle the shots. Peter approaches the shots and drinks a of them one at a time. 
Just one shot is enough to give Peter a runny tummy. What is the probability that Peter doesn't need to run to the loo?

Task
You are given:
n - The total number of shots.
x - The number of laxative laden shots.
a - The number of shots that peter drinks.
return the probability that Peter won't have the trots after drinking. n will always be greater than x, and a will always be less than n.
You must return the probability rounded to two decimal places i.e. 0.05 or 0.81
 
    def get_chance(n, x, a):
        prob = 1
        for i in range(a):
            prob *= ((n-x-i)/(n-i))
        return round(prob, 2)
