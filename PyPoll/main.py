# Assignment03 - pythong part 2

# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv
import pandas as pd
import numpy

# path of csv file
path = ("../election_data.csv")

# use panda dataframe to split the csv by commas  and store the dataframe into "df"
csvreader = pd.read_csv(path)
df = pd.DataFrame(csvreader)

#define a function
def vote_status():
    # calculations
    total_votes = df['Candidate'].count()
    candidate_list = df['Candidate'].unique()
    candidate_vt_counts = df['Candidate'].value_counts()
    candidate_prcnt = candidate_vt_counts / total_votes * 100
    most_votes = df['Candidate'][df['Candidate'].value_counts().max()]
    
    #output variable needed here since need to print results in terminal and file. 
    output = ("Election Results\n"
              '-------------------------\n'
              f"Total Votes: {total_votes}\n"
              '-------------------------\n'
             )
    
    # use a for loop to get the correct formafor each candidate.
    for candidate in candidate_list:        
        output = output + f"{candidate}: {candidate_prcnt[candidate]:.3f}% ({candidate_vt_counts[candidate]})\n"
    
    
    output = output + ('-------------------------\n'
                       f"Winner: {most_votes}\n"
                       '-------------------------'
                      )
    # return is used instead of 'pass' because of the for loop that cannot simply be written into a text file.
    return output

results = vote_status()

with open("Candidates_Reults.txt",'w') as output_file:
    output_file.write(results)

print(results)
