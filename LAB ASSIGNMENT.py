#AbuBakr
#SP24-BBA-006
#LAB ASSIGNMENT

# Dictionary: Pakistani cities and their estimated population (in millions)
city_population = {
    "Karachi": 16.1,
    "Lahore": 11.1,
    "Faisalabad": 3.8,
    "Rawalpindi": 2.1,
    "Multan": 2.0,
    "Peshawar": 2.3,
    "Quetta": 1.1,
    "Hyderabad": 1.9,
    "Sialkot": 0.9,
    "Gujranwala": 2.0
}

# 1. get() – Get population of a specific city
print("1. Population of Lahore:", city_population.get("Lahore"))

# 2. keys() – List all city names
print("2. All cities:", list(city_population.keys()))

# 3. values() – List all population values
print("3. Populations (in millions):", list(city_population.values()))

# 4. items() – Get all key-value pairs
print("4. City-Population pairs:", list(city_population.items()))

# 5. update() – Add a new city or update existing population
city_population.update({"Islamabad": 1.2})
print("5. After adding Islamabad:", city_population)

# 6. pop() – Remove a city
removed = city_population.pop("Quetta")
print(f"6. Removed Quetta (Population {removed} million)")

# 7. popitem() – Remove the last added city (Islamabad in this case)
last = city_population.popitem()
print("7. Last city removed:", last)

# 8. setdefault() – Add city only if it doesn’t exist
city_population.setdefault("Bahawalpur", 0.8)
print("8. After adding Bahawalpur with setdefault:", city_population)

# 9. fromkeys() – Create new dictionary with default value
new_cities = ["Sukkur", "Mardan", "Abbottabad"]
default_pop = 0.5
new_city_dict = dict.fromkeys(new_cities, default_pop)
print("9. New cities with default population:", new_city_dict)

# 10. clear() – Empty the new city dictionary
new_city_dict.clear()
print("10. Cleared new city dictionary:", new_city_dict)
