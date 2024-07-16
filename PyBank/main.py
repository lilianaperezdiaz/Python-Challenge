import os
import csv
import pandas as pd 

#Accessing data file from folders
data_csv = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# Declaring empty lists to store profit/loss data and monthly changes
profloss = []
monthly_changes = []
prof_clist = []
# Opening data file
with open(data_csv) as csv_file:
    # Reading the CSV file
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Ignoring the headers of the file
    csv_header = next(csv_reader)
    # Reading the first row to initialize variables
    first_row = next(csv_reader)
    profloss.append(int(first_row[1]))
    prev_value = int(first_row[1])
    
    # Iterating through all rows in csv_reader
    row = 0
    for row in csv_reader:
        #Creating variable for value of current row in column 2 
        current_value = int(row[1])
        # Adding column 2 from file to profloss list
        profloss.append(current_value)
        
        
        # Calculating monthly change and adding to the list
        monthly_change = current_value - prev_value
        monthly_changes.append(monthly_change)
        prev_value = current_value
    
    #Calculating profit change and adding to the list
    for r in profloss:
        prof_change = abs(r - (r+1))
        prof_clist.append(prof_change)
        

# Net Total Profit/Loss
total = sum(profloss)

# Average Change in Profit/Loss
if len(monthly_changes) > 0:
    avgchange = sum(monthly_changes) / len(monthly_changes)
else:
    avgchange = 0

#Greatest Increase/Decrease in Profits
max_increase = max(prof_clist)
max_decrease = min(prof_clist)

# Printing Results
title = "Financial Analysis"
print(title)
breaker = "----------------------------"
print(breaker)
print(f"Total Months: {len(profloss)}")
print(f"Total: ${total}")
print(f"Average Change: ${avgchange:.2f}")
print(f'Greatest Increase in Profits: $({max_increase})')
print(f'Greatest Decrease in Profits: $({max_decrease})')
