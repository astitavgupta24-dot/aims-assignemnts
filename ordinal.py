import pandas as pd

df = pd.read_csv('/Users/astitav/Desktop/aims/aims-assignemnts/PlayStation Sales and Metadata (PS3PS4PS5) (Oct 2025).csv')

map = {'PS3': '1', 'PS4': '2', 'PS5': '3'}

df['status'] = df['Console'].map(map)

print("original data:")
print(df[['Console','status']])