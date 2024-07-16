import csv
import pandas as pd
from pathlib import Path


#Accessing data file from folders
csv_file = Path("PyPoll/Resources/election_data.csv")
#Declaring lists
ballot = []
county = []
names = []
#Opening the data file 
with open(csv_file) as data_file:
    #Dataframe (data_reader) *created a dataframe to read csv file, should be reading with CSV
    data_reader = csv.reader(data_file, delimiter = ',')
    #Looping through data and adding columns to appropraite lists 
    for row in data_reader:

        ballot.append(row[0])
        county.append(row[1])
        names.append(row[2])


#Using lists to create a dataframe 
data_df = pd.DataFrame(
    {
        'Ballot ID' : ballot,
        'County' : county,
        'Candidates' : names
    })

#Declaring total votes
votes = len(data_df) - 1


#Searching dataframe for unique candidate names 
unique_names = data_df['Candidates'].unique()
print(unique_names)

#Percentage of votes per candidate
charles = [n for n in names if n == 'Charles Casper Stockham']
charles = len(charles)
charles_votes = round(((charles/votes)*100),3)

diana = [n for n in names if n == 'Diana DeGette']
diana = len(diana)
diana_votes = round(((diana/votes)*100),3)

raymon = [n for n in names if n == 'Raymon Anthony Doane']
raymon = len(raymon)
raymon_votes = round(((raymon/votes)*100),3)

#Calculating winner 
if charles > diana and charles > raymon:
    winner = 'Charles Casper Stockham'
elif diana > charles and diana > raymon:
    winner = 'Diana DeGette'
elif raymon > charles and raymon > diana:
    winner = 'Raymon Anthony Doane'
#Printing Results 
print('Election Results')
print("-------------------------")
print(f'Total Votes: {votes}')
print("-------------------------")
print(f'Charles Casper Stockham: {charles_votes}% ({charles})')
print(f'Diana DeGette: {diana_votes}% ({diana})')
print(f'Raymon Anthony Doane: {raymon_votes}% ({raymon})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")