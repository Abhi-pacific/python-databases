'''
In this program i am using classes, super() and class Method (@classmethod) it is a decurator which we use to alter the class variable  

'''
class Details:
    subject = 'Pyhton'
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def displayFunction(self):
        print(f'Your name is {self.fname} {self.lname}')
        print(f'Your subject is {self.subject}')
    @classmethod
    def changeSub(cls,string):
        cls.subject = string
    

class Infromation(Details):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
    def displayMessage(self):
        print('thank you for using me')

def main():
    I = Infromation('Abhishek','Chauhan')
    I.displayFunction()
    I.displayMessage()
    I.changeSub('Database')
    I.displayFunction()
main()