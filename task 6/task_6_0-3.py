import pandas as pd

df = pd.read_csv(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\wild_boars.csv')

medians = df.median(numeric_only=True)

with open(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\medians.txt', 'w', encoding='utf-8') as f:
    for column, median_value in medians.items():
        f.write(f"{column}: {median_value:.2f}\n")