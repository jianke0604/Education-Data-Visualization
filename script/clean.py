import pandas as pd
import datetime
import regex as re

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

# * 数据不合法的情况包括 题目ID不存在、班级号不存在、学生ID不存在
def load_id():
    global title_id, student_id
    df_title = pd.read_csv('../data/Data_TitleInfo.csv')
    df_student = pd.read_csv('../data/Data_StudentInfo.csv')
    title_id = df_title['title_ID'].tolist()
    student_id = df_student['student_ID'].tolist()
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

# * 基于is_row_valid函数，清洗数据
def data_clean():
    for i in range(1, 16):
        df = pd.read_csv(f'../data/Data_SubmitRecord/SubmitRecord-Class{i}.csv')
        print(f"length of class {i} before clean: {len(df)}")
        df = df[df.apply(is_row_valid, axis=1)]
        dataframe.append(df)
        # ! print out the invalid data
        # for _, row in df.iterrows():
        #     if (not is_row_valid(row)):
        #         print(f"Invalid row: {row}")

        print(f"length of class {i} after clean: {len(df)}")

        # ! save the cleaned data
        # df.to_csv(f'./data/submit/SubmitRecord-Class{i}.csv', index=False)

def get_min_max_time():
    for i in range(1, 16):
        df = pd.read_csv(f'../data/Data_SubmitRecord/SubmitRecord-Class{i}.csv')
        max_val = df['time'].max()
        min_val = df['time'].min()
        dt_max = datetime.datetime.fromtimestamp(max_val)
        dt_min = datetime.datetime.fromtimestamp(min_val)
        dt_max_fmt = dt_max.strftime('%Y-%m-%d %H:%M:%S')
        dt_min_fmt = dt_min.strftime('%Y-%m-%d %H:%M:%S')
        print(f"max: {max_val}, min: {min_val}, gap: {max_val - min_val}")
        print(f"max: {dt_max_fmt}, min: {dt_min_fmt}")

# * 为每一行的数据添加日期和分钟列索引
def add_date():
    global merged_dataframe
    merged_dataframe = pd.concat(dataframe, ignore_index=True)
    merged_dataframe['adjusted_time'] = pd.to_datetime(merged_dataframe['time'], unit='s') + pd.Timedelta(hours=8)
    merged_dataframe['date'] = pd.to_datetime(merged_dataframe['adjusted_time'], unit='s').dt.date
    merged_dataframe['minute'] = pd.to_datetime(merged_dataframe['adjusted_time'], unit='s').dt.strftime('%H:%M')
    merged_dataframe = merged_dataframe.drop('adjusted_time', axis=1)
    print(merged_dataframe)
    # print(merged_dataframe['ptime'])

# * 需要一个字典，key是日期，value是当天平均通过率、总提交次数(用圆圈的大小反映)、最热门的知识点类型和最热门的题目
# * 同时扁平化成数组，方便js直接使用
def group_by_date():
    global date_dict
    for date, group in merged_dataframe.groupby('date'):
        mapping = {0: 'midnight', 1: 'morning', 2: 'afternoon', 3: "night"}
        correct_cnt = [0 for _ in range(4)]
        try_cnt = [0 for _ in range(4)]
        title_dict = [{} for _ in range(4)]
        for _, row in group.iterrows():
            time = row['minute']
            hour, _ = time.split(':')
            hour = int(hour)
            cur_section = None
            if hour >= 0 and hour < 6:
                cur_section = 0
            elif hour >= 6 and hour < 12:
                cur_section = 1
            elif hour >= 12 and hour < 18:
                cur_section = 2
            else:
                cur_section = 3

            try_cnt[cur_section] += 1
            
            if row['state'] == 'Absolutely_Correct':
                correct_cnt[cur_section] += 1
            if row['title_ID'] in title_dict[cur_section]:
                title_dict[cur_section][row['title_ID']] += 1
            else:
                title_dict[cur_section][row['title_ID']] = 1
        
        max_title = [max(title_dict[i], key=title_dict[i].get) if title_dict[i] else None for i in range(4)]
        knowledge_dict = [{} for _ in range(4)]
        for i in range(4):
            for title in title_dict[i]:
                knowledge = title_to_knowledge[title]
                if knowledge in knowledge_dict[i]:
                    knowledge_dict[i][knowledge] += 1
                else:
                    knowledge_dict[i][knowledge] = 1
        max_knowledge = [max(knowledge_dict[i], key=knowledge_dict[i].get) if knowledge_dict[i] else None for i in range(4)]

        date_dict[date] = [[mapping[i], correct_cnt[i] / try_cnt[i], correct_cnt[i], try_cnt[i], max_knowledge[i], max_title[i]] \
                            if max_title[i] else [mapping[i], 0, 0, 0, None, None] for i in range(4)]
        # date_arr.append([[date.year, date.month, date.day, mapping[i], correct_cnt[i] / try_cnt[i], correct_cnt[i], try_cnt[i], max_knowledge[i], max_title[i]] \
        #                    if max_title[i] else [date.year, date.month, date.day, mapping[i], 0, 0, 0, None, None] for i in range(3)])
        for i in range(4):
            if not max_title[i]:
                date_arr.append([date.year, date.month, date.day, 0, 0, 0, 'None', 'None', mapping[i]])
            else:
                date_arr.append([date.year, date.month, date.day, correct_cnt[i] / try_cnt[i], correct_cnt[i], try_cnt[i], max_knowledge[i], max_title[i], mapping[i]])



if __name__ == '__main__':
    load_id()
    data_clean()
    add_date()
    group_by_date()
    print(date_dict)
    print(date_arr)