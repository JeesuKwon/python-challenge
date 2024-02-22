# import os module
import os

# import csv module for reading csv file
import csv

csvpath = os.path.join('Resources','budget_data.csv')

# number output for storing data
totalmonths = 0
totalamount = 0
totalchange = 0
grtinc = 0
grtdec = 0
# list for storing data
list_month = []
list_amount = []
list_change = []
# reading csvfile here in python

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        # count the number of months
        totalmonths = totalmonths + 1
        list_month.append(row[0])

        # total amount for profit
        list_amount.append(row[1])
        totalamount = totalamount + int(row[1])

    # loop for change by each month
    for c in range(1, len(list_amount)):
        list_change.append((int(list_amount[c])-int(list_amount[c-1])))
        totalchange = totalchange + int(list_change[c-1])

    # average of change
        avchange = totalchange / (totalmonths-1)
        avchange2 = round(avchange, 2)

    # greatest increase/decrease
        grtinc = max(list_change)
        grtdec = min(list_change)
    
# print results
    print ("Financial Analysis")
    print ("----------------------------")
    print (f"Total Months : {totalmonths}")
    print (f"Total: ${totalamount}")
    print (f"Average Change: ${avchange2}")
    print (f"Greatest Increase in Profits: {list_month[list_change.index(max(list_change))+1]} (${grtinc}) ")
    print (f"Greatest Decrease in Profits: {list_month[list_change.index(min(list_change))+1]} (${grtdec}) ")

# make it as text file
    file = open("Result.txt","w")

    file.write("Financial Analysis" + "\n")
    file.write("----------------------------" + "\n")   
    file.write(f"Total Months : {totalmonths}" + "\n")
    file.write(f"Total: ${totalamount}" + "\n")  
    file.write(f"Average Change: ${avchange2}" + "\n") 
    file.write(f"Greatest Increase in Profits: {list_month[list_change.index(max(list_change))+1]} (${grtinc})" + "\n")
    file.write(f"Greatest Decrease in Profits: {list_month[list_change.index(min(list_change))+1]} (${grtdec})" + "\n")    
    file.close()