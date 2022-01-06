# Data we need:
# 1. Total num of votes cast
# 2. Complete list of candidate who got votes
# 3. % of votes each candidate won
# 4. Total num of votes each candidate won
# 5. Winner of election based on popular vote

import os
import csv
import datetime\

total_votes = 0
candidate_options = []

read = os.path.join("Resources","election_results.csv")
write = os.path.join("Analysis","election_analysis.txt")
with open(read, 'r') as data:
    reader = csv.reader(data)
    headers = next(reader)
    for row in reader:
        candidate_name = row[2]
        candidate_options.append(candidate_name) if candidate_name not in candidate_options else None
        total_votes += 1
print(candidate_options)

# See if I can find a way to automatically create the directory and file if it does not exist.
with open(write, 'w') as output:
    output.write("Arapahoe\nDenver\nJefferson")
