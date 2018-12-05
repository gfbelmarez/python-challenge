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
            report = ""
csvfile.close()

# print results
report += "\nElection Results"
report += "\n-------------------------"
report += f"\nTotal Votes: {total}"
report += "\n-------------------------"
curr_max = 0
for candidate, votes in vote_totals.items():
    report += (f"\n{candidate}: {round (votes*100/total,4)}% ({votes})")
    # find winner
    if votes > curr_max:
        curr_max = votes
        winner = candidate
report += "\n-------------------------"
report += f"\nWinner: {winner}"
report += "\n-------------------------"

# save results as text file
text_file = open("report.txt", "w")
text_file.write(report)
text_file.close()
print (report)
print ("\nReport also exported to report.txt")
