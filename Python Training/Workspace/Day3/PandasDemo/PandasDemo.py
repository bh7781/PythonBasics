import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_table('data', header=0, nrows = 2)

print(df, '\n\n\n-------------------------------')

df1 = pd.read_csv('annual-enterprise-survey.csv', header = 0)

print('annual-enterprise-survey.csv\n\n',df1.head(5))
