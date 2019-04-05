import pandas as pd
import pycountry
from math import pi
from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
from collections import defaultdict

output_file("pie.html")

# Read the data
d = pd.read_csv('pubmed16.csv')

# Drop non-existing Country information
d.dropna(inplace=True, subset=['country'])

# Drop the 1st 40 entries, since they're differently formatted (by hand)
d = d[40:]

# Get the city and country occurances
city = defaultdict(int)
city_list = set([])
country_list = []

# REMOVE NUM CITIES AFTERWARD
NUM_CITIES = 1000
THRESHOLD = 10
for x in d['country'][:NUM_CITIES]:

    # Get rid of '.'
    x = x.replace('.', '')

    # Split different universities
    for y in x.split(';'):
        # Split strings in title of uni, to extract city
        for z in y.split(','):
            # Strip any whitespace
            z = z.strip()
            if 'USA' in z:
                z = 'United States'

            # Check if it has numbers
            if any(char.isdigit() for char in z):
                continue

            # Check if it's more than 3 words
            if z.count(' ') > 2:
                continue

            # Check if the length is not too big or too short
            if len(z) > 20 or len(z) < 3:
                continue

            # Drop if it contains some special words
            if 'University' in z or 'Faculty' in z or 'Clinic' in z or 'School' in z:
                continue

            # Check if it's a country
            if not z in country_list:
                try:
                    pycountry.countries.lookup(z)
                    country_list.append(z)
                    continue
                except:
                    pass
            else:
                country_list.append(z)
                continue
            city[z] += 1
            city_list.add(z)

# Sort and filter out some cities
sorted_city_list = sorted(city.items(), key=lambda x: x[1], reverse= True)
city_list_top = [x for x in sorted_city_list if x[1] > THRESHOLD]

# Get selected city list
unique_list = [x[0] for x in city_list_top]

# Adapt a little bit above code to get all the cities with their cooperation cities
relat = {}

for x in unique_list:
    relat[x] = defaultdict(int)

for x in d['country'][:NUM_CITIES]:
    x = x.replace('.','')
    temp = []
    for y in x.split(';'):
        temp.append(y.strip())

    for z in temp:
        if z in unique_list:
            for m in temp:
                if m != z and m in unique_list:
                    relat[z][m] += 1

# Calcualte how many cooperation cities each city has
temp = sorted(relat.items(), key = lambda x:len(x[1]), reverse = True)


# Plot pie chart
country_count = {i:country_list.count(i) for i in set(country_list)}
data = pd.Series(country_count).reset_index(name='value').rename(columns={'index':'country'})
# Take top 10 values
NUM_TO_DISPLAY = 10
data = data.nlargest(NUM_TO_DISPLAY, 'value')
data['angle'] = data['value']/data['value'].sum()*2*pi
data['color'] = Category20c[NUM_TO_DISPLAY]
p = figure(plot_height=350, title="Number of Papers Published by Countries in Clinical NLP", toolbar_location=None,
           tools="hover", tooltips="@country: @value", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend='country', source=data)

p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

show(p)


# Plot number of papers published each year
yearPub = [x.split()[0] for x in d['date']]

yearCount = defaultdict(int)
for y in yearPub:
    if y.isdigit():
        yearCount[y] += 1

countFrame = pd.DataFrame()
countFrame['Year'] = [int(x) for x in yearCount.keys()]
countFrame['Count'] = [int(x) for x in yearCount.values()]


# Plot bar chart
output_file("bar_sorted.html")

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]

# sorting the bars means sorting the range factors
sorted_fruits = sorted(fruits, key=lambda x: counts[fruits.index(x)])


p = figure(
        plot_height=350,
        title="Yearly Published Clinical NLP Papers",
        toolbar_location=None,
        tools="hover",
        tooltips="""
        <div>
          Year: @Year <br>
          Publications: @Count
        </div>
        """
        )

p.vbar(x='Year', top='Count', width=0.9, source=countFrame)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)


