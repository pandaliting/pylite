class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

class Stock(Subject):
    def __init__(self, data):
        Subject.__init__(self)
        self.data = data 

    def update(self, data):
        self.data = data
        self.notify()

class Tom:
    def update(self, subject):
        print 'Tom: %d' % subject.data

class Jerry:
    def update(self, subject):
        print 'Jerry: %d' % subject.data

def main():
    stock = Stock(100)
    tom = Tom()
    jerry = Jerry()
    stock.attach(tom)
    stock.attach(jerry)
    stock.update(110)
    stock.update(90)

main()

