import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_excel('csk1.xlsx')

print(df)
print('------------Age greater than 30----------------------------')

ans = df['Age'] > 30
print(df[ans])
print('---------------Age less than 30-------------------------')
print(df[df['Age'] < 30])
print('---------------Name = Mahendra-------------------------')
print(df[df.Name == 'Mahendra'])
print('----------------Best of 3------------------------')
print(df[df.Name.isin(['Mahendra', 'Dwayne', 'Suresh'])])
print('-------------------Best of 3 AND Age greater than 30---------------------')
print(df[(df.Age > 30) & (df.Name.isin(['Mahendra', 'Dwayne', 'Suresh']))])
print('-------------------Best of 3 OR Age greater than 30---------------------')
print(df[(df.Age > 30) | (df.Name.isin(['Mahendra', 'Dwayne', 'Suresh']))])
print('----------------------------------------')
df['Salary'] = pd.Series([])
print(df)
print('----------------------------------------')
df.loc[df.Age > 30, 'Salary'] = '10Cr'
df.loc[df.Age < 30, 'Salary'] = '5Cr'
print(df)
