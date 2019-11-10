import unittest

'''
The solution is based on a queue to keep track of
balanced parentheses.
A balanced paranthesis begins with '(' and ends with ')'.
We add the '(' s when encountered and we remove from the queue when
we encounter ')'. We keep track of the best length in a counter.
The counter gets reintialized to zero if the current sequence is no 
longer balanced.
'''

class Queue:

    def __init__(self):
        self.list = []
    
    def remove(self):
        self.list = self.list[:-1]
    
    def empty(self):
        if len(self.list)==0:
            return True
        else:
            return False
    
    def add(self,val):
        self.list = [val]+self.list

def longest(l):

    queue = Queue()
    best = 0
    B = True
    for el in l:
        #the balanced sequence has to begin with '('
        if B and el=='(':
            cpt = 0
            B = False

        if not B:
            if el =="(":
                queue.add(el)
            else:
                #we haven't encountered any misbalance yet
                if not queue.empty():
                    queue.remove()
                    cpt+=2
                    if cpt>best:
                        best = cpt
                #misbalance occurred or we are done in the loop
                else:
                    B = True
    
    return best

class BalancedParenthesesTest(unittest.TestCase):

    def test1(self):
        parentheses = '( ( ( ( ( ( ('.split()
        self.assertEqual(0,longest(parentheses))

    def test2(self):
        parentheses = ') ) ) ) ) )'.split()
        self.assertEqual(0,longest(parentheses))

    def test3(self):
        parentheses = ') ) ( ( ) ) ) ) ) ( ( ( ( ( )'.split()
        self.assertEqual(4,longest(parentheses)) 

    def test4(self):
        parentheses = '( ( ( ( ( ( ) ) ) ) ) )'.split()
        self.assertEqual(12,longest(parentheses))

if __name__ == "__main__":
    #unittest.main()
    p = '( ) ('.split()
    print(longest(p))