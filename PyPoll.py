# Data we need:
# 1. Total num of votes cast
# 2. Complete list of candidate who got votes
# 3. % of votes each candidate won
# 4. Total num of votes each candidate won
# 5. Winner of election based on popular vote

import os
import csv
import datetime

read = os.path.join("Resources","election_results.csv")
write = os.path.join("Analysis","election_analysis.txt")
with open(read, 'r') as data:
    reader = csv.reader(data)
    headers = next(reader)
    print(headers)

# See if I can find a way to automatically create the directory and file if it does not exist.
with open(write, 'w') as output:
    output.write("Arapahoe\nDenver\nJefferson")
#comment
