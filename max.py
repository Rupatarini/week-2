import pandas as pd
data = {'A': [1, 2, 3],
        'B': [10, 20, 15],
        'C': [5, 6, 7]}
df = pd.DataFrame(data)
max_value = df[data].max()
print(max_value)
