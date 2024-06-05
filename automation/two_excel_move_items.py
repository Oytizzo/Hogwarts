import json
from colorama import Fore, Style, init
import pandas as pd
students_excel_file_path = "/Users/zeuz/Desktop/contrib/personal/Hogwarts/automation/pandas_automation/students_not_created.xlsx"

df = pd.read_excel(students_excel_file_path)
df['dob'] = pd.to_datetime(df['dob']).dt.strftime('%m/%d/%Y')
df['date_of_joining'] = pd.to_datetime(df['date_of_joining']).dt.strftime('%m/%d/%Y')

df['schedule_date'] = pd.to_datetime(df['schedule_date']).dt.strftime('%m/%d/%Y')

students = df.to_dict(orient="records")

for student in students:
    if student["created"] == "No":
        student_1 = student
        break
if student_1 == students[0]:
    student = student_1
else:
    student = {}
def dprint(value:dict):
    print(Fore.GREEN + Style.NORMAL + json.dumps(value, indent=4))


def lprint(value:list):
    print(Fore.MAGENTA + Style.NORMAL + json.dumps(value, indent=4))

lprint(students)
dprint(student)

student['created'] = "Yes"
dprint(student)

if student['created'] == "Yes":
    students.remove(student)

dprint(students[0])
print(len(students))