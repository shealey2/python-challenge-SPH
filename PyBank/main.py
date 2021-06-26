import os
import csv

cwd = os.getcwd()
csvpath = os.path.join('c:/Users/Sean & Lauren/DataClass/python-challenge-SPH/PyBank/','Resources','budget_data.csv')



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        print(row[1])