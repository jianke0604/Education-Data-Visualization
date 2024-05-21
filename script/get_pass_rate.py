import json
import pandas as pd
import regex as re

question = []
student_num = None
question_student_dict = {}
ans = {}
class_id = [i + 1 for i in range(15)]
student_id = []
question_submit = {}
question_pass = {}
question_pass_rate = {}


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
            if row['state'] == 'Absolutely_Correct':
                if row['title_ID'] in question_student_dict:
                    if row['student_ID'] not in question_student_dict[row['title_ID']]:
                        question_student_dict[row['title_ID']].append(row['student_ID'])
                else:
                    question_student_dict[row['title_ID']] = [row['student_ID']]

                if row['title_ID'] in question_pass:
                    question_pass[row['title_ID']] += 1
                else:
                    question_pass[row['title_ID']] = 1
            if row['title_ID'] in question_submit:
                question_submit[row['title_ID']] += 1
            else:
                question_submit[row['title_ID']] = 1

if __name__ == '__main__':
    init()
    deal()
    for q in question:
        if q in question_student_dict:
            ans[q] = len(question_student_dict[q]) / student_num
        else:
            ans[q] = 0

    for q in question:
        if q in question_pass:
            question_pass_rate[q] = question_pass[q] / question_submit[q]
        else:
            question_pass_rate[q] = 0

    with open('../data/student_pass_rate_per_question.json', 'w') as f:
        json.dump(ans, f, indent=4)

    with open('../data/question_pass_rate.json', 'w') as f:
        json.dump(question_pass_rate, f, indent=4)

