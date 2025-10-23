import pandas as pd

data = {'college': ['dtu', 'nsut', 'dtu', 'iiitd', 'nsut']}
df = pd.DataFrame(data)

map = {'dtu': 'good', 'nsut': 'bad', 'iiitd': 'bad'}

df['status'] = df['college'].map(map)

print("original data:")
print(df)