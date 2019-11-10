import unittest

'''
The supposed data type is a list of lists.
We navigate the iterator in a circular way until no elements are available: 
for example we start with index 0, then 1, then 2, then 0 again, then 1....
This is done using the rest of the euclidean division every time we iterate.

We ignore the list in the current index of the iterator if it has 0 available 
elements, otherwise we can iterate and then we decrease the number of available 
elements by 1.
'''

class FlattenedIterator:

    def __init__(self,iterators):
        self.iterators = iterators
        self.indices = [i for i in range(len(self.iterators))]
        self.nb_remaining_el_each_iterator = [len(el) for el in iterators]
        self.current = -1

    def next(self):
        #current index for the possibly available elements, we increase the 
        #older step by 1 modulo the available elements to stay within the 
        #bounds of the list.
        self.current = (self.current+1)%len(self.indices)

        ind = self.indices[self.current]
        
        #if this condition is satisfied, there are still elements in the 
        #current index to explore
        if self.nb_remaining_el_each_iterator[ind]!=0:
            iter_length = len(self.iterators[ind])
            remaining_length = self.nb_remaining_el_each_iterator[ind]
            next_el = self.iterators[ind][iter_length-remaining_length]
            self.nb_remaining_el_each_iterator[ind]-=1
            return next_el
        #if not, this means that we don't have to consider this index anymore 
        #so we delete it and step back
        else:
            del self.indices[self.current]
            self.current-=1
            return self.next()
    
    def hasNext(self):
        if sum(self.nb_remaining_el_each_iterator)!=0:
            return True
        else:
            return False

class Tests(unittest.TestCase):

    def test1(self):
        iterators=[[],[],[],[]]
        flattenedList = create(iterators)
        self.assertEqual(flattenedList,[])

    def test2(self):
        iterators=[[1,3],[10,5,6],[2,8,9,11],[7]]
        flattenedList = create(iterators)
        self.assertEqual(flattenedList,[1,10,2,7,3,5,8,6,9,11])

    def test3(self):
        iterators=[[0],[1],[2],[3]]
        flattenedList = create(iterators)
        self.assertEqual(flattenedList,[0,1,2,3])

    def test4(self):
        iterators=[[1,2,3,4],[],[],[]]
        flattenedList = create(iterators)
        self.assertEqual(flattenedList,[1,2,3,4])

    def test5(self):
        iterators=[[1,2,3],[4,5,6],[7,8,9]]
        flattenedList = create(iterators)
        self.assertEqual(flattenedList,[1,4,7,2,5,8,3,6,9])

def create(iterators):

    iterator = FlattenedIterator(iterators)
    flattened =[]
    while True:
        if(iterator.hasNext()):
            flattened.append(iterator.next())
        else:
            break
    
    return flattened

if __name__ == "__main__":
    unittest.main()
