
class MinHeap(object):
    
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self,i):
        
        while i // 2 > 0:
            
            if self.heap_list[i] < self.heap_list[i // 2]:
                tmp = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tmp
            i = i // 2

    def insert(self,k):
        
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.perc_up(self.currentSize)    

        def percDown(self,i):
        
        while (i * 2) <= self.currentSize:
            
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def minChild(self,i):
        
        if i * 2 + 1 > self.currentSize:
            
            return i * 2
        else:
            
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1 