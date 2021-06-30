import os
import csv


#change file path if necessary 
csvpath = os.path.join('Resources','election_data.csv')
output_path = os.path.join('analysis','analysis.txt')

votes_cast = 0
candidates = []
candidates_votes = []
candidates_percent = []
highest_vote = 0
winning_candidate = ""


#Reads csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Removed Header
    next(csvreader, None)

    for row in csvreader: 

        #counts all the rows in the csv
        votes_cast += 1
        
        #fills array with candidates and creates arrays with 0 values for other variables
        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_votes.append(0)
            candidates_percent.append(0)
        
        #counts votes per each candidate
        for x in range(len(candidates)):
            if(candidates[x]==row[2]):
                candidates_votes[x]+=1
    
    for y in range(len(candidates)):
        candidates_percent[y]=candidates_votes[y]/votes_cast
        if(candidates_votes[y]>highest_vote):
            highest_vote=candidates_votes[y]
            winning_candidate=candidates[y]


    


            



print("Election Results")
print(".................................")
print(f"Total Votes: {votes_cast}")
print(".................................")
print(candidates)
print(candidates_votes)
print(candidates_percent)
print(".................................")
print(f"Winner: {winning_candidate}")