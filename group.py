import pandas as pd
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'C'],
    'Value': [10, 20, 30, 40, 50, 60]
})	
grouped = df.groupby('Category')['Value'].mean()
print(grouped)
