def factors(n):   # traditional function that computes factors
    results= []   #store factors in a list
    for k in range(1,n+1):
        if n % k ==0:     #divides evenly thus k is a factor
            results.append(k)   #add k to the list
    return results #return list

def factors_gen(n):
    for k in range(1,n+1):
        if n%k ==0:
            yield k
#test
num=100
#gen call
mygenerator = factors_gen(num)
print(mygenerator)
#trad call
print(factors(num))
#print yield
for i in mygenerator:
    print(i)

