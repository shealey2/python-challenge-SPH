import os
import csv

csvpath = os.path.join('c:/Users/Sean & Lauren/DataClass/python-challenge-SPH/PyBank/','Resources','budget_data.csv')



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    num_months = 0
    sum_profit = 0   
    month_change = 0
    first_month = 0
    last_month = 0
    
    #Removed Header
    next(csvreader, None)
   
    #Runs Through Rows
    for row in csvreader: 
        
       #adds 1 to for every row it reads
        num_months += 1  

        #takes a cumulative profit of every row it reads
        sum_profit += float(row[1])

        #defines the first and last month profit value
        if(num_months==1):
            first_month = float(row[1])
        
        last_month = float(row[1])
   
    #calculates the average change across months
    avg_change = (last_month - first_month) / (num_months - 1)    
 
    
    print(f"Financial Analysis")
    print(f"......................................")
    print(f"Total Months: {num_months}")
    print(f"Total: {'${:,.2f}'.format(sum_profit)}")
    print(f"Average Change: {'${:,.2f}'.format(avg_change)}")

        