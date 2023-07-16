def data_item(func):
    def data(a,b):
        if a < b:
            a,b = b,a
            print('Changes are made in variable')
        func(a,b)
    return data
@data_item
def div(a,b):
    print('The division of the a and b are :{:^10}'.format(a/b))

def main():
    div(2,4)
main()