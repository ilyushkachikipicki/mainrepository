import pandas as pd

df = pd.read_csv(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\wild_boars.csv')

means = df.mean(numeric_only=True)

with open(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\avg_means.txt', 'w', encoding='utf-8') as f:
    for param, value in means.items():
        f.write(f"{param}: {value:.2f}\n")