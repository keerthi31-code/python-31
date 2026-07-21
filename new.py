def prime_num(n):
    res=[]

    for num in range(2,n+1):
        is_prime=True

        for i in range(2,num):

            if num%i==0:
                is_prime= False
                break
        if is_prime:
            res.append(num)        
    return res

print(prime_num(30))

import math
def prime_num(n):
    res=[]
    for num in range(2,(n**0.5)+1):
        if n%num==0:
            return False
        else:
            res.append(num)
    return res
print(prime_num(30))
        