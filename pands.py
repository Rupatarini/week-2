import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data_series = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Series:")
print(data_series)
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12],
    'D': [13, 14, 15, 16]
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)
print("\nHead of DataFrame:")
print(df.head())
print("\nTail of DataFrame:")
print(df.tail())
print("\nDataFrame Info:")
print(df.info())
print("\nDataFrame Description:")
print(df.describe())
data2 = {
    'key': ['A', 'B', 'C', 'D'],
    'value': [10, 20, 30, 40]
}
df2 = pd.DataFrame(data2)
df_merged = pd.merge(df, df2, left_on='A', right_on='key')
print("\nMerged DataFrame:")
print(df_merged)
grouped = df.groupby('A').sum()
print("\nGrouped DataFrame by 'A':")
print(grouped)
df_dropped = df.drop(['B'], axis=1)
print("\nDataFrame with Column 'B' Dropped:")
print(df_dropped)
df_with_nan = df.copy()
df_with_nan.iloc[1, 1] = np.nan
print("\nDataFrame with NaN:")
print(df_with_nan)
df_filled = df_with_nan.fillna(999)
print("\nNaN Filled DataFrame:")
print(df_filled)
print("\nCheck for NaN (isnull):")
print(df_with_nan.isnull())
print("\nCheck for Non-NaN (notnull):")
print(df_with_nan.notnull())
df_applied = df.apply(lambda x: x * 2)
print("\nDataFrame after Applying Function:")
print(df_applied)
df_sorted_by_values = df.sort_values(by='A', ascending=False)
print("\nDataFrame Sorted by Values in Column 'A':")
print(df_sorted_by_values)
df_sorted_by_index = df.sort_index(ascending=False)
print("\nDataFrame Sorted by Index:")
print(df_sorted_by_index)
df.plot(kind='bar', x='A', y='B')
plt.title('Bar Plot of A vs B')
plt.show()

