import pandas as pd

df = pd.DataFrame({'A':[61.75,10.25], 'B':[0.62,0.45]})

print(df)

df['A'] = df['A'].div(100).round(2)

print(df)