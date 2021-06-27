import os
import csv

csvpath = os.path.join('c:/Users/Sean & Lauren/DataClass/python-challenge-SPH/PyBank/','Resources','budget_data.csv')



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    num_months = 0
    sum_profit = 0

    next(csvreader, None)
    for row in csvreader:
       
        num_months += 1
        sum_profit += float(row[1])
    
    print(f"Financial Analysis")
    print(f"......................................")
    print(f"Total Months: {num_months}")
    print(f"Total: {'${:,.2f}'.format(sum_profit)}")

        