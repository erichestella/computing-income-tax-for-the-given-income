#title of the code
print('\nCOMPUTING THE INCOME TAX FOR THE GIVEN INCOME.\n')

#given income tax and rate
print('\nTAXABLE INCOME:\nFirst $10,000\nNext $10,000\nThe remaining')
print('\nRate (in %):\n    0\n    10\n    20\n')


#your designated income
income = int(input('YOUR INCOME : '))

#variable to illustrate the tax
tax_numerical = 0

#the income if it is less than 10000
if income <= 10_000:
   tax_digit = 0

#the income if its less than equal to 20000
elif 10_000 < income <= 20_000:
    first_income= income - 10_000
    tax_digit = first_income * 0.1

# if the given income is more than 20000 
else:
     tax_digit = 0
     tax_digit= 10000 * 0.1

     income > 20_000
     tax_digit+= (income- 20_000)* 0.2

#it displays the total income
print('\nTHE TOTAL TAX THAT YOU NEED TO PAY IS','$',int(tax_digit), '\n')