import json

# 定义输入JSON文件的路径
input_file = 'student_statistics1.json'

# 读取JSON文件
with open(input_file, mode='r', encoding='utf-8') as jsonfile:
    student_stats = json.load(jsonfile)

# 创建一个列表来存储总答题次数少于10的学生ID
students_with_few_answers = []

# 创建一个集合来存储出现过的编程语言
programming_languages = set()

# 遍历学生统计信息，找出总答题次数少于10的学生，并收集编程语言
for student_id, stats in student_stats.items():
    if stats['total_answers'] < 10:
        students_with_few_answers.append(student_id)
    
    # 收集编程语言
    programming_languages.add(stats['most_common_method'])

# 输出结果
print("总答题次数少于10的学生ID：")
for student_id in students_with_few_answers:
    print(student_id)

# 输出编程语言总数
print(f"一共出现了 {len(programming_languages)} 种编程语言。")
