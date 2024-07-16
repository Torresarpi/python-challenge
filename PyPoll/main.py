import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
election_csv = os.path.join(script_dir, 'resources', 'election_data.csv')
output_txt = os.path.join(script_dir, 'analysis', 'output.txt')

with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    votes_count = 0
    candidates_list = []
    
    for row in csvreader:
        votes_count += 1
        candidates_list.append(str(row[2]))
candidates =  list(dict.fromkeys(candidates_list))
output_list = []
for candidate in candidates:
    votes = candidates_list.count(candidate)
    percent = votes/votes_count*100
    output_list.append((candidate, percent, votes))
winner = ""
if output_list[0][2] > output_list[1][2]:
    winner = output_list[0][0]
    if winner < output_list[2][2]:
        winner =  output_list[2][0]
elif output_list[1][2] > output_list[2][2]:
    winner = output_list[1][0]
else: winner = output_list[2][0]
out = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {votes_count}\n"
    f"----------------------------\n"
    f"{output_list[0][0]}: {output_list[0][1]:.2f}% ({(output_list[0][2])}) \n"
    f"{output_list[1][0]}: {output_list[1][1]:.2f}% ({(output_list[1][2])}) \n"
    f"{output_list[2][0]}: {output_list[2][1]:.2f}% ({(output_list[2][2])}) \n"
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------"
)

with open(output_txt, 'w') as file:
    file.write(out)
