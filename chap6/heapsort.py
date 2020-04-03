import math

#calss define
class Heap(object):
    def __init__(self,LIST,LENGTH):
        self.list = LIST
        self.heap_size = LENGTH



def PARENT(i):
    return math.floor(i/2)

def LEFT(i):
    return 2*i

def RIGHT(i):
    return 2*i+1

def MAX_HEAPIFY(A,i):
    l = LEFT(i)
    r = RIGHT(i)

    if l <= A.heap_size and A.list[l-1]>A.list[i-1]:
        largest = l
    else:
        largest = i

    if r <= A.heap_size and A.list[r-1]>A.list[largest-1]:
        largest = r

    if largest != i :
        buf = A.list[i-1]
        A.list[i-1] = A.list[largest-1]
        A.list[largest-1] = buf

        MAX_HEAPIFY(A,largest)

def BUILD_MAX_HEAP(A):
    for i in range(PARENT(A.heap_size),0,-1):
        MAX_HEAPIFY(A,i)


def HEAPSORT(A):
    BUILD_MAX_HEAP(A)
    for i in range(len(A.list),1,-1):
        buf  = A.list[i-1]
        A.list[i-1] = A.list[0]
        A.list[0] = buf
        A.heap_size = A.heap_size-1
        MAX_HEAPIFY(A,1)
        
        
#instance initialize
heaplist = [4,1,3,2,16,9,10,14,8,7]
A = Heap(heaplist,len(heaplist))
HEAPSORT(A)
print(A.list)
