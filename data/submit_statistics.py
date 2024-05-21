import csv
import json
from datetime import datetime
from datetime import timedelta

Question_list = {}

start_date = datetime.strptime('2023-08-31', '%Y-%m-%d')
end_date = datetime.strptime('2024-01-25', '%Y-%m-%d')

with open('Data_TitleInfo.csv', mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Question_list[row['title_ID']] = {}
        for i in range((end_date - start_date).days + 1):
            Question_list[row['title_ID']][datetime.strftime(start_date + timedelta(days=i), '%Y-%m-%d')] = 0
            
input_files = [f'./Data_SubmitRecord/SubmitRecord-Class{i}.csv' for i in range(1, 16)]
output_file = 'submit_statistics.json'

for input_file in input_files:
    with open(input_file, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            Question_list[row['title_ID']][datetime.fromtimestamp(float(row['time'])).strftime('%Y-%m-%d')] += 1

with open(output_file, mode='w', encoding='utf-8') as jsonfile:
    json.dump(Question_list, jsonfile, ensure_ascii=False, indent=4)
    