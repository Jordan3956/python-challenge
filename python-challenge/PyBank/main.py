
import os
import csv

#input_file_path = os.path.join("Resources", "budget_data.csv")
input_file_path = os.path.join("Resources", "budget_data.csv")

with open(input_file_path, newline="", encoding="utf-8") as budget:
    csvreader = csv.reader(budget, delimiter=",")
    header = next(csvreader)

    total_months = []
    total_profit = []
    monthly_profit_change = []

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit) - 1):
        monthly_profit_change.append(total_profit[i + 1] - total_profit[i])

max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

max_increase_month = monthly_profit_change.index(max_increase_value) + 1
max_decrease_month = monthly_profit_change.index(max_decrease_value) + 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${max_increase_value})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${max_decrease_value})")

output_file_path = os.path.join("analysis" "Financial_Analysis_Summary.txt")

with open(output_file_path, "w") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total: ${sum(total_profit)}\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change) / len(monthly_profit_change), 2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${max_increase_value})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${max_decrease_value})\n")
