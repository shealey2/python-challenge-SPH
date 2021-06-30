import os
import csv


csvpath = os.path.join('c:/Users/Sean & Lauren/DataClass/python-challenge-SPH/PyBank/','Resources','budget_data.csv')
output_path = os.path.join('c:/Users/Sean & Lauren/DataClass/python-challenge-SPH/PyBank/','analysis','analysis.txt')

#variable for total month
num_months = 0
#variable for total profit
sum_profit = 0   
#variables for average change
first_month = 0
last_month = 0
pre_month = 0
cur_month = 0
#variables for greatest increase
great_inc = 0
great_month = ""
#variables for greatest decrease
great_dec = 0
worst_month = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Removed Header
    next(csvreader, None)
   
    #Runs Through Rows
    for row in csvreader: 
    
        #sets cur_month value
        cur_month = row[1]

       #adds 1 to for every row it reads
        num_months += 1  

        #takes a cumulative profit of every row it reads
        sum_profit += float(row[1])

        #defines the first and last month profit value
        if(num_months==1):
            first_month = float(row[1])
        
        last_month = float(row[1])

       
        #determines if this month profit was greater than the previous greatest and stores month and profit
        if(float(cur_month)-float(pre_month)>great_inc):
            great_inc = float(cur_month)-float(pre_month)
            great_month = str(row[0])
        
        #determines if this month profit was less than the previous greatest and stores month and profit
        if(float(cur_month)-float(pre_month)<great_dec):
            great_dec = float(cur_month)-float(pre_month)
            worst_month = str(row[0])
    
        #now that code has run set cur_month to pre_month
        pre_month = cur_month

   
#calculates the average change across months
avg_change = (last_month - first_month) / (num_months - 1)    
 


#print to console and write to txt file
file1 = open(output_path, 'w')
file1.write(f"Financial Analysis\n")
file1.write(f"......................................\n")
file1.write(f"Total Months: {num_months}\n")
file1.write(f"Total: {'${:,.2f}'.format(sum_profit)}\n")
file1.write(f"Average Change: {'${:,.2f}'.format(avg_change)}\n")
file1.write(f"Greatest Increase in Profits: {great_month} ({'${:,.2f}'.format(great_inc)})\n")
file1.write(f"Greatest Increase in Profits: {worst_month} ({'${:,.2f}'.format(great_dec)})\n")
file1.close()


print(f"Financial Analysis")
print(f"......................................")
print(f"Total Months: {num_months}")
print(f"Total: {'${:,.2f}'.format(sum_profit)}")
print(f"Average Change: {'${:,.2f}'.format(avg_change)}")
print(f"Greatest Increase in Profits: {great_month} ({'${:,.2f}'.format(great_inc)})")
print(f"Greatest Increase in Profits: {worst_month} ({'${:,.2f}'.format(great_dec)})")