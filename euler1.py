# https://projecteuler.net/problem=1 (note: project euler doesn't want public sharing of solutions beyond problems 1-100)
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

sum = 0
sum_list = [] # this is just to check that my code is picking the right numbers, and I print it below

for number in range(1, 1000):
    if number % 3 == 0:
        sum += number
        sum_list.append(number) # adds numbers divisible by 3 to my sum total, and to sum_list so I can check what's being added
    elif number % 5 == 0:
        sum += number
        sum_list.append(number) # adds numbers divisible by 5 to my sum total, and to sum_list so I can check what's being added
    else:
        sum += 0

print(sum_list) # prints a list of all the numbers my code picks as divisible by 3 or 5
print(sum) # prints the problem's solution