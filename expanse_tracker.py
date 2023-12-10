from expense import Expense
import calendar
import datetime


def main():
    print("Running expanse Tracker!!!\n")
    expense_file_path ="expanse.csv"
    budget = 2000

    #get user input for expense.
    expense = get_user_expense()



    # Write their expense to a file.
    save_expense_to_file(expense,  expense_file_path)


    # Read file and summarize expenses.
    summarize_expense(expense_file_path,budget)
    

def get_user_expense():
    print("Getting User expanse!!!")
    expense_name = input("Enter expense name:")
    expense_amount = float(input("Enter expense amount:"))

    expense_category = ["food", "home", "work", "fun", "miscellaneous"]
    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_category):
            print(f" {i + 1}, {category_name}")
        
        selected_index = int(input("Enter Your category number:")) - 1
        print("Your input is")

        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense

        else:
            print("invalid category pls try again")


        break

 

def save_expense_to_file(expense: Expense, expense_file_path): #that was a type hint the ":  Expense" it helps knows the class in the other file 
    print(f"{expense} to {expense_file_path}")
    print("Saving User Expanse")
    with open(expense_file_path, "a") as f: #a is if the file exists it appends to it if not it'll create a new one and open simply opens the file
        f.write(f"{expense.name},  {expense.amount}, {expense.category}\n") #The write() method is used to write data into the file

    

def summarize_expense(expense_file_path, budget):
    print("Summarizing User expanse!!!\n")
    expenses = []
    with open(expense_file_path, "r") as f: #r stands for read only
        lines = f.readlines()#readlines gives you a list you can enumerate
        for line in lines:
            expense_name, expense_amount, expense_category = line.strip().split(',')#split seperates it from the comma
            line_expense = Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category
            )
            expenses.append(line_expense)
   

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    print("Expenses By Category\n")
    for key, amount in amount_by_category.items():#makes it arrange downward looping through both key and values
        print(f"{key}: ${amount}")

    total_spent = sum([ex.amount for ex in expenses])
    print(f"You've spent ${total_spent} this month.")

    remaining_budget = budget - total_spent
    if remaining_budget < 0:
        print(red("Budget exceeded! You've reached a negative remaining budget {remaining_budget:.2f}"))
    else:
        print(green(f"Your Remaining Budget for this month is: ${remaining_budget:.2f}"))

    #get the current date
    current_date_time = datetime.datetime.now()

    # Get the number of days in the current month
    total_days_in_month = calendar.monthrange(current_date_time.year, current_date_time.month)[1]

    # Calculate the remaining days in the current month
    remaining_days = total_days_in_month - current_date_time.day



    daily_budget = remaining_budget / remaining_days
    if daily_budget < 0:
        print(red(f"Budget per Day has been exceeded: ${daily_budget:.2f}"))
    else:
        print(f"Estimated Budget per Day: ${daily_budget:.2f}")

print("You can Edit this on your CSV file to your liking")

def green(text):
    return f"\033[92m{text}\033[0m"

def red(text):
    return f"\033[91m{text}\033[0m"



if __name__ == "__main__":
    main()