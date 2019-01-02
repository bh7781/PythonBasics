try:
    ans = 10 / 0
    print(ans)
except:
    print('Exception occurred in division')
    
    
print('Out of try-except block')

try:
    name = 'Chinmay'
    print(name[100])
except:
    print('Exception occurred')
    

try:
    name = 'Chinmay'
    ans = 10 / 0
    print(ans)
    print(name)
except IndexError:
    print('Exception occurred in Name related code')
except ZeroDivisionError:
    print('Division by zero found')
finally:
    print('Closing application')
    

try:
    name = 'Chinmay'
    ans = 10 / 0
    print(ans)
    print(name)
except IndexError:
    print('Exception occurred in Name related code')
finally:
    print('Closing application')