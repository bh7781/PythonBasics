class Person:
    def pinfo(self):
        print('Pinfo in Person class')
        
class Human:
    def __init__(self, age):
        print('Human init', age)
    def humanInfo(self):
        print('humanInfo in Human class')
        
class Employee3(Person, Human):
    """This is employee class"""
    cname = 'Accenture'
    def __init__(self, eid, ename):
        super().__init__(25)
        self.__empid = eid
        self.__empname = ename
        print('Inside init', self.__empid, self.__empname)
        
    def info(self):
        print('Employee info is ', self.__empid, self.__empname)
        
obj = Employee3(101, 'Chinmay')
obj.info()
obj.pinfo()
obj.humanInfo()