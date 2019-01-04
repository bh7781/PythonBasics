import matplotlib.pyplot as plt

size = [30,30,20,20]
lab = ['India', 'US', 'Japan', 'UK']

#plt.pie(x=size, labels=lab, explode=[0.05,0,0,0], 
        #colors=['red', 'grey', 'yellow', 'indigo'])
#plt.xlabel('Countries')
#plt.show()

y = [10,3,8,5,6,9]
x = ['A','B','C','D','E', 'F']
width = 0.2

plt.barh(x, y, width, color = ['yellow', 'blue'])
plt.xlabel('Shares')
plt.ylabel('Price')
plt.title('Information about shares')
plt.show()