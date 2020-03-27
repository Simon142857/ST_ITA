#!/usr/bin/env python3

# this is the python script i write to adress the maximun subarry question in the chapter 4

# simon

import math
import re

def fing_crossing_maxsubarray(A,low,mid,high):
    left_sum = float("-inf")
    right_sum = float("-inf")
    suml = 0
    sumr = 0

    for i in range(mid,low-1,-1):
        suml = suml + A[i]
        if suml >left_sum:
            left_sum = suml
            max_left = i

    for i in range(high,mid,-1):
        sumr = sumr + A[i]
        if sumr >right_sum:
            right_sum = sumr
            max_right = i

    return(max_left,max_right,left_sum+right_sum)

def find_max_subarray(A,low,high):
    if high == low:
        return(low,high,A[low])
    else:
        mid = math.floor((low+high)/2)
        (left_low,left_high,left_max) = find_max_subarray(A,low,mid)
        (right_low,right_high,right_max) = find_max_subarray(A,mid+1,high)
        (cross_low,cross_high,cross_max) = fing_crossing_maxsubarray(A,low,mid,high)
        
        if left_max >= right_max and left_max >= cross_max:
            return(left_low,left_high,left_max)
        elif right_max >= left_max and right_max >= cross_max:
            return(right_low,right_high,right_max)
        else:
            return(cross_low,cross_high,cross_max)

A_input = input("Please enter the original number diff list \n")
A_str = re.split(" |\,",A_input.strip())
A = [float(x) for x in A_str]

low_init = 0
high_init = len(A)-1

(low,high,max_sum)=find_max_subarray(A,low_init,high_init)

print(" From number ",low+1," to number ",high+1," in your list")
print("is the max subarray of the enter array, and the sum is ",max_sum)







