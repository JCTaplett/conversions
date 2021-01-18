
import csv
import json

with open('input.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

json_data = []
for row in rows:

    item =  {
        'title': row['title'],
        'subtitle': row['subtitle'],
        'ranges': [
            float(row['range_min']),
            float(row['range_mid']),
            float(row['range_max'])],
        'measures': [
            float(row['measure_min']),
            float(row['measure_max'])],
        'markers': [float(row['markers'])]
    }
    json_data.append(item)

with open('output.json', 'w') as jsonfile:
    json.dump(json_data, jsonfile, indent=4)
