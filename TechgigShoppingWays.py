def possibleways(input1):
    tempsum = 0
    for i in input1:
        tempsum += i
    finsum = 0
    for i in xrange(len(input1)):
        finsum += (i + 1) * tempsum * input1[i]
        tempsum -= input1[i]
        fin %= 10 ** 9 + 7
    return finsum
