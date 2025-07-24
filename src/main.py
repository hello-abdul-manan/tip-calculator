print('\nTip Calculator')

# Get inputs
bill = float(input('Enter bill amount $: '))
tip_percent = float(input('Enter tip %: '))
people = int(input('Number of people to split: '))

# Calculate tip and per person amount
tip = bill * tip_percent / 100
total = bill + tip
per_person = total / people

# Show result
print('----------')
print('Tip: $' + str(round(tip, 2)))
print('Total: $' + str(round(total, 2)))
print('Each person should pay: $' + str(round(per_person, 2)))
