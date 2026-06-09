import pandas as pd

df = pd.read_csv(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\wild_boars.csv')

with open(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\modes.txt', 'w', encoding='utf-8') as f:
    for column in df.columns:
        mode_values = df[column].mode()
        mode_str = ', '.join([str(val) for val in mode_values])
        f.write(f"{column}: {mode_str}\n")