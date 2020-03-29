import math
import re

import random


def merge(A,p,q,r,count):
    n1 = q-p+1
    n2 = r-q 
    L = A[p:q+1]
    if r == len(A)-1:
        R = A[q+1::]
    else:
        R = A[q+1:r+1]
    i = 0
    j = 0     
    for k in range(p,r+1):
        if i == n1:
            A[k:r+1] = R[j::]
            break
        elif j == n2:
            A[k:r+1] = L[i::]
            break
        else:
            if L[i]<=R[j]:
                A[k] = L[i]
                i = i+1
            else:
                A[k] = R[j]
                j = j+1
                count[0] = count[0] +len(L[i::])
    return

def merge_sort(A,p,r,count):
    if p < r:
        q = math.floor((r+p)/2)
        merge_sort(A,p,q,count)
        merge_sort(A,q+1,r,count)
        merge(A,p,q,r,count)
        return 
    else:
        return 


for n in range(90,100):
    E_calculate = n*(n-1)/4

    sum_average = 0
    A_original = [i for i in range(n)]
    time = 2000
    t = 0
    while t < time:
    
        A = A_original[:]
        random.shuffle(A) 
        sum = 0
        p = 0
        count = [0]
        r = len(A)-1

        merge_sort(A,p,r,count)

        sum_average = (sum_average*t + count[0])/(t+1)

        t = t+1
        if t == time:
            print("list length:",n,"   loop time:",t,"\n test E:",sum_average,"   calculate E:",E_calculate)
            print("error",abs(math.floor(100*(sum_average-E_calculate)/E_calculate)),"%")
    
    # A_sort = A[:]
    # A_output = " ".join([str(x) for x in A_sort])

    # print("The sorted list:\n",A_output)
    # print("The number of the inversion in the original list is: ",inversion_count,"\n")
    # answer = input("Do you want to continue ? (y/[n])")
    # if answer in "nN":
        # break

