class Employee:
    def display(self):
        print('base class running')
    def data(self):
        print('data function calling')
class Emp(Employee):
    def driveclass(self):
        print('vhild class is running')
def main():
    a = Emp()
    a.data()
main()