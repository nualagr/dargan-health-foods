# Initial code found at: https://pythonexamples.org/python-csv-to-json/
# and then modified

import csv
import json


def csv_to_json(csvFilePath, jsonFilePath):
    """
    Function to convert CSV to JSON.
    Takes the file paths as arguments.
    """
    # Create an empty list to hold the dicts
    jsonArray = []

    # Read the file
    with open(csvFilePath, encoding="utf-8-sig") as csvf:
        # Load the CSV-file data using CSV library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # Convert each CSV row into python dict
        for row in csvReader:
            # Create a new empty outer dict
            outRow = {}
            # Add a new subset dict called fields
            outRow["fields"] = {}
            for key, value in row.items():
                # Add 'name' and 'friendly_name' key value pairs
                # to the new subset dict
                if (
                    key == "name"
                    or key == "friendly_name"
                ):
                    outRow["fields"][key] = value
                # Add the other key value pairs to the outer dict
                else:
                    outRow[key] = value

            # Add this python dict to json array
            jsonArray.append(outRow)

    # Convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, "w", encoding="utf-8") as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


# File paths
csvFilePath = r"./blog/fixtures/topics.csv"
jsonFilePath = r"./blog/fixtures/topics.json"

# Call the csv_to_json function
csv_to_json(csvFilePath, jsonFilePath)
