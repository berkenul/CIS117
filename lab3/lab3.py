# CIS-117 Lab3
# This program reads a csv file with countries and makes a new file for each region
# Berk Enul
# I worked alone on this

import csv
import os

countries_by_region = {}

try:
    os.makedirs("output", exist_ok=True)

    # open the csv file and read it
    with open("country_full.csv", "r", encoding="utf-8") as source:
        reader = csv.DictReader(source)

        # check that the file has name and region columns
        if "name" not in reader.fieldnames or "region" not in reader.fieldnames:
            raise ValueError("Expected 'name' and 'region' columns.")

        for row in reader:
            name = row["name"].strip()
            region = row["region"].strip()

            if not name or not region:
                continue

            # add the country to its region
            if region not in countries_by_region:
                countries_by_region[region] = []
            countries_by_region[region].append([name, region])

    # make a file for each region and write the countries in it
    for region, countries in countries_by_region.items():
        filename = "output/" + region + ".CSV"
        with open(filename, "w", newline="", encoding="utf-8") as output:
            writer = csv.writer(output)
            writer.writerow(["name", "region"])
            writer.writerows(countries)

        print("Created " + filename)

except FileNotFoundError as error:
    print("File not found: " + str(error.filename))
except PermissionError as error:
    print("Permission denied: " + str(error.filename))
except OSError as error:  # OSError covers IOError too in python 3
    print("File error: " + str(error))
except ValueError as error:
    print("CSV error: " + str(error))
