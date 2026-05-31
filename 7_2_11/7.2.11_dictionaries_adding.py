mileage = {'John': 10000, 'Bert': 12000, 'Susan': 15000}
mileage['road_trip'] = {'Bert': 300} # adding a new key entry road_trip with a dictionary in it
print(mileage)

print("Icluding road trip, Bert's mileage:")
print("{:,} miles".format((mileage['Bert'] + mileage['road_trip']['Bert']))) # adding whatever is in the Bert entry plus the new dictionary road_trip which also has a Bert entry
