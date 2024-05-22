# import csv
# import json
# from collections import defaultdict
# from datetime import datetime
# import os

# # 初始化一个字典来存储学生数据
# students_data = defaultdict(lambda: defaultdict(lambda: {"first_time": None, "last_time": None}))

# # 读取多个CSV文件
# for class_num in range(1, 16):
#     file_path = f'./Data_SubmitRecord/SubmitRecord-Class{class_num}.csv'
    
#     if os.path.exists(file_path):
#         with open(file_path, mode='r', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 student_id = row['student_ID']
#                 title_id = row['title_ID']
#                 result = row['state']
#                 timestamp = float(row['time'])

#                 if result == 'Absolutely_Correct':
#                     # 转换时间戳为datetime对象
#                     time_obj = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

#                     if students_data[student_id][title_id]['first_time'] is None:
#                         # 记录第一次正确回答的时间戳
#                         students_data[student_id][title_id]['first_time'] = time_obj
#                     # 更新最后一次正确回答的时间戳
#                     students_data[student_id][title_id]['last_time'] = time_obj
#     else:
#         print(f"File {file_path} does not exist")

# # 写入JSON文件
# output_path = './students_data.json'
# with open(output_path, mode='w', encoding='utf-8') as json_file:
#     json.dump(students_data, json_file, ensure_ascii=False, indent=4)

# print(f"Data has been written to {output_path}")

import json

# 读取之前生成的JSON文件
with open('students_data.json', mode='r', encoding='utf-8') as json_file:
    students_data = json.load(json_file)

# 初始化一个字典来存储每个学生的不一致题目统计
inconsistent_questions = {}

# 遍历所有学生的数据
for student_id, titles in students_data.items():
    inconsistent_titles = []
    for title_id, times in titles.items():
        if times['first_time'] != times['last_time']:
            inconsistent_titles.append(title_id)
    
    # 记录每个学生不一致的题目数和题目id
    inconsistent_questions[student_id] = {
        'count': len(inconsistent_titles),
        'titles': inconsistent_titles
    }

# 将结果写入新的JSON文件
with open('students_inconsistent_questions.json', mode='w', encoding='utf-8') as json_file:
    json.dump(inconsistent_questions, json_file, ensure_ascii=False, indent=4)

