# # Primes in numbers
# Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.

# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
import math
def prime_factors(n):
    factorStr = ""
    uniquePrimeList = []
    primeFactor = []
    j = 2
    while n %j ==0 :
        uniquePrimeList.append(j)
        primeFactor.append(j)
        n = n/j
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i ==0:
            print(i)
            uniquePrimeList.append(i)
            primeFactor.append(i)
            n = n/i
    primeList = sorted(set(uniquePrimeList))
    occurences = [primeFactor.count(x) for x in sorted(primeList)] #if sorted(lst).count(x) > 0
    for i in range(len(primeList)):
        if occurences[i] > 1:
            factorStr =factorStr+ "({0}".format(primeList[i])+"**"+"{0})".format(occurences[i])
        else:
            factorStr =factorStr+ "({0})".format(primeList[i])
    return factorStr

print(prime_factors(7919))

# plst = [2,3,7]
# lst = [2, 2, 3, 7]
# outS = ""
# occurences = [lst.count(x) for x in sorted(plst)] #if sorted(lst).count(x) > 0
# for i in range(len(plst)):
#     if occurences[i] > 0:
#         outS =outS+ "({0}".format(occurences[i])+"**"+"{0})".format(plst[i])
# print(outS)
        #(2**5)(5)(7**2)(11)