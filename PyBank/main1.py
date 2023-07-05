import pandas as pd

# Read the CSV file
data = pd.read_csv('Resources/budget_data.csv')

# Calculate the total number of months
total_months = len(data)

# Calculate the net total amount of "Profit/Losses"
net_total = data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" over the entire period
data['Change'] = data['Profit/Losses'].diff()

# Calculate the average change
average_change = data['Change'].mean()

# Find the greatest increase in profits (date and amount)
greatest_increase = data[data['Change'] == data['Change'].max()]
increase_date = greatest_increase['Date'].values[0]
increase_amount = greatest_increase['Change'].values[0]

# Find the greatest decrease in profits (date and amount)
greatest_decrease = data[data['Change'] == data['Change'].min()]
decrease_date = greatest_decrease['Date'].values[0]
decrease_amount = greatest_decrease['Change'].values[0]

# Print the results
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {increase_date} (${increase_amount})\n"
    f"Greatest Decrease in Profits: {decrease_date} (${decrease_amount})\n"
)

# Print the results
print(output)

# Export the results to a text file
with open("financial_analysis.txt", "w") as txtfile:
    txtfile.write(output)

print("Results exported to 'financial_analysis.txt' file.")