import pandas as pd

df = pd.read_csv(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\wild_boars.csv')

with open(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\iqr_by_gender.txt', 'w', encoding='utf-8') as f:
    for gender in df['gender'].unique():
        group_data = df[df['gender'] == gender]['length_cm']
        q1 = group_data.quantile(0.25)
        q3 = group_data.quantile(0.75)
        iqr = q3 - q1
        f.write(f"{gender}: {iqr:.1f} cm\n")