# Script to add values to a tally.

# initialize total
total = 0

# initialize value input
value_in = '0'

# initial instructions
print('Type an amount to add or x to exit.')

# loop until 'x' is entered
while value_in != 'x':
    # convert input to number and add onto total
    value = float(value_in)
    total = total + value

    # output the new total and prompt for next input
    print(f'Total={total}')
    print("")
    value_in = input('Add:')