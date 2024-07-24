import pandas as pd
from io import StringIO
csv_data = """name,age,city
Rupa,20,HYD
Gayi,25,SKLM
kavya,35,VZ
"""
csv_file = StringIO(csv_data)
df = pd.read_csv(csv_file)
print(df)
