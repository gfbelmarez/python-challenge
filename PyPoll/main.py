import os
import csv

election_data = os.path.join("./Resources","election_data.csv")
with open(election_data, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    vote_totals = {}
    total = 0
    
    # for each row in the file
    for row in csvreader:
        # add to total
        total +=1
        # tally votes for each candidate
        if row[2] in vote_totals:
            vote_totals[row[2]] = vote_totals[row[2]] + 1
        else:
            vote_totals[row[2]] = 1
    
    # print results
    print ("Election Results")
    print ("-------------------------")
    print (f"Total Votes: {total}")
    print ("-------------------------")
    curr_max = 0
    for candidate, votes in vote_totals.items():
        print (f"{candidate}: {round (votes*100/total,4)}% ({votes})")
        # find winner
        if votes > curr_max:
            curr_max = votes
            winner = candidate
    print ("-------------------------")
    print (f"Winner: {winner}")
    print ("-------------------------")