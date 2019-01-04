import sqlite3
import pandas as pd

connection = sqlite3.connect('C:\Chinmay\PythonBasics\Database\Info.db')
print('Connected to ', connection)

df = pd.read_sql('SELECT * FROM Employee', connection)

print(df)
