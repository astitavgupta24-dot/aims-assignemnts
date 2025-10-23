import pandas as pd

data = {'age': [22, None, 25, None, 30,44,None]}
df = pd.DataFrame(data)

meanage = df['age'].mean()
df['age'] = df['age'].fillna(meanage)


print("data after imputation: \n",df)

