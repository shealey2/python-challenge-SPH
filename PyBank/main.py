import os
import csv

csvpath = os.path.join('c:/Users/Sean & Lauren/DataClass/python-challenge-SPH/PyBank/','Resources','budget_data.csv')



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    num_months = 0

    next(csvreader, None)
    for row in csvreader:
       
        num_months += 1
    
        
    print(f"The total number of months is {num_months}.")
    print(f"")

        