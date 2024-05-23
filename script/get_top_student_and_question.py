import json
import pandas as pd
import regex as re

student_dict = {}

with open("../data/student_statistics.json", "r") as f:
    student_statistics = json.load(f)
    for student in student_statistics:
        student_dict[student] = student_statistics[student]["correct_rate"]
    
student_dict = dict(sorted(student_dict.items(), key=lambda x: x[1], reverse=True))
top_20_student = dict(list(student_dict.items())[:int(len(student_dict) * 0.2)])

# 需要统计top 20%的学生的错误提交题目
question_student_false_dict = {}
question_student_all_dict = {}

question = []
class_id = [i + 1 for i in range(15)]
student_id = []



def init():
    global student_num, question, student_id
    df_title = pd.read_csv('../data/Data_TitleInfo.csv')
    df_student = pd.read_csv('../data/Data_StudentInfo.csv')
    student_num = len(df_student)
    question = df_title['title_ID'].tolist()
    student_id = df_student['student_ID'].tolist()

def is_row_valid(row) -> bool:
        pattern = r'\d+'
        potential = re.findall(pattern, row['class'])
        if len(potential) == 0:
            return False
        cur_class = int(potential[0])
        return cur_class in class_id and row['title_ID'] in question and row['student_ID'] in student_id

def deal():
    global question_student_dict
    for i in range(1, 16):
        df = pd.read_csv(f'../data/Data_SubmitRecord/SubmitRecord-Class{i}.csv')
        # print(f"length of class {i} before clean: {len(df)}")
        df = df[df.apply(is_row_valid, axis=1)]
        for _, row in df.iterrows():
            if row['student_ID'] not in top_20_student:
                continue
            if row['state'] != 'Absolutely_Correct':
                if row['title_ID'] in question_student_false_dict:
                    question_student_false_dict[row['title_ID']] += 1
                else:
                    question_student_false_dict[row['title_ID']] = 1
            
            if row['title_ID'] in question_student_all_dict:
                question_student_all_dict[row['title_ID']] += 1
            else:
                question_student_all_dict[row['title_ID']] = 1


if __name__ == '__main__':
    init()
    deal()
    output = {}
    for q in question_student_false_dict:
        output[q] = question_student_false_dict[q] / question_student_all_dict[q]
    # output = dict(sorted(output.items(), key=lambda x: x[1], reverse=True))
    with open("../data/submit_features.json", "r") as f:
        feature = json.load(f)
        for q in output:
            output[q] = {
                "error": output[q] * 100,
                "difficulty": feature[q]["std"],
                "mul": output[q] * feature[q]["std"] * 100
            }
    output = dict(sorted(output.items(), key=lambda x: x[1]["mul"], reverse=True))
    with open("../data/t4_question_unreason_rate.json", "w") as f:
        json.dump(output, f, indent=4)

    a = []
    b = []
    for q in output:
        a.append([q, output[q]["error"], output[q]["difficulty"]])

    print(a)
