gross_income = int(input("Enter the gross income amount?"))
tax_group_a = gross_income * 0.05
tax_group_b = gross_income * 0.16
tax_group_c = gross_income * 0.19
tax_group_d = gross_income * 0.30

if (gross_income <= 100000):
    print("Gross Income:", gross_income)
    print("Net Income:", gross_income - tax_group_a)

elif (gross_income > 100000) & (gross_income < 150000):
    print("Gross Income:", gross_income)
    print("Net Income:", gross_income - tax_group_b)

elif (gross_income >= 150001) & (gross_income <= 300000):
    print("Gross Income:", gross_income)
    print("Net Income:", gross_income - tax_group_c)

else:
    print("Gross income",gross_income)
    print("Net income",gross_income - tax_group_d)



