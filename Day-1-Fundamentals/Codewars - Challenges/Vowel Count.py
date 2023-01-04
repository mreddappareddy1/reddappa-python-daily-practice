# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    countVowels=0
    for i in list(sentence):
        if i in ['a','e','i','o','u']:
            countVowels=countVowels+1
    return countVowels


sentence = "Some Sample Sentence in the python program"
print(get_count(sentence))
