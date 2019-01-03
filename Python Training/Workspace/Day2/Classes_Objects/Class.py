class Employee:
    """This is employee class"""
    cname = 'Accenture'
    def __init__(self):
        print('Inside init')
        

print(Employee.cname)
print('Document comment is',Employee.__doc__)
obj = Employee()

print('-----------------------------------------------')

class Employee1:
    """This is employee class"""
    cname = 'Accenture'
    def __init__(self, eid, ename):
        print('Inside init', eid, ename)
        
obj1 = Employee1(101, 'Chinmay')

print('-----------------------------------------------')

class Employee2:
    """This is employee class"""
    cname = 'Accenture'
    def __init__(self, eid, ename):
        self.empid = eid
        self.empname = ename
        print('Inside init', self.empid, self.empname)
        
    def info(self):
        print('Employee info is ', self.empid, self.empname)
        
obj2 = Employee2(101, 'Chinmay')
obj2.info()
print(obj2.empid, '    ', obj2.empname)


print('-----------------------------------------------')

#Privete Variables

class Employee3:
    """This is employee class"""
    cname = 'Accenture'
    def __init__(self, eid, ename):
        self.__empid = eid
        self.__empname = ename
        print('Inside init', self.__empid, self.__empname)
        
    def info(self):
        print('Employee info is ', self.__empid, self.__empname)
        
obj3 = Employee2(101, 'Chinmay')
obj3.info()
print(obj3.__empid, '    ', obj3.__empname)


print('-----------------------------------------------')
