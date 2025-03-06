# parent class
class person( object ):
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee( person ):
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the _init_ of the parent class
        person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Makinde', 20210401, 15000, "Intern")
b = Employee('kunle', 20210402, 25000, "manager")
c = Employee('kola', 20210403, 35000, "CEO")

# calling a function of the class person using its instance
a.display()
b.display()
c.display()