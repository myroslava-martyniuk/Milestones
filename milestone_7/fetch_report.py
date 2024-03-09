import sys
import requests
from datetime import datetime
import csv



server = "http://127.0.0.1:5000"

def fetch_report(month, department, url):
    
    try:
        response = requests.get(server+url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching report: {e}")
        return None
    
def display_report_birthdays(month, department):
    url = f"/birthdays?month={month}&department={department}"
    report_data = fetch_report(month, department, url)
    if report_data:
        print(f"Report for {department} department for {month} fetched.")
        print(f"Total: {len(report_data)}")
        print("Employees:")
        for entry in report_data:
            print('- ' + entry['Birthday'], entry['Name'])

    else:
        print("No birthdays")

def display_report_anniversaries(month, department):
    url = f"/anniversaries?month={month}&department={department}"
    report_data = fetch_report(month, department, url)
    if report_data:
        print(f"Anniversaries report for {department} department for {month} fetched.")
        print(f"Total: {len(report_data)}")
        print("Employees:")
        for entry in report_data:
            print('- ' + entry['Birthday'], entry['Name'])

    else:
        print("No anniversaries")

if __name__ == '__main__':
    month = sys.argv[1]
    department = sys.argv[2]    
    display_report_birthdays(month, department)
    display_report_anniversaries(month, department)
    

  