import csv
import datetime

INPUT_DATE_FORMAT = '%Y-%m-%d'
OUTPUT_DATE_FORMAT = "%-d-%b-%y"

with open('input.txt') as f:
    lines = f.read().splitlines()[15:]

with open('output.tsv', 'w') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerow(['date', 'close'])

    for line in lines:
        date, value = line.split()
        parsed_date = datetime.datetime.strptime(date, INPUT_DATE_FORMAT)
        output_date = parsed_date.strftime(OUTPUT_DATE_FORMAT)
        
        if parsed_date.year < 1970:
            continue

        writer.writerow([output_date, value])
