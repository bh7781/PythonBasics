import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_excel('csk.xlsx')

print('This is DataFrame: \n\n', df, '\n------------------------------\n\n')

print(df.sum())
print('Max age is: ',df['Age'].max())
print('-----------------------------------------------------')
print(df.sort_index(axis=1, ascending=True, inplace=True))
print(df)
print('-----------------------------------------------------')
print(df.sort_values(by = 'Name'))
print('-----------------------------------------------------')
for k,v in df.iteritems():
    print(k)
    print(v)
print('-----------------------------------------------------')
for k,v in df.iterrows():
    print(k)
    print('___________________________')
    print(v)
