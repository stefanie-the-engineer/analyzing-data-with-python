import os
import csv

# get the csv file and create output folder and output file
this_folder = os.path.dirname(__file__)
import_path = os.path.join(this_folder, "Resources", "budget_data.csv")
output_path = os.path.join(this_folder, "Output", "financial_analysis.csv")

#create lists that hold the data obtained from the csv
month_list = []
amount_list = []
change_list = []

# create variable to hold count, average_profit, lowest
total = 0.0
average_change = 0.0
lowest = 0.0
highest = 0.0

# reads in csv from resources folder
with open(import_path, newline='') as csvfile:

    # csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # read each row of data after the header and append months and amounts into lists
    for row in csvreader:
        month_list.append(row[0])
        amount_list.append(float(row[1]))
    
    # gets the total
    for amount in amount_list:
        total = total + amount
    
    # gets the average change
    #index = 0
    #for amount in amount_list:
    #    if index >= 1:
    #        if (amount_list[index - 1] >= 0.0) & (amount_list[index] >= 0.0): # if both are positive
    #            if amount_list[index] > amount_list[index - 1]: 
    #                change_list.append(amount_list[index] - amount[index - 1])
    #                print(index, amount_list[index])
    #            else:
    #                change_list.append(amount_list[index] - amount[index - 1] * -1)
    #        elif (amount_list[index - 1] >= 0.0) & (amount_list[index] < 0.0): # if current index is less than 0.0
    #            change_list.append(amount_list[index] - amount_list[index - 1])
    #        elif (amount_list[index - 1] < 0.0) & (amount_list[index] >= 0.0): # if previous index is less than 0.0
    #            change_list.append(amount_list[index] - amount_list[index - 1]) # working on logic
    #    
    #    index += 1
        
    #for index, first in enumerate(amount_list):
    #    for second in amount_list[index+1:]:
    #        if first >= 0.0 and second >= 0.0:
    #            if second >= first:                             # increase only considering positive amounts 
    #                change_list.append(second - first)
    #            else:                                           # decrease only considering positive amounts
    #               change_list.append(-1.0 * (second - first))      
    #        elif first >= 0.0 and second < 0:                     # decrease going from positive to negative
    #            change_list.append(-1.0 * (first - second))
    #        elif first < 0.0 and second >= 0.0:                   # increase from negative to positive
    #            change_list.append(second - first)
    
    index = 0
    for amount in amount_list:
        if index >= 1:
            if (amount_list[index - 1:] >= 0.0) and (amount_list[index] >= 0.0): # if both are positive
                if amount_list[index] > amount_list[index - 1:]: 
                    change_list.append(amount_list[index] - amount[index - 1:])
                    print(index, amount_list[index])
                else:
                    change_list.append(amount_list[index] - amount[index - 1:] * -1)
            elif (amount_list[index - 1:] >= 0.0) and (amount_list[index] < 0.0): # if current index is less than 0.0
                change_list.append(amount_list[index] - amount_list[index - 1:])
            elif (amount_list[index - 1:] < 0.0) and (amount_list[index] >= 0.0): # if previous index is less than 0.0
                change_list.append(amount_list[index] - amount_list[index - 1:]) # working on logic
        index = index + 1
    
# writes data to new file
with open(output_path, "w"):

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
    

print("Financial Analysis")
print("--------------------------------------------------------")
print("Total Months: " + str(len(month_list)))
print("Total: " + str('${:,.2f}'.format(total)))
print("Average Change: " + str(sum/len(change_list)))
print("Greatest Increase in Profits: ") 
print("Greatest Decrease in Profits: ") 
