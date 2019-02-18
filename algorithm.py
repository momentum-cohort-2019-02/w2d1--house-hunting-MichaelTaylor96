current_savings = 0
months = 0

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to be saved, as a decimal: "))
r = input("Enter the expected annual rate of return [0.04]: ")

if r == "no":
    r = 0.04
else:
    r = float(r)

total_cost = float(input("Enter the total cost of your dream home: "))
portion_down_payment = input("Enter the percent of your home's cost to save as a down payment [0.25]: "
)

if portion_down_payment == "no":
    portion_down_payment = 0.04
else:
    portion_down_payment = float(portion_down_payment)

while current_savings < (total_cost * portion_down_payment):
    current_savings = (current_savings*(1+(r/12))) + (annual_salary*(portion_saved)/12)
    months = months + 1

else :
    print("Number of months: " + str(months))