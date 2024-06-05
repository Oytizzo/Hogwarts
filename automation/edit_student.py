import json
from colorama import Fore, Style, init
import pandas as pd

environments = ["dev", "testing", "production", "staging"]
env = environments[0]

students_created_excel_file_path = f"/Users/zeuz/Desktop/bb/test_data/{env}_students_created.xlsx"
students_not_created_excel_file_path = f"/Users/zeuz/Desktop/bb/test_data/{env}_students_not_created.xlsx"

df = pd.read_excel(students_created_excel_file_path)

df['dob'] = pd.to_datetime(df['dob']).dt.strftime('%m/%d/%Y')
df['date_of_joining'] = pd.to_datetime(df['date_of_joining']).dt.strftime('%m/%d/%Y')
df['schedule_date'] = pd.to_datetime(df['schedule_date']).dt.strftime('%m/%d/%Y')

students = df.to_dict(orient="records")

def dprint(value:dict):
    print(Fore.GREEN + Style.NORMAL + json.dumps(value, indent=4))

for student in students:
    if student["created"] == "No":
        dprint(student)
        student["created"] = "Yes"
        dprint(student)
        students_df = pd.DataFrame(students)
        students_df.to_excel(students_created_excel_file_path, index=False)
