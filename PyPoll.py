# Data we need:
# 1. Total num of votes cast
# 2. Complete list of candidate who got votes
# 3. % of votes each candidate won
# 4. Total num of votes each candidate won
# 5. Winner of election based on popular vote

import os
import csv
import datetime

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

read = os.path.join("Resources","election_results.csv")
write = os.path.join("Analysis","election_analysis.txt")
with open(read, 'r') as data:
    reader = csv.reader(data)
    headers = next(reader)
    for row in reader:
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name]+=1
        total_votes += 1

for key, value in candidate_votes.items():
    votes=value
    vote_percentage = value / total_votes * 100
    print(f"{key}: {value / total_votes * 100:.1f}% ({value:,})\n")
    if(votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = key
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

# See if I can find a way to automatically create the directory and file if it does not exist.
with open(write, 'w') as output:
    output.write("Arapahoe\nDenver\nJefferson")
