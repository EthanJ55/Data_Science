import os
import csv

with open(os.path.join(os.path.dirname(__file__), 'data_sets_new.csv')) as csvFile:
    rows = csv.reader(csvFile)
    with open(os.path.join(os.path.dirname(__file__), 'data_final.csv'), 'w') as f:
        writer = csv.writer(f)
        count = 0
        for row in rows:
            temp = row[0]
            if count != 0:
                temp = temp[0: len(temp) - 2]
            row[0] = row[1]
            row[1] = temp
            writer.writerow(row)
            count += 1
