# CTI-110
# M2HW2 - Tip Tax Total
# Brandon Dalton
# 9/10/2017
#
foodCost = float(input('Enter cost of the meal:$ '))
tipAmount = foodCost * .18
salesTax = foodCost * .07
totalCost = foodCost + salesTax + tipAmount
print('Tax - $', format(salesTax,',.2f'))

print('Tip - $', format(tipAmount,',.2f'))

print('Total - $', format(totalCost,',.2f'))
