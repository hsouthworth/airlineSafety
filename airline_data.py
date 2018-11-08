
import pandas
import matplotlib

flight_data = pandas.read_csv('airline-safety.csv')


# There are two different timelines within this data
# The first timeline is from 1985-1999 and the second timeline is from 2000-2014
# So the first thing im going to do is to split these two timelines into their own dataframes

flight_85_99 = flight_data.drop(['incidents_00_14','fatal_accidents_00_14','fatalities_00_14'], axis=1)

flight_00_14 = flight_data.drop(['incidents_85_99','fatal_accidents_85_99','fatalities_85_99'], axis=1)

# Next, I want to show the summary statistics of all the airlines for each timeline

print("For airlines from 1985-1999\n")
for i in ['avail_seat_km_per_week', 'incidents_85_99',
       'fatal_accidents_85_99', 'fatalities_85_99']:
    print("The average " + i + " of all airlines is: " + str(flight_85_99[i].mean()))

print("\n")

print("For airlines from 2000-2014\n")
for i in ['avail_seat_km_per_week', 'incidents_00_14',
       'fatal_accidents_00_14', 'fatalities_00_14']:
    print("The average " + i + " of all airlines is: " + str(flight_00_14[i].mean()))


# Next, I want to find the statistics from each airline in each timeline

for i in range(56):
    print("Name: " + flight_85_99["airline"].loc[i])   