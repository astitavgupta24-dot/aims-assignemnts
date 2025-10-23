import pandas as pd
import numpy as np

data = {'club': ['liverpool', 'ac milan', 'liverpool', 'manchester city','barcelona','arsenal']}
df = pd.DataFrame(data)

clubs = df['club'].to_list()

df2 = pd.DataFrame()

for football in clubs:
    df2[football] = np.where(df['club'] == football, 1, 0)

df3 = pd.concat([df, df2], axis=1)

print("encoded data:")
print(df3)