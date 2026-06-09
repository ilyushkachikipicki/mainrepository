import pandas as pd

df = pd.read_csv(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\wild_boars.csv')
pd.set_option('display.max_rows', None)

print("Длины клыков:")
print(df['tusk_length_cm'])

min_tusk = df['tusk_length_cm'].min()
max_tusk = df['tusk_length_cm'].max()

print(f"\nСамая короткая длина клыков: {min_tusk} см")
print(f"Самая длинная длина клыков: {max_tusk} см")