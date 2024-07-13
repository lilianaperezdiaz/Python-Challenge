import os
import csv

data_csv = os.path.join('..', 'Resources', 'budget_data.csv')
with open(data_csv, encoding = 'ISO-8859-1') as csv_file:
    csv_reader = csv.reader(csv_file, deliminater = ",")
    csv_header = next(csv_file)
    print(f'Header : {csv_header}')

