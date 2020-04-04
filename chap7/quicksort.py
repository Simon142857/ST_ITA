import math
import random
#record the time cost
import time

def list_exchage(A,i,j):
    buf = A[i]
    A[i] = A[j]
    A[j] = buf

#quicksort

def PARTITION(A,p,r):
    pivot_element = A[r-1]
    i = p-1
    for j in range(p,r):
        if A[j-1]<= pivot_element:
            i = i+1
            list_exchage(A,i-1,j-1)
    list_exchage(A,i,r-1)
    return(i+1)


def QUICKSORT(A,p,r):
    if p < r:
        q = PARTITION(A,p,r)
        QUICKSORT(A,p,q-1)
        QUICKSORT(A,p+1,r)

#randomized quicksort

def RANDOMIZED_PARTITION(A,p,r):
    i = random.randint(p,r)
    list_exchage(A,i-1,r-1)
    return PARTITION(A,p,r)

def RANDOMIZED_QUICKSORT(A,p,r):
    if p < r:
        q = RANDOMIZED_PARTITION(A,p,r)
        RANDOMIZED_QUICKSORT(A,p,q-1)
        RANDOMIZED_QUICKSORT(A,p+1,r)
#test
A = [2,8,7,1,3,5,6,4]

A_normal = A[:]
A_randomized = A[:]
p = 1
r = len(A)
start_normal = time.process_time()
QUICKSORT(A_normal,p,r)
end_normal = time.process_time()

start_randomized = time.process_time()
RANDOMIZED_QUICKSORT(A_randomized,p,r)
end_randomized = time.process_time()

print("normal quicksort:\n",A_normal,"time cost:",end_normal-start_normal)
print("randomized quicksort:\n",A_randomized,"time cost:",end_randomized-start_randomized)
