#!/usr/bin/env python3


# This is the python script to count the inversion of the number list


#simon 
import math
import re

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

while True:

    p = 0
    count = [0]
# A = [2,3,8,6,1]
    A_input = input("enter the number list: \n")
    A_str = re.split(" |\.|\,",A_input.strip())
    A = [int(x) for x in A_str]
    r = len(A)-1


    merge_sort(A,p,r,count)

    inversion_count = count[0]
    A_sort = A[:]
    A_output = " ".join([str(x) for x in A_sort])


    print("The sorted list:\n",A_output)
    print("The number of the inversion in the original list is: ",inversion_count,"\n")
    answer = input("Do you want to continue ? (y/[n])")
    if answer in "nN":
        break

