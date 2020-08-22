#Import the os module
import os

#Import the module for reading csv file
import csv

#Csv file path
budget_data = os.path.join('Resources', 'budget_data.csv')

#Set variables and initial values
months = 0
profitloss_total = 0
value = 0
change = 0

#Create date and profit lists
dates = []
profits = []

#Opening and reading the CSV file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading the header row
    csv_header = next(csvreader)

    #Reading the first row and track changes and count month
    first_row = next(csvreader)
    months = months + 1
    profitloss_total = profitloss_total + int(first_row[1])
    value = int(first_row[1])
    
    #Read each row of data after the header & first row 
    for row in csvreader:
        #Keeping track of the dates by adding to list
        dates.append(row[0])
        
        #Calculate the change and add it to profits list and set new value.
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Count months
        months = months + 1

        #Calculate the total amount of profit and losses
        profitloss_total = profitloss_total + int(row[1])

    #Find the greatest increase in profits list and the coresponding date from the dates list
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Find the greatest decrease in profits list and the coresponding date from the dates list
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#Display the profit and loss data
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(months)}")
print(f"Total: ${str(profitloss_total)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Output analysis to .txt file and put in analysis folder
output_path = os.path.join("Analysis", "Financial Analysis.txt")
with open(output_path, 'w') as txtfile:

    txtfile.write("Financial Analysis")
    txtfile.write("---------------------")
    txtfile.write(str(f"Total Months: {str(months)}"))
    txtfile.write(str(f"Total: ${str(profitloss_total)}"))
    txtfile.write(str(f"Average Change: ${str(round(avg_change,2))}"))
    txtfile.write(str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})"))
    txtfile.write(str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})"))


