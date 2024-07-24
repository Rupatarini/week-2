import pandas as pd
from io import StringIO
csv_data = """A,B,C
1,6,11
2,7,12
3,8,13
4,9,14
5,10,15
6,11,16
7,12,17
8,13,18
9,14,19
10,15,20
11,16,21
12,17,22
"""
csv_file = StringIO(csv_data)
df = pd.read_csv(csv_file)
first_ten_rows = df.head(10)
print(first_ten_rows)
