# def my_kdkr(a,b,c,d):
#     print("Hello Kandukur :",d)
#     print('Sum of two arguments :' ,a+b)
#     e=a+c
#     print(e)
#     f=b+c
#     return f,e
# ongole,vijag=my_kdkr(1,2,78,'kdkr')
# print(ongole,vijag)
def simple_interest(p,t,r):
    if p<100000 and p>=10000:
        if t<24 and t>=6:
            if r<5 and r>2:
                si=(p*t*r)/100
                return si
            else:
                print("Please enter valid Rate of interest ")
        else:
                print("Please enter valid term ")
    else:
        print("Please enter valid principal amount")
          
    # print(si)
simpleInterst = simple_interest(50000,6,4)
# print(kdkr)
# print(simpleInterst)
print("Simple Interest is : ", simpleInterst)