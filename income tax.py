#title of the code
print('\nCOMPUTING THE INCOME TAX FOR THE GIVEN INCOME.\n')

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