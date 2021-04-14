from random import randint

class RandList():
    """
        Создает список, заполненный случайными числами. 
    """
    def __init__(self, rows = None, cols = None):
        self.list = []
        if cols == None and rows == None:
            for x in range(0, 5):
                a = []
                for y in range(0, 5):
                    a.append(randint(0,100))
                self.list.append(a)
        else:
            for x in range(0, rows):
                a = []
                for y in range(0, cols):
                    a.append(randint(0,100))
                self.list.append(a)

    def __repr__(self):
        return repr(self.list)


    def print_data(self):
        for x in self.list:
            for y in x:
                print(y, end = ' ')
            print('\n')
        print('\n')

    def find_num(self, num):
        i = 0
        while i < len(self.list):
            j = 0
            while j < len(self.list[i]):
                if self.list[i][j] == num:
                    print(j)
                    return j
                j += 1
            i += 1
        print(num, ' нет в списке')
        return None


if __name__ == '__main__':
    
    a = RandList()
    b = RandList(23, 15)

    a.print_data()
    b.print_data()

    a.find_num(13)
    b.find_num(13)
