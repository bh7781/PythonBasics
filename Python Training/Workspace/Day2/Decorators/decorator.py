# Without Decorators

def add():
    print('add function___Without decorators')
    
add()

print('\n\n--------------------------------------------------\n\n')

# With decorators

def myDec(anyFunc):
    def inner(*val):
        print('You can do pre task here before calling anyFunc().')
        anyFunc(*val)
        print('Arguments passed: ', val)
        print('anyFunc called here is: ',anyFunc.__name__,)
        print('You can also do post task here after calling anyFunc() ')
    return inner

@myDec
def add1():
    print('add1 function___With decorators')
    
@myDec
def login(username, password):
    print('login function___With decorators', username, password)
    
myDec(add1())
print('\n\n--------------------------------------------------\n\n')
myDec(login('admin', 'admin123'))
