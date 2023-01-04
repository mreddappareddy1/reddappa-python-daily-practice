# The goal of this exercise is to convert a string to a new string where 
# each character in the new string is "(" if that character appears
#  only once in the original string, or ")" 
# if that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a duplicate.

# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

def duplicate_encode(word):
    outString = []
    lst = [word.lower().count(c) for c in list(word.lower())]
    for n in lst:
        if n == 1:
            outString.append('(')
        else:
            outString.append(')')
    outString = "".join(outString)
    return outString

print(duplicate_encode("Success"))