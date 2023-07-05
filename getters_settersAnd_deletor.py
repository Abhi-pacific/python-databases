import re
class Details:
    """Here self represent the object of a class means for example "an = Details(Abhsihek,Chauhan)" so self represent the an """
    try:
        def __init__(self,fname,lname):
            self.fname = fname
            self.lname = lname
    except:
        print('Must Pass 2 parameters ')
    # using the decorator to set the property
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return 'Email Id not exist please set it the help of setter'
        return f'Your email id is {self.fname}.{self.lname}@gmail.com'
    # creating a setter so that we assign the values
    # for this we must the name of attribute, which want take as input in my case it is email
    @email.setter
    def email(self,string):
        data = string.split('@')
        names = data[0].split('.')
        self.fname = names[0]
        self.lname = names[1]
    #


    
                
