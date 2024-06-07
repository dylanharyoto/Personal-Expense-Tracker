# Database 
accounts = {}
passcodes = {}
goal_name = {"i": "income", "e": "expense", "s": "saving", "c": "charity"}
status_name = {"s": "store", "u": "update", "r": "retrieve", "d": "delete"}

# Input Validation
"""
The validate_username() function is responsible to verify the username in the form of phone number (8 digits) with the input validation.
It has 1 parameter:
- username (str): create or login
It will return:
- username (str)
"""
def validate_username(username):
    # While format is incorrect
    while True:
        # Case 1: If username consists of characters.
        if not username.isdigit():
            username = input("\nThe input '{0}' cannot be characters. Please re-input your phone number (e.g. 12345678).\n>> ".format(username))
        # Case 2: If username's length is not equal to 8.
        elif len(username) != 8:
            username = input("\nThe input '{0}' has invalid length. Please re-input your phone number (e.g. 12345678).\n>> ".format(username))
        # Case 3: If pass case 1 and 2.
        else:
            break
    # Case 1: If username is not registered.
    if username not in accounts:
        status = input("\nThe phone number '{0}' is not registered. Do you want to create an account?\nType 'y' for YES.\nType 'n' for NO.\n>> ".format(username))
        # While answer is incorrect.
        while status not in ["y", "n"]:
            status = input("\nInvalid answer! The phone number '{0}' is not registered. Do you want to create an account?\nType 'y' for YES.\nType 'n' for NO.\n>> ".format(username))
        # If user decide not to create an account.
        if status == "n":
            lock_screen()
    return username
"""
The validate_passcode() function is responsible to verify the passcode (4 digits) with the input validation.
It has 2 parameters:
- username (str): user's database
- passcode (str): make new or verification
It will return:
- passcode (str)
"""
def validate_passcode(username, passcode):
    # While format is incorrect
    while True:
        # Case 1: If passcode consists of characters.
        if not passcode.isdigit():
            passcode = input("\nThe input cannot be characters. Please re-input your passcode with length of 4 (e.g. 1234).\n>> ")
        # Case 2: If passcode's length is not equal to 8.        
        elif len(passcode) != 4:
            passcode = input("\nThe input '{0}' has invalid length. Please re-input your passcode with length of 4 (e.g. 1234).\n>> ".format(passcode))
        # Case 3: If username does not exist (new account).
        elif username not in accounts:
            # Assign the new allocations to accounts and new passcode to passcodes with the new username.
            passcodes[username] = passcode
            accounts[username] = {"income": {}, "expense": {}, "saving": {}, "charity": {}}
            break
        # Case 4: If username exists but wrong password (exixsting account).
        elif passcodes[username] != passcode:
            passcode = input("\nWrong passcode! Please re-input your passcode with length of 4 (e.g. 1234).\n>> ")
        # Case 5: If pass case 1, 2, 3, and 4.
        else:
            break
    return passcode
"""
The validate_date() function is responsible to prompt user and verify the date with the input validation.
It has 3 parameters:
- username (str): user's database
- goal (str): associated with username
- stop (int): when to stop prompting the user (0 - nonstop, 1 - year, 2 - year, month, 3 - year, month, date)
It will return:
- final_date (str)
"""
def validate_date(username, goal, stop):
    """
    The validate_date_details() function is responsible to prompt user and verify the date in the YYYY-MM-DD format with the input validation.
    It has 3 parameters
    - text (str): what to input (year, month, or date)
    - start (int): the starting range of the input
    - stop (int): the ending range of the input
    It will return:
    - date_entity (str)
    """
    def validate_date_details(text, start, end):
        date_entity = input("Please input the current {0}.\n>> ".format(text))
        # While format is incorrect
        while True:
            # Case 1: If result consists of characters.
            if not date_entity.isdigit():
                date_entity = input("The input '{0}' cannot be characters. Please re-input the {1} according to the YYYY-MM-DD format.\n>> ".format(date_entity, text))
            # Case 2: If result is out of range.
            elif int(date_entity) not in range(start, end):
                date_entity = input("The input '{0}' is out of range. Please re-input the {1} according to the YYYY-MM-DD format.\n>> ".format(date_entity, text))
            # Case 5: If pass case 1 and 2.
            else:
                break
        return date_entity
    final_date = 0
    print("\nWhen is it happening? Please input the date according to the YYYY-MM-DD format.")
    # While final_date does not exist.
    while True:
        year = validate_date_details("year in YYYY", 1000, 10000)
        # Case 1: If new function.
        if stop == 1:
            final_date = year
            break
        # Else, continue.
        month = validate_date_details("month in MM", 1, 13)
        if stop == 2:
            final_date = year + "-" + month
            break
        # Case 1: If month is February.
        if int(month) == 2:
            date = validate_date_details("date in DD", 1, 29)
        # Case 2: If month is April, June, Septembet, November.
        elif int(month) in [4, 6, 9, 11]:
            date = validate_date_details("date in DD", 1, 31)
        # Case 3: If month is January, March, May, July, August, October, December.
        else:
            date = validate_date_details("date in DD", 1, 32)
        # Ensure month and date have the same length.
        if len(month) == 1:
            month = "0" + month
        if len(date) == 1:
            date = "0" + date
        # Concatenate year, month, and date into the YYYY-MM-DD format.
        final_date = year + "-" + month + "-" + date
        # Case 1: If function is ('store' or 'newfunction2') or final_date exists.
        if stop == 3 or final_date in username[goal]:
            break
        # Else, continue
        print("\nThe date '{0}' is not found in '{1}'. Please input another date according to the YYYY-MM-DD format.".format(final_date, goal))
    return final_date
"""
The validate_category() function is responsible to prompt user to input the category (5-10 characters) with the input validation.
It has 4 parameters:
- username (str): user's database
- goal (str): associated with username
- date (str): associated with goal
- function (str): whether to store ("s"), update ("u"), retrieve ("r"), or delete ("d")
It will return:
- category (str)
"""
def validate_category(username, goal, date, function):
    condition = False
    text = "does not exist"
    # Case 1: If function is to store.
    if function == "s":
        condition = True
        text = "existed"
    category = input("\nWhere is the source of the {0} that you wish to {1} from? Please input the category (e.g. salary).\n>> ".format(goal, status_name[function]))
    # While format is incorrect.
    while True:
        # Case 1: If category consists of digits.
        if category.isdigit():
            category = input("The input '{0}' cannot be integers. Please re-input the category.\n>> ".format(category))
        # Case 2: If category is out of range.
        elif len(category) not in range(5, 11):
            category = input("The input '{0}' is out of range (5-10 characters). Please re-input the category.\n>> ".format(category))
        # Case 3: If category does not exist.
        elif (category in username[goal][date]) == condition:
                category = input("The input '{0}' {1}. Please re-input another category.\n>> ".format(category, text))
        # Case 4: If pass case 1, 2, and 3.
        else:
            break
    return category
"""
The validate_amount() function is responsible to prompt user to input the amount with the input validation.
It has 3 parameters:
- category (str): user's database
- goal (str): whether to income, expense, saving, charity
- function (str): whether to store ("s"), update ("u"), retrieve ("r"), or delete ("d")
It will return:
- amount (int)
"""
def validate_amount(category, goal, function):
    amount = input("\nHow much is the '{0}' do you wish to {1} to {2}? Please input the amount in HKD (e.g. 100).\n>> ".format(category, status_name[function], goal))
    # Reference https://stackoverflow.com/questions/16290373/validate-float-data-type-python 
    # While format is incorrect.
    while True:
        try:
            amount = float(amount)
        except ValueError:
            amount = input("The input '{0}' cannot be strings. Please re-input the amount.\n>> ".format(amount))
            continue
        if float(amount) <= 0:
            amount = input("The input '{0}' is lesser than or equal to 0. Please re-input the amount.\n>> ".format(amount))
        # Case 2: If pass case 1.
        else:
            break
    return float(amount)

# Helper Functions
"""
The sort_date() procedure is responsible to sort the dates of every record stored in the database of the chosen allocation.
It has 2 parameters:
- username (str): user's database
- goal (str): whether to income, expense, saving, charity
"""
def sort_date(username, goal):
    dates, result = [], {}
    records = username[goal]
    # Loop for every record and assign it to a list called dates.
    for record in records:
        dates.append(record)
    # Sort the dates in descending order.
    dates.sort(reverse=True)
    # Loop for every date in the dates and records, compare both.
    for date1 in dates:
        for date2 in records:
            # If both date match, assign the date and content to a dictionary.
            if date1 == date2:
                result[date1] = records[date1]
    # Replace the current dictionary with the newly sorted dictionary.
    username[goal] = result
"""
The sort_amount() procedure is responsible to sort the amount of every record stored in the database of the chosen allocation.
It has 2 parameters:
- username (str): user's database
- goal (str): whether to income, expense, saving, charity
"""
def sort_amount(username, goal):
    records = username[goal]
    # Loop for every record.
    for record in records:
        content, result = [], {}
        # Loop for every key (category) and value (amount), assign them to a list called content.
        for category, amount in records[record].items():
            content.append([amount, category])
        # Sort the content in descending order.
        content.sort(reverse=True)
        # Loop for every category and amount, assign them to a dictionary.
        for item in content:
            result[item[1]] = item[0]
        # Replace the current dictionary with the newly sorted dictionary.
        records[record] = result

# Starter
"""
The lock_screen() function is responsible to prompt user to input the username in the form of phone number (8 digits) and the passcode (4 digits) with the input validation.
It will return:
- username (str)
"""
def lock_screen():
    # Prompt username and username validation.
    username = input("\nHello! Welcome to the Budget Tracking App ver.1002!\nPlease input your phone number to login/register (e.g. 12345678).\n>> ")
    username = validate_username(username)
    # Prompt passcode and username passcode. 
    passcode = input("\nPlease input your passcode with length of 4 (e.g. 1234).\n>> ")
    passcode = validate_passcode(username, passcode)
    return username
"""
The opening() function is responsible to prompt user to input the chosen allocation and the purpose of either store, update, retrieve, or delete with the input validation.
It has 1 parameter:
- username (str): user's name
It will return:
- goal (str)
- status (str)
"""
def opening(username):
    print("\nWelcome, {0}! What do you want to track today?".format(username))
    # Prompt goal and goal validation.
    goal = input("Type 'i' for income.\nType 'e' for expense.\nType 's' for saving.\nType 'c' for charity.\n>> ")
    while goal not in ["i", "e", "s", "c"]:
        goal = input("\nInvalid input!\nType 'i' for income.\nType 'e' for expense.\nType 's' for saving.\nType 'c' for charity.\n>> ")
    # Replace goal wth the original name.
    goal = goal_name[goal]
    print("\nThank you for choosing {0}. What do you want to do?".format(goal))
    # Prompt status and status validation.
    status = input("Type 's' to store {0}.\nType 'u' to update {0}.\nType 'r' to retrieve {0}.\nType 'd' to delete {0}.\nNew feature! Type '1' to display the total {0} of the previous year.\nNew feature! Type '2' to display the top 3 {0} of the past 30 days.\n>> ".format(goal))
    while status not in ["s", "u", "r", "d", "1", "2"]:
        status = input("\nInvalid input!\nType 's' to store {0}.\nType 'u' to update {0}.\nType 'r' to retrieve {0}.\nType 'd' to delete {0}.\nNew feature! Type '1' to display the total {0} of the previous year.\nNew feature! Type '2' to display the top 3 {0} of the past 30 days.\n>> ".format(goal))
    return (goal, status)

# Display Functions
"""
The display_total_per_year() procedure is responsible to display the chosen allocation of last year from the ledger according to the year inputted by the user.
It has 3 parameters:
- username (str): user's name
- goal (str): whether to income, expense, saving, charity
- count (int): how many days - in this case, 30
"""
def display_total_per_year(username, goal, count):
    # Case 1: If goal contains something.
    if len(username[goal]) != 0:
        current_year = validate_date(username, goal, 1)
        # Decrement current_year by 1 for last_year
        last_year = str(int(current_year) - count)
        dates = username[goal]
        total = 0
        record = []
        # Loop for every date in the list and records, compare both.
        for date in dates:
            # Case 1: If date's year is equal to last_year.
            if date[:4] == last_year:
                # Loop for every date in the list and records, compare both.
                for category, amount in dates[date].items():
                    record.append([date, category, amount])
                    total += dates[date][category]
        # Sort the record in descending order.
        record.sort(reverse=True)
        print("\nTotal {0} of {1}.".format(goal, last_year))
        print("-" * 40)
        print("| {0:^10} | {1:^10} | {2:^10} |".format("Date", "Category", "Amount"))
        print("-" * 40)
        # Case 1: If there is nothing to display.
        if len(record) == 0:
            print("{0} is still empty.".format(goal))
        # Else, loop for each date, category, amount in record.
        else:
            for item in record:
                print("| {0:^10} | {1:^10} | {2:^10} |".format(item[0], item[1], item[2]))
        print("-" * 40)
        print("Total {0}: {1}".format(goal, total))
    # Case 2: If goal contains nothing.
    else:
        print("\nNothing to display.")
"""
The display_top_three_per_day() procedure is responsible to display the top 3 of the chosen allocation in the past 30 days from the ledger according to the date inputted by the user.
It has 3 parameters:
- username (str): user's name
- goal (str): whether to income, expense, saving, charity
- count (int): how many days - in this case, 30
"""
def display_top_three_per_day(username, goal, count):
    # Case 1: If goal contains something.
    if len(username[goal]) != 0:
        current_date = validate_date(username, goal, 3)
        dates = username[goal]
        total = 0
        record = []
        current_year, current_month, current_date = [int(x) for x in current_date.split("-")]
        new_year, new_month, new_date = current_year, current_month, current_date
        # Loop # of times based on the number in count.
        for i in range(count):
            new_date -= 1
            if new_date < 1:
                new_month -= 1
                # Case 1: If new_month is below January.
                if new_month < 1:
                    new_month = 12
                    new_year -= 1
                # Case 1: If new_month is February.
                if new_month == 2:
                    new_date = 28
                # Case 2: If month is April, June, Septembet, November.
                elif new_month in [4, 6, 9, 11]:
                    new_date = 30
                # Case 3: If month is January, March, May, July, August, October, December.
                else:
                    new_date = 31
            # Loop for every date in dates.
            for date in dates:
                # Case 1: If new_year, new_month, new_date match with the date entities interating.
                if [new_year, new_month, new_date] == [int(entity) for entity in date.split("-")]:
                    # Loop for every category and amount in each date.
                    for category, amount in dates[date].items():
                        record.append([amount, category, date])
                        total += amount
        # Sort the record in descending order.
        record.sort(reverse=True)
        print("\nTop 3 {0} from {1}-{2}-{3} to {4}-{5}-{6}.".format(goal, new_year, new_month, new_date, current_year, current_month, current_date))
        print("-" * 40)
        print("| {0:^10} | {1:^10} | {2:^10} |".format("Date", "Category", "Amount"))
        print("-" * 40)
        # Else, loop for each date, category, amount in top 3 of the record.
        for item in record[:3]:
            print(f"| {item[2]:^10} | {item[1]:^10} | {item[0]:^10} |")
        print("-" * 40)
    # Case 2: If goal contains nothing.
    else:
        print("\nNothing to display.")

# Functions
"""
The store() procedure is responsible to store the chosen allocation to the ledger with the date, category, and amount inputted by the user.
It has 2 parameters:
- username (str): user's name
- goal (str): whether to income, expense, saving, charity
"""
def store(username, goal):
    date = validate_date(username, goal, 3)
    # If date does not exist.
    if date not in username[goal]:
        username[goal][date] = {}
    category = validate_category(username, goal, date, "s")
    amount = validate_amount(category, goal, "s")
    # Append new record to the ledger. 
    username[goal][date][category] = amount
    # Sort by amount, then sort by date.
    sort_amount(username, goal)
    sort_date(username, goal)
    print("\nThe {0} from '{1}' in {2} as much as {3} HKD is successfully stored.".format(goal, category, date, amount))
"""
The update() procedure is responsible to update the chosen allocation in the ledger with the date, category, and amount inputted by the user.
It has 2 parameters:
- username (str): user's name
- goal (str): whether to income, expense, saving, charity
"""
def update(username, goal):
    if len(username[goal]) != 0:
        display_total_per_year(username, goal, 0)
        date = validate_date(username, goal, 0)
        category = validate_category(username, goal, date, "u")
        amount = validate_amount(category, goal, "u")
        print("\nUpdating {0} in {1}...".format(goal, date))
        # Append new amount to the ledger. 
        username[goal][date][category] = amount
        # Sort by amount, then sort by date.
        sort_amount(username, goal)
        print("The {0} from '{1}' in {2} is successfully updated.".format(goal, category, date))
    else:
        print("\n{0} is still empty.".format(goal))
"""
The retrieve() procedure is responsible to retrieve the chosen allocation from the ledger with the category and amount based on the date inputted by the user.
It has 2 parameters:
- username (str): user's name
- goal (str): whether to income, expense, saving, charity
"""
def retrieve(username, goal):
    if len(username[goal]) != 0:
        date = validate_date(username, goal, 0)
        categories = username[goal][date]
        print("\nRetrieving {0}s in {1}...".format(goal, date))
        print("-" * 27)
        print("| {0:^10} | {1:^10} |".format("Category", "Amount"))
        print("-" * 27)
        for category in categories:
            print("| {0:^10} | {1:^10} |".format(category, categories[category]))
        print("-" * 27)
        print("The {0}s in {1} is successfully retrieved.".format(goal, date))
    else:
        print("\n{0} is still empty.".format(goal))
"""
The delete() procedure is responsible to delete the chosen allocation from the ledger according to the date, category, and amount inputted by the user.
It has 2 parameters:
- username (str): user's name
- goal (str): whether to income, expense, saving, charity
"""
def delete(username, goal):
    if len(username[goal]) != 0:
        display_total_per_year(username, goal, 0)
        date = validate_date(username, goal, 0)
        category = validate_category(username, goal, date, "d")
        print("\nDeleting {0}s in {1}...".format(goal, date))
        del username[goal][date][category]
        if len(username[goal][date]) == 0:
            del username[goal][date]
        sort_amount(username, goal)
        sort_date(username, goal)
        print("The {0} from '{1}' in {2} is successfully deleted.".format(goal, category, date))
    else:
        print("\n{0} is still empty.".format(goal))

# Main
def main():
    status = "l"
    while status != "e":
        if status == "l":
            username = lock_screen()
        purpose, status = opening(username)
        current = accounts[username]
        if status == "s":
            store(current, purpose)
        elif status == "u":
            update(current, purpose)     
        elif status == "r":
            retrieve(current, purpose)
        elif status == "d":
            delete(current, purpose)
        elif status == "1":
            display_total_per_year(current, purpose, 1)
        else:
            display_top_three_per_day(current, purpose, 30)
        status = input("\nThank you for tracking. What do you want to next?\nType 'e' to end session (this will lose all your data).\nType 'c' to continue.\nType 'l' to logout.\n>> ")
        while status not in ["e", "c", "l"]:
            status = input("\nInvalid input!\nWhat do you want to next?\nType 'e' to end session (this will lose all your data).\nType 'c' to continue.\nType 'l' to logout.\n>> ")
main()