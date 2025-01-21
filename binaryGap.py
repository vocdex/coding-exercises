""" Given a positive N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap."""
"""Solution: 
1. Traverse the sequence
2. Increment a counter variable for each zero split
3. Get new max counter by comparing it with the current counter value
4. Reset the current counter value to 0
Complexity: O(n) just traversing for-loop"""

def binaryGap(n):
    N=bin(n)[2:]
    if(N.count('1'))==1:
        return 0
    b=0
    maxb=0
    for k in N:
        if int(k)==0:
            b+=1
        elif int(k)==1:
            maxb=max(b,maxb)
            b=0
    return maxb+1
# Given two binary strings a and b, return their sum as a binary string
def addBinary(a,b):
    return bin(int(a,2)+int(b,2))[2:]
nums=[1,1,1,2]
print(1^5)