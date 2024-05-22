import json
from datetime import datetime
from datetime import timedelta
import csv
Question_list = {}

start_date = datetime.strptime('2023-08-31', '%Y-%m-%d')
end_date = datetime.strptime('2024-01-25', '%Y-%m-%d')

Question_features = {}

def cal_total(Question_list, start_date, end_date):
    Question_total = {}
    for key in Question_list.keys():
        Question_total[key] = 0
        for i in range((end_date - start_date).days + 1):
            Question_total[key] += Question_list[key][datetime.strftime(start_date + timedelta(days=i), '%Y-%m-%d')]
    return Question_total

def cal_std(Question_list, start_date, end_date, Question_total):
    # 平均提交时间
    Question_avg_time = {}
    Question_std = {}
    for key in Question_list.keys():
        Question_avg_time[key] = 0
        for i in range((end_date - start_date).days + 1):
            Question_avg_time[key] += (Question_list[key][datetime.strftime(start_date + timedelta(days=i), '%Y-%m-%d')] * i)
        Question_avg_time[key] /= Question_total[key]
    for key in Question_list.keys():
        Question_std[key] = 0
        for i in range((end_date - start_date).days + 1):
            Question_std[key] += (Question_list[key][datetime.strftime(start_date + timedelta(days=i), '%Y-%m-%d')] * (i - Question_avg_time[key]) ** 2)
        Question_std[key] = (Question_std[key] / Question_total[key]) ** 0.5
    return Question_std

with open('submit_statistics.json', mode='r', encoding='utf-8') as file:
  Question_list = json.load(file)
  
Question_total = cal_total(Question_list, start_date, end_date)
Question_std = cal_std(Question_list, start_date, end_date, Question_total)

for key in Question_list.keys():
    Question_features[key] = {}
    Question_features[key]['total'] = Question_total[key]
    Question_features[key]['std'] = Question_std[key]

with open('submit_features.json', mode='w', encoding='utf-8') as file:
    json.dump(Question_features, file, ensure_ascii=False, indent=4)