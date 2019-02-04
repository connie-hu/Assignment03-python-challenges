# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period


# import the libraries
import os
import pandas as pd
import numpy as np


# path of the file
path = os.path.join("../budget-data.csv")

# use panda dataframe to split the csv by commas  and store the dataframe into "df"
csvreader = pd.read_csv(path, delimiter = ',')
df = pd.DataFrame(csvreader)

# define a function to store all calcs
def calcs():
    
    # since df variable is defined as a dataframe(made of a bunch of series),
    # define the dates and profits_losses as separate series (list) before doing any calcs.
    dates = df['Date']
    profits_losses = df['Profit/Losses']
    
    # The total number of months included in the dataset
    total_mnths = dates.nunique()
    
    # The net total amount of "Profit/Losses" over the entire period
    total_profit_losses = profits_losses.sum()
    
    # diff needed to calc the "rolling" difference of profit/losses
    diff = profits_losses.diff(periods = 1)
    
    # The average of the changes in "Profit/Losses" over the entire period
    rollavg_profit_losses = np.around(diff.mean(), decimals = 2)
    
    # The greatest increase in profits (date and amount) over the entire period
    max_profit_losses = int(diff.max())
    max_mnth = dates[profits_losses.idxmax()]
    
    # The greatest decrease in losses (date and amount) over the entire period
    min_profit_losses = int(diff.min())
    min_mnth = dates[profits_losses.idxmin()]
    
# write outputs to a txt file and print outputs


    with open("Financial_Analysis.txt",'w') as output_file:
        #put the output into a string so the text can be used for writing to a text file and to be able to print.
        output = str("Financial Analysis"
                          '\n' "---------------------------------------------------------"
                          '\n' f"Total Months: {total_mnths}"
                          '\n' f"Total: ${total_profit_losses}"
                          '\n' f"Mean Change: ${rollavg_profit_losses}"
                          '\n' f"Greatest Increase in Profits: {max_mnth} ${max_profit_losses}"
                          '\n' f"Greatest Decrease in Profits: {min_mnth} ${min_profit_losses}"
                         )
        
        #write the output into the Financial_Analysis.txt file.
        output_file.write(output)
        
        print(output)
    
    pass

calcs()
