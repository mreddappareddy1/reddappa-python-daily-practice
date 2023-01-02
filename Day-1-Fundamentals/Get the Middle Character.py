# You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

# #Examples:

# Kata.getMiddle("test") should return "es"

# Kata.getMiddle("testing") should return "t"

# Kata.getMiddle("middle") should return "dd"

# Kata.getMiddle("A") should return "A"
import math
def get_middle(s):
    sLen = len(s)
    index = math.floor(sLen/2)
    outS = ""
    if sLen%2 == 0:
        outS = s[index-1:index+1]
    else:
        outS = s[index]
    return outS

s = 'fdSPz'
sLen = len(s)
index = math.floor(sLen/2)
outS = ""
print("start:{0} - {3}, mid:{1} - {4}, end:{2}-{5}".format(index-1,index,index+1,s[index-1],s[index],s[index+1]))
if sLen%2 == 0:
    outS = s[index-1:index+1]
else:
    outS = s[index-1]
print(outS)