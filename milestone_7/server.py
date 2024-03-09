from flask import Flask, request
import csv
from datetime import datetime

def is_anniversary(data: dict) -> bool:
    year = int(data['Birthday'].split('_')[0])
    if (datetime.now().year - year) % 10 == 0:
        return True
    return False

def is_birthday_month(data: dict, search_month: str) -> list:
    month = data['Birthday'].split('_')[1]
    if month == search_month:
        return True
        
    return False

def read_data(filename, month, department, serach_anniversary):
  
  data = []
  with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if is_birthday_month(row, month) == True and row['Department'] == department:
        if serach_anniversary ==False:
            data.append(row)
        elif is_anniversary(row):
           data.append(row)


  return data



app = Flask(__name__)

@app.route('/birthdays', methods=['GET'])
def get_birthdays():
  month = request.args.get('month')
  department = request.args.get('department')
  response = read_data('company_database.csv', month, department, False)
  return response

@app.route('/anniversaries', methods=['GET'])
def get_anniversary():
  month = request.args.get('month')
  department = request.args.get('department')
  response = read_data('company_database.csv', month, department, True)
  return response





if __name__ == '__main__':
 
  app.run(debug=True)