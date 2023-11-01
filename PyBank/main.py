import csv
import os

budget_data = os.path.join("..","python-challenge","PyBank","Resources","budget_data.csv")

#Initialise variables
total_months = 0
total_amount = 0
changes = []
prev_amount = None

#Initialise variables for greatest increase and decrease in profits/losses
greatest_increase = {"Date": "","Amount":float("-inf")}
greatest_decrease = {"Date": "", "Amount":float("inf")}

#Read the CSV file 
with open (budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    for row in csv_reader:
        date = row[0]
        amount = int(row[1])

        #Count the total number of months in the dataset
        total_months += 1

        #Calculate the net total amount of Profit/Loss 
        total_amount += amount

        #Calculate the changes in "Profit/Losses" over the entire period
        if prev_amount is not None:
            change = amount - prev_amount
            changes.append(change)

            #Check for greatest increase in profits 
            if change > greatest_increase["Amount"]:
                greatest_increase = {"Date": date, "Amount": change}

            #Check for greatest decrease in profits
            elif change < greatest_decrease["Amount"]:
                greatest_decrease = {"Date":date,"Amount": change}

        prev_amount = amount

#Calculate average change in Profit/Loss
average_change = round(sum(changes)/len(changes),2) if changes else 0

# Print and save the analysis
print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Amount']})")

#Save the output file path
output_file = os.path.join("..","PyBank","analysis","Financial Analysis.txt")

with open(output_file, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-" * 30 + "\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Amount']})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Amount']})\n")