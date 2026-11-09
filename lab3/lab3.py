# CIS-117 Lab3
# Reads country_full.csv and creates a CSV file for each region.
# Berk Enul

import csv
import os

countries_by_region = {}

try:
    os.makedirs("output", exist_ok=True)

    with open("country_full.csv", "r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)

        if not {"name", "region"}.issubset(reader.fieldnames or []):
            raise ValueError("Expected 'name' and 'region' columns.")

        for row in reader:
            name = (row["name"] or "").strip()
            region = (row["region"] or "").strip()

            if not name or not region:
                continue

            if region not in countries_by_region:
                countries_by_region[region] = []
            countries_by_region[region].append([name, region])

    for region, countries in countries_by_region.items():
        filename = "output/" + region + ".CSV"
        with open(filename, "w", encoding="utf-8", newline="") as output:
            writer = csv.writer(output)
            writer.writerow(["name", "region"])
            writer.writerows(countries)

        print("Created " + filename)

except FileNotFoundError as error:
    print("File not found: " + str(error.filename))
except PermissionError as error:
    print("Permission denied: " + str(error.filename))
except OSError as error:
    print("File error: " + str(error))
except (ValueError, csv.Error) as error:
    print("CSV error: " + str(error))
