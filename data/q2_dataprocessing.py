import csv
import json
from datetime import datetime

# 定义输入CSV文件的路径模式和输出JSON文件的路径
input_files = [f'./Data_SubmitRecord/SubmitRecord-Class{i}.csv' for i in range(1, 16)]
output_file = 'q2_output2.json'

# 创建一个空的列表来存储处理后的数据
data = []

# 读取每个CSV文件并处理
for input_file in input_files:
    with open(input_file, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # 处理每一行
        for row in reader:
            student_id = row['student_ID']
            
            # 将时间戳转换为人类可读格式
            timestamp = float(row['time'])
            answer_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
            
            # 判断答题状态
            state = row['state']
            if state == 'Absolutely_Correct':
                answer_state = 1
            else:
                answer_state = 0
            method = row['method']
            # 将处理后的数据添加到列表中
            data.append({
                'student_id': student_id,
                '答题时间': answer_time,
                '答题状态': answer_state,
                '编程语言': method
            })

# 将数据写入JSON文件
with open(output_file, mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print(f"数据处理完成，结果已保存到 {output_file}")
