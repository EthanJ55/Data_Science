import os
import csv

with open(os.path.join(os.path.dirname(__file__), 'result.csv')) as csvFile:
    rows = csv.reader(csvFile)
    with open(os.path.join(os.path.dirname(__file__), 'temp.csv'), 'w') as f:
        writer = csv.writer(f)
        for row in rows:
            date = row[0]
            formal = '2020/' + date[:2] + '/' + date[2: 4]
            row[0] = formal
            writer.writerow(row)
