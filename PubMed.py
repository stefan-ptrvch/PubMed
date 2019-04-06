import pandas as pd
import pycountry
import json
from math import pi
from bokeh.io import output_file, show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.embed import components
from collections import defaultdict, Counter

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

# List of relationships between cities
relationships = []

# REMOVE NUM CITIES AFTERWARD
NUM_CITIES = 1000
THRESHOLD = 1

for x in d['country'][:NUM_CITIES]:

    # Get rid of '.'
    x = x.replace('.', '')

    # One relationship
    relationship = set()

    # Split different universities
    for y in x.split(';'):

        # Split strings in title of uni, to extract city
        for z in y.split(','):
            # Strip any whitespace
            z = z.strip()
            if 'USA' in z:
                z = 'United States'

            if 'Korea' in z:
                continue

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
            special_words = ['Research', 'University', 'Clinic', 'School',
                             'Faculty', 'College', 'Healthcare', 'Pharmacy',
                             'Center', 'Faculté', 'Patients', 'Hôpital',
                             'Partners', 'Veteran']
            cont = False
            for word in special_words:
                if word in z:
                    cont = True
                    break
            if cont:
                continue

            # Check if string is allcaps
            allcaps = False
            for word in z.split(" "):
                if word.isupper():
                    allcaps = True
                    break
            if allcaps:
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

            # Add the city to the relationship set
            relationship.add(z)

        # Add the relationship to the list
        if len(relationship) == 2:
            relationships.append(frozenset(relationship))


# Count the relationships
relationships = Counter(relationships)

# Sort in descending order, and take most frequent
relationships = sorted(relationships.items(), key=lambda x: x[1], reverse=True)
relationships = [x for x in relationships if x[1] > 4]

# Sort and filter out some cities
sorted_city_list = sorted(city.items(), key=lambda x: x[1], reverse= True)
city_list_top = [x for x in sorted_city_list if x[1] > THRESHOLD]

# Generate json for d3 graph plot
graph_data = {
        'nodes': [],
        'links': []
        }
city_list_top_ = [city[0] for city in city_list_top]
for city in city_list_top:
    for rel in relationships:
        if city[0] in rel[0]:
            both_cities = list(rel[0])
            if both_cities[0] in city_list_top_ and both_cities[1] in city_list_top_:
                if not city[0] in graph_data['nodes']:
                    graph_data['nodes'].append(city)
                graph_data['links'].append(rel[0])

# Reformat data a bit
graph_data['links'] = list(set(graph_data['links']))
graph_data['nodes'] = list(set(graph_data['nodes']))

links = []
for link in graph_data['links']:
    links.append({
        'source': list(link)[0],
        'target': list(link)[1]
        })
graph_data['links'] = links

nodes = []
for node in graph_data['nodes']:
    nodes.append({
        'name': node[0],
        'num_pub': node[1]
        })
graph_data['nodes'] = nodes

# Write out .json
filename = 'cities.json'
with open(filename, 'w') as f:
    json.dump(graph_data, f)


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

print('###########################################################')
script, div = components(p)
print(script)
print(div)

#  show(p)


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

print('###########################################################')
script, div = components(p)
print(script)
print(div)

#  show(p)
