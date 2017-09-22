#1)Given the list bank_holidays_in_month = [1, 0, 1, 1, 2, 0, 0, 1, 0, 0, 0, 2]
#where each element represent the number of bank holiday in a month,
#for example in January there is 1, in February 0, March there is 1 etc.
#Write a function called bank_holiday(), that takes a number to represent
#the month and return the number of bank holidays in that month.
#Example: bank_holiday(5) --> 2

bank_holidays_in_month = [1, 0, 1, 1, 2, 0, 0, 1, 0, 0, 0, 2]

def bank_holiday(number):
    return bank_holidays_in_month[number-1]

month = int(input("Please enter the number of the month to return bank holidays for "))

print(bank_holiday(month))
