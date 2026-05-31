mileage_totals = {'John': 10000, 'Bert': 12000, 'Susan': 15000}
mileage_extra = 300;
mileage_totals['John'] = mileage_totals['John'] + mileage_extra # Jonhs mileage will be their current total + the extra value
mileage_totals['Bert'] += mileage_extra # same as with john, less code
mileage_totals['Susan'] += mileage_extra
print(mileage_totals)
