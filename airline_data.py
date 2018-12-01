
import pandas
import matplotlib.pyplot

flight_data = pandas.read_csv('airline-safety.csv')


# There are two different timelines within this data
# The first timeline is from 1985-1999 and the second timeline is from 2000-2014
# So the first thing im going to do is to split these two timelines into their own dataframe

flight_85_99 = flight_data.drop(['incidents_00_14','fatal_accidents_00_14','fatalities_00_14'], axis=1)

flight_00_14 = flight_data.drop(['incidents_85_99','fatal_accidents_85_99','fatalities_85_99'], axis=1)

# Next, I want to show the summary statistics of all the airlines for each timeline

print("For Airlines from 1985-1999\n")
for i in ['incidents_85_99',
       'fatal_accidents_85_99', 'fatalities_85_99']:
    names = i.split("_")
    attrib = ""
    for j in range(len(names)-1):
        if names[j].isalpha():
            attrib += " " + names[j]
    avg = flight_85_99[i].mean()
    print("The average number of" + attrib + " is: %.2f per year" % (avg/15))

print("\n")

# Next, I want to show the top and bottom 3 airlines from 1985-1999 for each column

print("Top 3 Airlines in number of Incidents:\n")
topthree = flight_85_99[flight_85_99['incidents_85_99'] < flight_85_99['incidents_85_99'].quantile(.06)].sort_values(by='incidents_85_99')
count = 1
for lines in topthree['airline']:
    print(str(count) + ". " + lines.strip("*"))
    count = count + 1

print("\n")

print("Bottom 3 Airlines in number of Incidents:\n")
bottomthree = flight_85_99[flight_85_99['incidents_85_99'] > flight_85_99['incidents_85_99'].quantile(.95)].sort_values(by='incidents_85_99',ascending=False)
count = 1
for lines in bottomthree['airline']:
    print(str(count)+". "+lines.strip("*"))
    count = count+1

print("\n")

print("Top 3 Airlines in number of Fatal Accidents:\n")
topthree = flight_85_99[flight_85_99['fatal_accidents_85_99'] < flight_85_99['fatal_accidents_85_99'].quantile(.30)].sort_values(by='fatal_accidents_85_99')
count = 1
print()
for lines in topthree['airline']:
    if count==4:
        break
    print(str(count) + ". " + lines.strip("*"))
    count = count + 1

print("\n")

print("Bottom 3 Airlines in number of Fatal Accidents:\n")
bottomthree = flight_85_99[flight_85_99['fatal_accidents_85_99'] > flight_85_99['fatal_accidents_85_99'].quantile(.95)].sort_values(by='fatal_accidents_85_99', ascending=False)
count = 1
for lines in bottomthree['airline']:
    print(str(count) + ". " + lines.strip("*"))
    count = count + 1

print("\n")

print("Top 3 Airlines in number of Fatalities:\n")
topthree = flight_85_99[flight_85_99['fatalities_85_99'] < flight_85_99['fatalities_85_99'].quantile(.30)].sort_values(by='fatalities_85_99')
count = 1
print()
for lines in topthree['airline']:
    if count==4:
        break
    print(str(count) + ". " + lines.strip("*"))
    count = count + 1

print("\n")

print("Bottom 3 Airlines in number of Fatalities:\n")
bottomthree = flight_85_99[flight_85_99['fatalities_85_99'] > flight_85_99['fatalities_85_99'].quantile(.95)].sort_values(by='fatalities_85_99', ascending=False)
count = 1
for lines in bottomthree['airline']:
    print(str(count) + ". " + lines.strip("*"))
    count = count + 1

print("\n")
print("For airlines from 2000-2014\n")
for i in ['incidents_00_14',
       'fatal_accidents_00_14', 'fatalities_00_14']:
    names = i.split("_")
    attrib = ""
    for j in range(len(names) - 1):
        if names[j].isalpha():
            attrib += " " + names[j]
    avg = flight_00_14[i].mean()
    print("The average number of" + attrib + " is: %.2f per year" % (avg / 15))

print(" ")

print("Top 3 Airlines in number of Incidents:\n")
topthree = flight_00_14[flight_00_14['incidents_00_14'] < flight_00_14['incidents_00_14'].quantile(.15)].sort_values(by='incidents_00_14')
count = 1
for lines in topthree['airline']:
    if count==4:
        break
    print(str(count) + ". " + lines.strip("*"))
    count = count + 1

print("\n")

print("Bottom 3 Airlines in number of Incidents:\n")
bottomthree = flight_00_14[flight_00_14['incidents_00_14'] > flight_00_14['incidents_00_14'].quantile(.95)].sort_values(by='incidents_00_14', ascending=False)
count = 1
for lines in bottomthree['airline']:
    print(str(count)+". "+lines.strip("*"))
    count = count+1

print("\n")

print("Top 3 Airlines in number of Fatal Accidents:\n")
topthree = flight_00_14[flight_00_14['fatal_accidents_00_14'] < flight_00_14['fatal_accidents_00_14'].quantile(.60)].sort_values(by='fatal_accidents_00_14')
count = 1
print()
for lines in topthree['airline']:
    if count==4:
        break
    print(str(count) + ". " + lines.strip("*"))
    count = count + 1

print("\n")

print("Bottom 3 Airlines in number of Fatal Accidents:\n")
bottomthree = flight_00_14[flight_00_14['fatal_accidents_00_14'] > flight_00_14['fatal_accidents_00_14'].quantile(.60)].sort_values(by='fatal_accidents_00_14', ascending=False)
count = 1
for lines in bottomthree['airline']:
    if count==4:
        break
    print(str(count) + ". " + lines.strip("*"))
    count = count + 1

print("\n")

print("Top 3 Airlines in number of Fatalities:\n")
topthree = flight_00_14[flight_00_14['fatalities_00_14'] < flight_00_14['fatalities_00_14'].quantile(.60)].sort_values(by='fatalities_00_14')
count = 1
print()
for lines in topthree['airline']:
    if count==4:
        break
    print(str(count) + ". " + lines.strip("*"))
    count = count + 1

print("\n")

print("Bottom 3 Airlines in number of Fatalities:\n")
bottomthree = flight_00_14[flight_00_14['fatalities_00_14'] > flight_00_14['fatalities_00_14'].quantile(.95)].sort_values(by='fatalities_00_14', ascending=False)
count = 1
for lines in bottomthree['airline']:
    print(str(count) + ". " + lines.strip("*"))
    count = count + 1