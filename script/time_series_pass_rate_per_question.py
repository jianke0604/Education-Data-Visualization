import pandas as pd
import datetime
import regex as re
from collections import OrderedDict
import json

# ! 注意修改脚本中的文件路径
# ! 当前脚本是在/script文件夹下，并且假设项目根目录下有data文件夹

class_id = [i + 1 for i in range(15)]
title_id = []
title_to_knowledge = {}
student_id = []
dataframe = []  # * [df1, df2, ..., df15] 每个班级的数据
merged_dataframe = None # * 班级合并后的数据
date_dict = {} # * key: date, value: [time section(midnight, day, night), average pass rate, total pass time, total submit times, most popular knowledge type, most popular title]
date_arr = []   # * [year, month, day, time section(midnight, day, night), average pass rate, total pass times, total submit times, most popular knowledge type, most popular title]

date_lb = None
date_ub = None

# ! 前缀和求累计通过

ans = {}    # {student id: {day: pass rate}}
pre_prefix_pass = {}

# * 数据不合法的情况包括 题目ID不存在、班级号不存在、学生ID不存在
def load_id():
    global title_id, student_id, ans, pre_prefix_pass
    df_title = pd.read_csv('../data/Data_TitleInfo.csv')
    df_student = pd.read_csv('../data/Data_StudentInfo.csv')
    title_id = df_title['title_ID'].tolist()
    student_id = df_student['student_ID'].tolist()
    ans = {i: {} for i in student_id}
    pre_prefix_pass = {i: {} for i in student_id}

    for _, row in df_title.iterrows():
        title_to_knowledge[row['title_ID']] = row['knowledge']

# * 检查每一行的数据是否合法
def is_row_valid(row) -> bool:
        pattern = r'\d+'
        potential = re.findall(pattern, row['class'])
        if len(potential) == 0:
            return False
        cur_class = int(potential[0])
        return cur_class in class_id and row['title_ID'] in title_id and row['student_ID'] in student_id

def data_clean():
    for i in range(1, 16):
        df = pd.read_csv(f'../data/Data_SubmitRecord/SubmitRecord-Class{i}.csv')
        # print(f"length of class {i} before clean: {len(df)}")
        df = df[df.apply(is_row_valid, axis=1)]
        dataframe.append(df)
        # ! print out the invalid data
        # for _, row in df.iterrows():
        #     if (not is_row_valid(row)):
        #         print(f"Invalid row: {row}")

        # print(f"length of class {i} after clean: {len(df)}")

# * 为每一行的数据添加日期和分钟列索引
def add_date():
    global merged_dataframe
    merged_dataframe = pd.concat(dataframe, ignore_index=True)
    merged_dataframe['adjusted_time'] = pd.to_datetime(merged_dataframe['time'], unit='s') + pd.Timedelta(hours=8)
    merged_dataframe['date'] = pd.to_datetime(merged_dataframe['adjusted_time'], unit='s').dt.date
    merged_dataframe['minute'] = pd.to_datetime(merged_dataframe['adjusted_time'], unit='s').dt.strftime('%H:%M')
    merged_dataframe = merged_dataframe.drop('adjusted_time', axis=1)
    # print(merged_dataframe)

def deal():
    global pre_prefix_pass
    for _, row in merged_dataframe.iterrows():
        student_id = row['student_ID']
        date = row['date']
        date = date.strftime('%Y-%m-%d')
        # print(f"student_id: {student_id}, date: {date}")
        if row['state'] != 'Absolutely_Correct':
            continue
        if date not in pre_prefix_pass[student_id]:
            pre_prefix_pass[student_id][date] = [row['title_ID']] 
        else:
            print(f"at least 2 elements in pre_prefix_pass[{student_id}][{date}]")
            pre_prefix_pass[student_id][date].append(row['title_ID'])
        print(f"student_id: {student_id}, size: {len(pre_prefix_pass[student_id][date])}")


def get_ans():
    global pre_prefix_pass, ans
    date_range = pd.date_range(start=date_lb, end=date_ub)
    for student_id in pre_prefix_pass:
        total_cnt = len(title_id)
        total_pass = set()
        for date in date_range:
            date_str = date.strftime('%Y-%m-%d')
            # print("date_str: ", date_str)
            if date_str not in pre_prefix_pass[student_id]:
                ans[student_id][date_str] = len(total_pass) / total_cnt
            else:
                total_pass = total_pass.union(set(pre_prefix_pass[student_id][date_str]))
                ans[student_id][date_str] = len(total_pass) / total_cnt


if __name__ == '__main__':
    load_id()
    data_clean()
    add_date()
    date_lb = merged_dataframe['date'].min()
    date_ub = merged_dataframe['date'].max()
    print(f"date lower bound: {date_lb}, date upper bound: {date_ub}")
    deal()
    # print(pre_prefix_submit)
    # print(pre_prefix_pass)
    # for student_id in pre_prefix_submit:
    #     pre_prefix_submit[student_id] = OrderedDict(sorted(pre_prefix_submit[student_id].items(), key=lambda x: x[0]))

    # for student_id in pre_prefix_pass:
    #     pre_prefix_pass[student_id] = OrderedDict(sorted(pre_prefix_pass[student_id].items(), key=lambda x: x[0]))

    # print(pre_prefix_submit)
    # print(pre_prefix_pass)

    get_ans()
    
    # print(pre_prefix_submit)
    with open('./temp.json', 'w') as f:
        json.dump(pre_prefix_pass, f, indent=4)

    with open('../data/time_series_pass_rate_per_question.json', 'w') as f:
        json.dump(ans, f, indent=4)