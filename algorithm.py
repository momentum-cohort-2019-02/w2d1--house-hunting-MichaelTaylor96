current_savings = 0
months = 0

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to be saved, as a decimal: "))
r = input("Enter the expected annual rate of return [0.04]: ")

try:
    r = float(r)
except ValueError:
    r = 0.04

total_cost = float(input("Enter the total cost of your dream home: "))
portion_down_payment = input("Enter the percent of your home's cost to save as a down payment [0.25]: "
)

try:
    portion_down_payment = float(portion_down_payment)
except ValueError:
    portion_down_payment = 0.25

while current_savings < (total_cost * portion_down_payment):
    current_savings = (current_savings*(1+(r/12))) + (annual_salary*(portion_saved)/12)
    months = months + 1

else :
    print("Number of months: " + str(months))