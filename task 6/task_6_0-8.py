import pandas as pd

df = pd.read_csv(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\wild_boars.csv')

with open(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\cv_tusk_by_gender.txt', 'w', encoding='utf-8') as f:
    for gender in df['gender'].unique():
        group = df[df['gender'] == gender]['tusk_length_cm']
        mean = group.mean()
        std = group.std()
        cv = (std / mean) * 100 if mean != 0 else float('nan')
        f.write(f"{gender}: {cv:.2f}%\n")