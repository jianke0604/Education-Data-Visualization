import json
from datetime import datetime, timedelta
from collections import Counter

# 定义输入和输出JSON文件的路径
input_file = 'q2_output2.json'
output_file = 'student_statistics1.json'

# 读取JSON文件
with open(input_file, mode='r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

# 创建一个字典来存储每个学生的统计信息
student_stats = {}

# 处理每一条记录
for entry in data:
    student_id = entry['student_id']
    answer_time = entry['答题时间']
    answer_state = entry['答题状态']
    method = entry['编程语言']

    # 如果该学生ID还未在字典中，初始化一个条目
    if student_id not in student_stats:
        student_stats[student_id] = {
            'total_answers': 0,
            'total_correct': 0,
            'answer_times': [],
            'methods': []
        }

    # 更新统计信息
    student_stats[student_id]['total_answers'] += 1
    student_stats[student_id]['total_correct'] += answer_state
    student_stats[student_id]['methods'].append(method)

    # 提取时间部分并转换为秒数表示
    time_only = datetime.strptime(answer_time, '%Y-%m-%d %H:%M:%S').time()
    total_seconds = time_only.hour * 3600 + time_only.minute * 60 + time_only.second
    student_stats[student_id]['answer_times'].append(total_seconds)

# 计算每个学生的统计结果
for student_id, stats in student_stats.items():
    # 计算答题正确率
    total_answers = stats['total_answers']
    total_correct = stats['total_correct']
    correct_rate = total_correct / total_answers

    # 计算答题时间的平均值
    avg_seconds = sum(stats['answer_times']) / total_answers
    avg_time = (datetime.min + timedelta(seconds=avg_seconds)).time().strftime('%H:%M:%S')

    # 统计每个学生使用最多的编程语言
    most_common_method = Counter(stats['methods']).most_common(1)[0][0]

    # 更新统计信息
    stats['correct_rate'] = correct_rate
    stats['average_time'] = avg_time
    stats['most_common_method'] = most_common_method

    # 移除不再需要的原始答题时间和方法
    del stats['answer_times']
    del stats['total_correct']
    del stats['methods']

# 将统计结果写入新的JSON文件
with open(output_file, mode='w', encoding='utf-8') as jsonfile:
    json.dump(student_stats, jsonfile, ensure_ascii=False, indent=4)

print(f"数据处理完成，结果已保存到 {output_file}")
