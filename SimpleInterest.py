def fun(p,t,r):
    return (p*t*r)/100
p,t,r=10000,5,10
res=fun(p,t,r)
print(res)

#Using Lambda function
si = lambda p,t,r: (p*t*r)/100
p,t,r = 1000,5,10
res=si(1000,5,5)
print(res)