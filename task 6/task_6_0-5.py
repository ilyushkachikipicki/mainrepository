import pandas as pd

df = pd.read_csv(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\wild_boars.csv')

numeric_columns = df.select_dtypes(include='number').columns

percentiles = [0.25, 0.5, 0.75, 0.9, 0.95, 1.0]
labels = ['25% (Q1)', '50% (Q2/Медиана)', '75% (Q3)', '90%', '95%', '100% (Максимум)']

with open(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\percentiles.txt', 'w', encoding='utf-8') as f:
    for col in numeric_columns:
        f.write(f"\n{col}:\n")
        for p, label in zip(percentiles, labels):
            value = df[col].quantile(p)
            f.write(f"  {label}: {value:.1f}\n")