cities = [
    {"name": "New York", "Country": "ABD", "Population": "8.538 million"},
    {"name": "İstanbul", "Country": "Turkey", "Population": "15.03 million :P"},
    {"name": "Ankara", "Country": "Turkey"},
]

for city in cities:
    print("City: {0} - Country: {1} - Population: {2}"
          .format(city.get("name", "Not Found Name Information"),
                  city.get("Country", "Not Found Country Information"),
                  city.get("Population", "Not Found Population Information")))

print("Try start...")
# try except
try:
    cities[2]["Population"]
    total_population = 5 + cities[0]["population"]
except KeyError:
    print("Error finding Population")
except TypeError:
    print("I can't add these two together!")
print("This code executes!")

