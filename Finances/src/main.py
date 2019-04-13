import os
import csv

# this module reads in csv file; get count of months included in analysis; get total loss/profit over these months; get average, lowest and highest change from month to month; prints the financial analysis to both the terminal and a text file

# get the csv file and create output file
this_folder = os.path.dirname(__file__)
import_path = os.path.join(this_folder, "Resources", "budget_data.csv")
output_path = os.path.join(this_folder, "Output", "financial_analysis.txt")

# create lists that hold the data obtained from the csv
months = []
amounts = []

def printToTerminalFinancialAnalysis(amounts = [], months = []):
    
    # variable declarations and initializations
    total = 0.0
    max_index = 0
    min_index = 0
    max = 0.0
    min = 0.0
    
    # gets the total
    for amount in amounts:
        total = total + amount
        
    # get the average change - here we subtract the last month from the first month and divide by number of months - 1 (we know this as changes = length - 1
    average_change = (amounts[len(amounts) - 1] - amounts[0]) / (len(amounts) - 1)
    
    # get max value and the index in which the value is so we can retrieve the index in the months list to retrieve the respectful month
    for index, amount in enumerate(amounts):
        if index > 0:
            first = amounts[index - 1]
            second = amounts[index]
            if max < (second - first):
                max = second - first
                max_index = index
                
    # get max value and the index in which the value is so we can retrieve the index in the months list to retrieve the respectful month
    for index, amount in enumerate(amounts):
        if index > 0:
            first = amounts[index - 1]
            second = amounts[index]
            if min > (second - first):
                min = second - first
                min_index = index
    
    print("Financial Analysis")
    print("----------------------------------------------------------------")
    print("Total Months: " + str(len(months)))
    print("Total: " + str('${:,.2f}'.format(total)))
    print("Average Change: " + str('${:,.2f}'.format(average_change)))
    print("Greatest Increase in Profits: (" + months[max_index] + ") " + str('${:,.2f}'.format(max)))
    print("Greatest Decrease in Profits: (" + months[min_index] + ") " + str('${:,.2f}'.format(min)))
    
def printToTextFileFinancialAnalysis(amounts = [], months = [], output_path = ""):
    
    # create output file to write
    output_file = open(output_path, "w")
   
    # variable declarations and initializations
    total = 0.0
    max_index = 0
    min_index = 0
    max = 0.0
    min = 0.0
    
    # gets the total
    for amount in amounts:
        total = total + amount
        
    # gets the average change - here we subtract the last month from the first month and divide by number of months - 1 (we know this as changes = length - 1
    average_change = (amounts[len(amounts) - 1] - amounts[0]) / (len(amounts) - 1)
    
    # get max value and the index in which the value is so we can retrieve the index in the months list to retrieve the respectful month
    for index, amount in enumerate(amounts):
        if index > 0:
            first = amounts[index - 1]
            second = amounts[index]
            if max < (second - first):
                max = second - first
                max_index = index
                
    # get min value and the index in which the value is so we can retrieve the index in the months list to retrieve the respectful month
    for index, amount in enumerate(amounts):
        if index > 0:
            first = amounts[index - 1]
            second = amounts[index]
            if min > (second - first):
                min = second - first
                min_index = index
       
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------------------------------------------\n")
    output_file.write("Total Months: " + str(len(months)) + "\n")
    output_file.write("Total: " + str('${:,.2f}'.format(total)) + "\n")
    output_file.write("Average Change: " + str('${:,.2f}'.format(average_change)) + "\n")
    output_file.write("Greatest Increase in Profits: (" + months[max_index] + ") " + str('${:,.2f}'.format(max)) + "\n")
    output_file.write("Greatest Decrease in Profits: (" + months[min_index] + ") " + str('${:,.2f}'.format(min)))

# reads in csv from resources folder
with open(import_path, newline = "") as csvfile:

    # csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        months.append(row[0])
        amounts.append(float(row[1]))

# print results to terminal
printToTerminalFinancialAnalysis(amounts, months)

# prints results to text file
printToTextFileFinancialAnalysis(amounts, months, output_path)