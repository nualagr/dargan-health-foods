# Initial code found at: https://pythonexamples.org/python-csv-to-json/
# and then modified
from datetime import datetime, timezone

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
    # Solution to removing the BOM found on Stack Overflow:
    # https://stackoverflow.com/questions/17912307/u-ufeff-in-python-string/17912811
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
                # Add the following key value pairs
                # to the fields subset dict
                if key == "name":
                    if value != "":
                        new_name = (
                            value.lower()
                            .strip()
                            .replace("-", "")
                            .replace("(", "")
                            .replace(")", "")
                            .replace("'", "")
                            .replace(".", "")
                            .replace("+", "_plus")
                            .replace("&", "n")
                            .replace(" ", "_")
                            .replace("__", "_")
                        )
                        outRow["fields"][key] = new_name
                elif key == "main_image":
                    if value != "":
                        if value.endswith(".jpg"):
                            image_name = "product_images/" + value
                        else:
                            image_name = "product_images/" + value + ".jpg"
                        outRow["fields"][key] = image_name
                elif (
                    key == "sku" or
                    key == "friendly_name" or
                    key == "abbreviated_friendly_name" or
                    key == "size_unit" or
                    key == "vat_code" or
                    key == "information" or
                    key == "ingredients" or
                    key == "allergens" or
                    key == "usage" or
                    key == "barcode"
                ):
                    if value != "":
                        outRow["fields"][key] = value.strip()
                elif (
                    key == "brand" or
                    key == "size_value" or
                    key == "weight_g" or
                    key == "category" or
                    key == "num_in_stock"
                ):
                    if value != "":
                        outRow["fields"][key] = int(value.strip())
                elif (
                    key == "price" or
                    key == "discount_price" or
                    key == "avg_rating"
                ):
                    if value != "":
                        outRow["fields"][key] = float(value.strip())
                elif (
                    key == "free_from" or
                    key == "on_offer" or
                    key == "discontinued"
                ):
                    if value == "TRUE":
                        outRow["fields"][key] = True
                    elif value == "FALSE":
                        outRow["fields"][key] = False
                elif key == "main_image_url":
                    outRow["fields"][key] = None
                elif key == "date_added":
                    # Solution to creating a timezone aware datetime
                    # found on StackOverflow:
                    # https://stackoverflow.com/questions/796008/cant-subtract-offset-naive-and-offset-aware-datetimes/25662061#25662061
                    now = datetime.now(timezone.utc)
                    # Make the datetime compatible with JSON
                    outRow["fields"][key] = now.isoformat()
                # Add the other key value pairs to the outer dict
                else:
                    if key == "pk" and value != "":
                        outRow[key] = int(value)
                    elif value != "":
                        outRow[key] = value

            # Add this python dict to json array
            jsonArray.append(outRow)

    # Convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, "w", encoding="utf-8") as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


# File paths
csvFilePath = r"./products/fixtures/products.csv"
jsonFilePath = r"./products/fixtures/products.json"

# Call the csv_to_json function
csv_to_json(csvFilePath, jsonFilePath)
