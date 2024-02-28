import sys
import csv
from datetime import datetime

def is_anniversary(year: int) -> bool:
    if (datetime.now().year - year) % 10 == 0:
        return True
    return False


def count(data: dict, search_month: str) -> list:
    month = data['Birthday'].split('_')[1]
    year = int(data['Birthday'].split('_')[0])
    if month == search_month:
        return [True, data['Department'], is_anniversary(year)]
        
    return [False, None, None]

if __name__ == '__main__':
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    dict_departments = {'Administration' : 0, 'Accounting' : 0, 'HR' : 0, 'Sales' : 0}
    total = 0
    anniversaries = 0
    database_file = sys.argv[1]
    month = sys.argv[2]
    if month not in months:
        print(f'Please give the following format for month {months}')
        sys.exit()
    

    with open(database_file, 'r', newline='') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            is_birthday = count(row, month) 
            
            if is_birthday[0] == True:
                total += 1
                dict_departments[is_birthday[1]] += 1
                if is_birthday[2] == True:
                    anniversaries += 1
            
    print(f"Total No of birthdays in {month} is: {total}")
    print(f"By departments: {dict_departments}")
    print(f"Total No of anniversaries is: {anniversaries}")
        