from faker import Faker
from datetime import datetime
import random


fake = Faker()

departments = ['Administration', 'Accounting', 'HR', 'Sales']
company_data = []

for _ in range(100):
    row = dict()
    row["Name"] = fake.name()
    row["Birthday"] = fake.date_between_dates(date_start='-60y', date_end='-30y').strftime("%Y_%B_%d")
    row["Start_day"] = fake.date_between_dates(date_start='-6y', date_end='now').strftime("%Y_%B_%d")
    row["Department"] = departments[random.randint(0,3)]
    company_data.append(row)

with open('company_database.csv', 'w') as file:
    file.write(','.join(company_data[0].keys()))
    file.write('\n')
    for row in range (len(company_data)):
        file.write(','.join(company_data[row].values()))
        file.write('\n')



