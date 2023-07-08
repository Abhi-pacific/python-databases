import pyttsx3
class Vector:
    def __init__(self,i,k):
        self.i = i
        self.k = k
    
    # Here both the self and self_1 are the object of a class 
    def __add__(self,self_1): 
        return Vector(self.i + self_1.i,self.k + self_1.k)
    def __str__(self):
        return f'{self.i}i + {self.k}k'
    

def main():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    engine.setProperty('volume',1.0)
    engine.say('Welcome to Operator overloading')
    engine.runAndWait()
    V = Vector(2,4)
    W = Vector(3,6)
    print(V + W)
main()