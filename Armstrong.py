#Using a Mathematical Approach
# n=155
# t=n
# p=len(str(n))
# s=0
# while t>0:
#     d=t%10
#     s+=d**p
#     t//=10
# if s == n:
#     print("Given number is Armstrong number")
# else:
#     print("Given number is not Armstrong number")

#Using String Conversion
# n=153
# p=len(str(n))
# s=sum(int(d)**p for d in str(n))
# if s == n:
#     print("Given number is Armstrong number")
# else:
#     print("Given number is not Armstrong number")
    
#Using map() and lambda
n=153
p=len(str(n))
s=sum(map(lambda d:int(d)**p,str(n)))
if s == n:
    print("Given number is Armstrong number")
else:
    print("Given number is not Armstrong number")
 