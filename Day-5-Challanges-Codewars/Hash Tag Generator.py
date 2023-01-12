def hashtag(s):
    s = 'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'
    hashStr = ""
    if len(s) > 0 and len(s) <140 :
        splitStr = [(s.capitalize()) for s in s.split()]
        hashStr = "#"+"".join(splitStr)
        return hashStr
    else:
        return False