class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

        def printname(self):
            print(self.fname, self.lname)

class Student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

x = Student("Mike","Olsen",2019)
x.printname()
print(x.graduationyear)

y= Student("John","Doe",2022)
y.printname()
print(y.graduationyear)

