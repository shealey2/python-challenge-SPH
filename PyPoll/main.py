import os
import csv


#change file path if necessary 
csvpath = os.path.join('c:/Users/Sean & Lauren/DataClass/python-challenge-SPH/PyPoll/','Resources','election_data.csv')
output_path = os.path.join('c:/Users/Sean & Lauren/DataClass/python-challenge-SPH/PyPoll/','analysis','analysis.txt')

votes_cast = 0
candidates = []
candidates_votes = []


#Reads csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Removed Header
    next(csvreader, None)

    for row in csvreader: 

        #counts all the rows in the csv
        votes_cast += 1
        
        #fills array with candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_votes.append(0)
        
        for x in range(len(candidates)):
            if(candidates[x]==row[2]):
                candidates_votes[x]+=1


            




print(votes_cast)
print(candidates)
print(candidates_votes)