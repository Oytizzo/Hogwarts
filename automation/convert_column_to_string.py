import json
from colorama import Fore, Style, init
import pandas as pd

environments = ["dev", "testing", "production", "staging"]
env = environments[1]

students_excel_file_path = f"/Users/zeuz/Desktop/bb/test_data/{env}_students.xlsx"

df = pd.read_excel(students_excel_file_path)

print("\nTypes of data before conversion:\n", df.dtypes)
print(df)

# for item in df:
#     df[item] = df[item].astype(str)

# # df["teacher_id_2"] = df["teacher_id_2"].astype(str)
# # df["teacher_id_2"] = df["teacher_id_2"].astype(str)
# # df["teacher_id_2"] = df["teacher_id_2"].astype(str)
# print("\nTypes of data after conversion:\n", df.dtypes)
# print(df)
# df.to_excel(students_excel_file_path, index=False)
