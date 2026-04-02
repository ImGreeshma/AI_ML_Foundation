import requests
import json
import pandas as pd

try:
   
    url = "https://restcountries.com/v3.1/all?fields=common_name,population,region,area"
    response = requests.get(url)
    status_code = response.status_code
    print(f"Status Code: {status_code}")

    if (status_code == 200):
        data = response.json()
        # print(data)
        print(f"Total Contries: {len(data)}")
    
    else:
        print("Failed to fetch data")

except Exception as e:
    print("Error:", e)


countries_list = []

for country in data:
    name = country.get("name", {}).get("common", "Unknown")
    population = country.get("population", 0)
    region = country.get("region", "Unknown")
    area = country.get("area", 0)

    countries_list.append({
        "common_name": name,
        "population": population,
        "region": region,
        "area": area
    })

df = pd.DataFrame(countries_list)

print("\nFirst 10 rows:")
print(df.head(10))

region_population = df.groupby("region")["population"].sum()
top_region = region_population.idxmax()

# 2. Country with largest area
largest_country = df.loc[df["area"].idxmax(), "common_name"]

print("\nSummary Results:")
print("Region with highest population:", top_region)
print("Country with largest area:", largest_country)






