squares = [1,1,2]
def generateFibonacci(n):
    i = 0
    j = 1
    counter = 1
    series = [j,]
    while counter <= n:
        k = j
        j = i+j
        i = k
        series.append(j)
        counter = counter+1
    if n==0:
        return [0]
    elif n==1:
        return [1]
    else:
        return series
outSeries = generateFibonacci(7)
peri = sum(4*x for x in outSeries)