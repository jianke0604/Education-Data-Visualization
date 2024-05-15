import csv
import json
from datetime import datetime
from datetime import timedelta

# 定义输入CSV文件的路径模式和输出JSON文件的路径
input_files = [f'./Data_SubmitRecord/SubmitRecord-Class{i}.csv' for i in range(1, 16)]
output_file = 'dateheatmap.json'

# 创建一个空的列表来存储处理后的数据
data = {}

# 读取每个CSV文件并处理
for input_file in input_files:
    with open(input_file, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # 处理每一行
        for row in reader:
            student_id = row['student_ID']
            
            # 将时间戳转换为人类可读格式
            timestamp = float(row['time'])
            answer_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
            
            # 判断日期是否已经存在
            if answer_time not in data:
                data[answer_time] = 0
            
            else:
                data[answer_time] += 1

# 获取最早和最晚的日期
# 获取最早和最晚的日期
start_date = datetime.strptime(min(data.keys()), '%Y-%m-%d')
end_date = datetime.strptime(max(data.keys()), '%Y-%m-%d')

# 生成完整的日期列表
date_list = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range((end_date - start_date).days + 1)]

# 将缺失的日期添加到数据中
for date in date_list:
    if date not in data:
        data[date] = 0

# 将数据转换为列表
data = [{'date': key, 'value': value} for key, value in data.items()]


# 按日期排序  
data = sorted(data, key=lambda x: x['date'])

# 将数据写入JSON文件
with open(output_file, mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False)

            