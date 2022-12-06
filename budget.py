print("Welcome to budget tracker")
budget = input("Please input your budget. ")
if budget.isdigit():
    budget = int(budget)

    if budget <= 0:
        print('Input larger number than 0')
        quit()

shopping_list = []

transaction_times = input("How many transactions have you done today? ")
if transaction_times.isdigit():
    transaction_times = int(transaction_times)

    if transaction_times <= 0:
        print('Input larger number than 0')
        quit()


for idx in range(transaction_times):
    item = input('What items have you bought? ')
    shopping_list.append(item)

print("You have bought",shopping_list)

shopping_list_prices = []

for idx in range(transaction_times):
    prices = int(input('What are the prices of your items? '))
    shopping_list_prices.append(prices)

print("Your purchase(s) amounted to: ", sum(shopping_list_prices))
new_budget = (budget - sum(shopping_list_prices))
print("Your current budget is now", budget - sum(shopping_list_prices))
