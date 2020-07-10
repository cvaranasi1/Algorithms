# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 16:17:52 2020

@author: chand
"""
import wget
import time

url = 'https://d18ky98rnyall9.cloudfront.net/_bcb5c6658381416d19b01bfc1d3993b5_IntegerArray.txt?Expires=1594425600&Signature=POuKa8hIF5aOkghDfLXEOG1t1MWDq~JLcz31DQdcL-VqGwBlAgmHY-pj7XG84yKuFTmBHAAaAvM9r8sw6RRZOlsESes0HoWbddGYd9fVd1Sp4cRh3IQlMmaLZt1Py5QJRDGl12IJ2Be-zkA784jPmRoaHCOndlofRVF0PE6r7Mo_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A'
wget.download(url, 'C:\\Users\\chand\\Google Drive\\CourseEra_Stuff\\Algorithms_Stanford\\Algorithms\\integerArray.txt')
L = []
with open("integerArray.txt", 'r') as file_being_read:
    for line in file_being_read:
        line = line.rstrip("\n")
        L.append(int(line))

# Now, we will write recursive sort_and_count described in the lecture
def sort_and_count(A,n):
    if n == 1:
        return 0, A
    elif n==2 and A[0] > A[1]:
        return 1, list(reversed(A))
    elif n==2 and A[0] < A[1]:
        return 0, A
    else:
        X,B = sort_and_count(A[0:n//2],len(A[0:n//2]))
        Y,C = sort_and_count(A[n//2:],len(A[n//2:]))
        D = []
        i = 0
        j = 0
        Z = 0
        while len(D) < len(B)+len(C):
            if B[i]<C[j]:
                D.append(B[i])
                i += 1
            elif B[i]>C[j]:
                D.append(C[j])
                j += 1
                Z += len(B[i:])
#            elif B[i]==C[j]:
#                D.append(B[i])
#                i += 1
#                j += 1
            if i==len(B):
                D.extend(C[j:])
                break
            if j==len(C):
                D.extend(B[i:])
                break
        return X+Y+Z,D
st=time.time()  
(ic,sa) = sort_and_count(L,len(L))  
print("--- %s seconds for inversion_counter ---" % (time.time() - st))       