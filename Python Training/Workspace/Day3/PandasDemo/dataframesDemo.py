import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_excel('csk.xlsx')

print('This is DataFrame: \n\n', df, '\n------------------------------\n\n')

print('\nColumns: ', df.columns)
print('\nAxes: ', df.axes)
print('\nSize: ', df.size)
print('\nValues: ', df.values)
print('------------------------------------------')
df.info()
print('------------------------------------------')
print(type(df[['ID']]))
print('------------------------------------------')
print(df[['ID','Name']])
print('------------------------------------------')
print(type(df.ID))
print('------------------------------------------')
print(df.loc[0:2])
print('------------------------------------------')
df['Salary/IPL'] = pd.Series(['15Cr', '5Cr', '6Cr', '45Cr', 
                          '2Cr', '8.5Cr', '90L', '2Cr',
                          '13Cr', '9Cr', '6Cr'])
print(df)
print('------------------------------------------')
#df.to_excel('csk.xlsx', index=False)
print('------------------------------------------')
data = pd.Series([12, 'Ngidi', 20, '1Cr'], 
                 index=['ID', 'Name', 'Age', 'Salary/IPL'])
df = df.append(data, ignore_index=True)
print(df)
print('------------------------------------------')
df.pop('ID')
print(df)
print('------------------------------------------')