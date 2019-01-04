import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('csk.xlsx')

df.plot(kind='bar')
plt.show()