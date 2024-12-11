# PyBank and PyPoll Analysis

## Overview 
Using python to analyze the financial records of a company and calcualte profits, losses, seaarch for increases and decreases. Using python we will also analyze the vote counting process using data from a small town. 

## PyBank
*Results*
<p> From our resutls we can see that the largest increated in profits occured in August while the largest decrease occured in Feburary. Over all the total fiancial change totaled to a decrease in $8311.11 over a total of 8 months. In order to find these results, all rows were iterated through and values were saved to the empty lists created. While iterating through rows and columns,the changes noticed in profits were being calcualted before appending value to assigned list. <p></p>
```
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
`````
<p>Once all of the information was added to its respective lists the profits and loss list was summed to find the totoal at the end of the time frame provided in the data. Conditionals were created to test if any new data was added to the monthly changes list to be able to recalculate average change.</p>         

```
# Net Total Profit/Loss
total = sum(profloss)

# Average Change in Profit/Loss
if len(monthly_changes) > 0:
    avgchange = sum(monthly_changes) / len(monthly_changes)
else:
    avgchange = 0
`````

<p> Once all of the data has been collected, the max and min integers in the profit list are searched to be able to print our final results. </p>
#Greatest Increase/Decrease in Profits
max_increase = max(prof_clist)
max_decrease = min(prof_clist)
```
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
`````
<img width="319" alt="image" src="https://github.com/user-attachments/assets/c6bee8fd-4cb8-400c-8568-1e1e82cd702d">


## PyPoll

*Results*
<p> From the resutls we can see the percentage of votes each candidate accumulated from the total 369,711 voters. The winner of the ellection is declared as Diana DeGette as she obtainied 73.81% of the vote with Charles Casper Stockham coming in second place with 23.05% of the votes and Raymon Anthony Doane coming in last place with 3.14% of the votes. <p></p>
<img width="276" alt="image" src="https://github.com/user-attachments/assets/0dac2004-b71d-4605-a893-1a89e1a70b2e">

