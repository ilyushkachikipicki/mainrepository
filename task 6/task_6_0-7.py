import pandas as pd

df = pd.read_csv(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\wild_boars.csv')

numeric_columns = df.select_dtypes(include='number').columns

with open(r'C:\Users\User\Documents\semenyako_dd\projects_6\task_6_0\variation_stats.txt', 'w', encoding='utf-8') as f:
    for col in numeric_columns:
        mean = df[col].mean()
        var = df[col].var()
        std = df[col].std()
        cv = (std / mean) * 100 if mean != 0 else float('nan')
        
        f.write(f"{col}:\n")
        f.write(f"  Дисперсия: {var:.2f}\n")
        f.write(f"  Стандартное отклонение: {std:.2f}\n")
        f.write(f"  Коэффициент вариации: {cv:.2f}%\n\n")