def isPrime(N):
    for i in range(2,N):
        if(N%i) == 0:
            return True
    return False
def evenfactor(N):
    lst=[]
    for i in range(1,N+1):
        if((N%i ==0) and (i%2) == 0):
            lst.append(i)
    return lst
            
n = int(input())
if(n<10):
    print("Invalid Number")
elif(isPrime(n)!= True):
    print("Please input a different number")
else:
    res=[]
    prod=1
    res=evenfactor(n)
    print(sorted(res,reverse=True))
    for i in range(0,len(res)):
        prod=prod*res[i]
    print(prod)