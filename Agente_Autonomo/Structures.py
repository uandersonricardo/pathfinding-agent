class PriorityQueue(object):
    def __init__(self):
        self.l = []
  
    def __str__(self):
        return str(self.l)

    def empty(self):
        return len(self.l) == 0

    def put(self, data, priority):
        self.l.append((data, priority))
  
    def get(self):
        try:
            min = 0
            for i in range(len(self.l)):
                if self.l[i][1] < self.l[min][1]:
                    min = i
            item = self.l[min][0]
            del self.l[min]
            return item
        except IndexError:
            print()
            exit()
            
class Queue(object):
    def __init__(self):
        self.l = []
  
    def __str__(self):
        return str(self.l)
  
    def empty(self):
        return len(self.l) == 0

    def put(self, data, *args):
        self.l.append(data)

    def get(self):
        try:
            return self.l.pop(0)
        except IndexError:
            print()
            exit()
            
class Stack(object):
    def __init__(self):
        self.l = []
  
    def __str__(self):
        return str(self.l)
  
    def empty(self):
        return len(self.l) == 0

    def put(self, data, *args):
        self.l.append(data)

    def get(self):
        try:
            return self.l.pop()
        except IndexError:
            print()
            exit()
