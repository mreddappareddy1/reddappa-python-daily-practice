# Take a Number And Sum Its Digits Raised To The Consecutive Powers And ..
# The number 898989 is the first integer with more than one digit that fulfills 
# the property partially introduced in the title of this kata.
#  What's the use of saying "Eureka"? Because this sum gives the same number: 
#  89= 8^1 + 9^2 = 89

# The next number in having this property is 135:
# See this property again: 135=11+32+53135 = 1^1 + 3^2 + 5^3 = 135

# We need a function to collect these numbers, that may receive two integers aaa, bbb that defines the range [a,b][a, b][a,b] (inclusive) 
# and outputs a list of the sorted numbers in the range that fulfills the property described above.

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    sumList = []
    for i in range(a,b+1):
        sumN = 0
        if i < 10:
            sumList.append(i)
        else:
            numStr = [int(x) for x in list(str(i))]
            for n in range(len(numStr)):
                sumN = sumN +pow(numStr[n],n+1)
            if i==sumN:
                sumList.append(i)
                print(sumN)
    return sumList

print(sum_dig_pow(1,100))