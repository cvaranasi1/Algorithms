# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:52:53 2020

@author: Chandra Varanasi
"""

def prod(n1,n2):
    if len(n1)==1 and (n1 != '' and n2 != ''):
        return int(n1)*int(n2)
    elif len(n2)==1 and (n1 == '' and n2 != ''):
         return 0
    elif len(n1)==1 and (n1 != '' and n2 == ''):
         return 0
    elif n1 == '' and n2 == '':
         return 0
    
    else:
        hLa = len(str(n1))//2
        hLb = len(str(n1))//2
        a = n1[0:hLa]
        b = n1[hLa:]
        c = n2[0:hLb]
        d = n2[hLb:]
        return 10**len(n1)*prod(a,c) + 10**hLa*(prod(a,d) + prod(b,c)) + prod(b,d)
        
def karatsuba(n1,n2):
    if len(n1)==1 and len(n2)==1:
        return int(n1)*int(n2)
    else:
        dval = abs(len(n1)-len(n2))
        if len(n1) <= len(n2):
            n1 = '0'*dval + n1
        else:
            n2 = '0'*dval + n2
        if len(n1)%2 == 1:
            n1 = '0'+n1
            n2 = '0'+n2
        # Now, both n1 and n2 are same length and even
        lenVal = len(n1)
        k1 = 10**(lenVal//2)
        k2 = 10**lenVal
        a = n1[0:lenVal//2]
        b = n1[lenVal//2:]
        c = n2[0:lenVal//2]
        d = n2[lenVal//2:]   
        q1 = str(int(a) + int(b))
        q2 = str(int(c) + int(d))
        defi = abs(len(q1)-len(q2))
        if len(q1) <= len(q2):
            q1 = '0'*defi + q1
        else:
            q2 = '0'*defi + q2
        if len(q1)%2 == 1 and len(q1) != 1:
            q1 = '0'+q1
            q2 = '0'+q2
        # Now, both q1 and q2 are same length and even
        p1 = karatsuba(a,c)
        p2 = karatsuba(b,d)
        p3 = karatsuba(q1, q2)
            
        return k2*p1 + (p3-p1-p2)*k1 + p2

    
import time
#n1 = '3141592653589793238462643383279502884197169399375105820974944592'
#n2 = '2718281828459045235360287471352662497757247093699959574966967627'
n1 = '9509090958164057267497022913300417684341772484307875629755329462831070821785127159670052473793464100979339895889746353138559887988294355346396259803963956030063880220813053988520717421913782288218444359253148866287554851687427214264758532702784990463166050'
n2 = '8869905480101421754029658022141462145364998772684420847838410201867544038345041673755428184096957803661971239945690101337347013995167200299368957070993663445317591147229634611657120605175033869194756084492011109267497808621959974001499202660852430421078437'
#n1 = '950909095816405726749702291330041768434177248430787562975532946283'
#n2 = '950909095816405726749702291330041768434177248430787562975532946283'
#n1 = '1234'
#n2 = '5678'
start_time = time.time()
print(prod(n1,n2))
print("--- %s seconds for recursive multiplication ---" % (time.time() - start_time))
start_time = time.time()
print(karatsuba(n1,n2))
print("--- %s seconds for Karatsuba multiplication ---" % (time.time() - start_time))
