def move_zeros(lst):
    #zeroCounter = sum(1 for i in lst if i in [0])
    zeroCounter = 0
    for i in range(len(lst)):
        if lst[i] == 0:
            zeroCounter = zeroCounter+1
    lst = [x for x in lst if x != 0]
    for i in range(zeroCounter):
        lst.append(0)
    return lst

print(move_zeros([1,2,3,0,0,2,3,1]))
