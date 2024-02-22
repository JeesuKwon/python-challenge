# Import modules that are needed
import os
import csv

# Path for CSV file
election_csv = os.path.join('Resources', 'election_data.csv')

# number output for storing data
totalvote = 0
percentvalue = 0
# list for storing data
candidatelist = []
unique_list = []
valuelist = []
percentlist = []
# dic for storing data
conter_dict={}
# Read csv data and header
with open(election_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        # count the number of total votes
        totalvote = totalvote + 1
        
        # count votes by candidates
        candidate=row[2]
        candidatelist.append(row[2])
        if candidate in conter_dict:
            conter_dict[candidate]=conter_dict[candidate]+1
        else:
            conter_dict[candidate]=1

    # list up unique index of candidates and value of vote    
    for x in set(candidatelist):
        unique_list.append(x)
        y = candidatelist.count(x)
        valuelist.append(y)
    # count for % of vote each candidates won
    for p in valuelist:
        percentvalue = round((p / totalvote)*100, 3)
        percentlist.append(percentvalue)

    # select the winner
    max_value = max(valuelist)
    winner = unique_list[valuelist.index(max_value)]
    

# print results
print("Election Result")
print("-------------------------")
print(f"Total Votes: {totalvote}")
print("-------------------------")
for i in range(len(unique_list)):
    print(f"{unique_list[i]}: {percentlist[i]}% ({valuelist[i]})")
print("-------------------------")
print(f"Winner: {winner}")    
print("-------------------------")

# make it as text file
file = open("Result.txt","w")

file.write("Election Result"+ "\n")
file.write("-------------------------"+ "\n")
file.write(f"Total Votes: {totalvote}"+ "\n")
file.write("-------------------------"+ "\n")
for i in range(len(unique_list)):
    file.write(f"{unique_list[i]}: {percentlist[i]}% ({valuelist[i]})"+ "\n")
file.write("-------------------------"+ "\n")
file.write(f"Winner: {winner}"+ "\n")
file.write("-------------------------"+ "\n")
file.close()

