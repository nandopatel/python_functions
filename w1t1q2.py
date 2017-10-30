def numcalc(num1,num2):
    diff = num2-num1
    finans = num1
    for i in range(1,diff):
        finans += num1+i
    return finans
