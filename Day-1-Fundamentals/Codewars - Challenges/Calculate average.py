# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

def find_average(numbers):
    # your code here
    sum = 0
    for i in range(len(numbers)):
        sum = sum+numbers[i]
    if len(numbers) > 0:
        return sum/len(numbers)
    else:
        return 0
print(find_average([1]))