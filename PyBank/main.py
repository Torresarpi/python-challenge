import os
import csv

script_dir = os.path.dirname(os.path.abspath(__file__))
budget_csv = os.path.join(script_dir, 'resources', 'budget_data.csv')
output_txt = os.path.join(script_dir, 'analysis', 'output.txt')

with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    row1 = next(csvreader)
    
    months_count = 1
    total_profit = int(row1[1])
    previous_profit = int(row1[1])
    sum_change = 0
    greatest_inc = 0
    greatest_dec = 0
    greatest_inc_month = ""
    greatest_dec_month = ""
    
    for row in csvreader:
        months_count += 1
        curr = int(row[1])
        total_profit += curr
        change = curr - previous_profit
        sum_change += change
        
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_month = row[0]
        
        if change < greatest_dec:
            greatest_dec = change
            greatest_dec_month = row[0]
        
        previous_profit = curr

    avg_change = sum_change / (months_count - 1)

out = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months_count}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})\n"
    f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})\n"
)

with open(output_txt, 'w') as file:
    file.write(out)
