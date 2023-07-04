# my first class program
class PartyAnimal:
    x = 0
    def party(self):
        self.x = self.x + 1
        print(f'So far the value of x is {self.x}')

if __name__ == '__main__':
    def main():
        an = PartyAnimal()
        an.party()
        # we can write this also in otherways for example
        PartyAnimal.party(an)
    main()