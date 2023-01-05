def count_smileys(arr):
    smileyCount = 0
    for smileys in arr:
        if list(str(smileys))[0] in [':',';']:
            if list(str(smileys))[1] in ['-','~',')','D']:
                if list(str(smileys))[-1] in [')','D']:
                    print(list(smileys))
                    smileyCount = smileyCount +1
    return smileyCount #the number of valid smiley faces in array/list

print(count_smileys([';)',':-X',':-D']))