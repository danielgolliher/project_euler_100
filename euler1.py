# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
# https://projecteuler.net/problem=1

sum = 0
sum_list = []

for number in range(1, 1000):
    if number % 3 == 0:
        sum += number
        sum_list.append(number)
    elif number % 5 == 0:
        sum += number
        sum_list.append(number)
    else:
        sum += 0

print(sum_list)
print(sum)