print('Welcome to the tip calculator.')
total_bill = float(input('What was the total bill? $'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people_to_split = int(input('How many people to split the bill? '))
end_bill = (total_bill + (total_bill * (tip_percentage / 100))) / people_to_split

print(f'Each person should pay: ${end_bill:.2f}')
end_bill = '{:.2f}'.format(end_bill)
print(end_bill)