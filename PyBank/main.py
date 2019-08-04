import csv
import os


budget_load = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("budget_analysis.txt")


month_total = 0
month_of_change = []
change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
net_total = 0


with open(budget_load) as financial_data:
    reader = csv.reader(financial_data)

   
    header = next(reader)

    
    first_row = next(reader)
    month_total = month_total + 1
    net_total = net_total + int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

       
        month_total = month_total + 1
        net_total = net_total + int(row[1])

        
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        change_list = change_list + [net_change]
        month_of_change = month_of_change + [row[0]]

        
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

net_monthly_avg = float(sum(change_list) / len(change_list))


output = (
    f"\nFinancial Analysis\n"
    f"-----------------------\n"
    f"Total Months: {month_total}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${net_monthly_avg}\n"
    f"Greatest Increase in Profits: {greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease}\n")

print(output)

with open(output_file, "w") as txt_file:
    txt_file.write(output)