class Emp:
    company = 'ROG'
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def showData(self):
        print(f'hello {self.fname} {self.lname} your company is {self.company}')
    # Using classmethod so that we can change the value of class variable
    @classmethod
    # we are using cls but we can also use self or any other name but because of convension we use cls ('class')
    def changeVar(cls,name):
        cls.company = name
def main():
    E = Emp('Abhishek','Chauhan')
    Emp.showData(E)
    E.changeVar('Apple')
    E.showData()
main()
