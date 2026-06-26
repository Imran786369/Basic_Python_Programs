# import math
# n=6
# print(math.factorial(n))

# import numpy as np
# n=6
# if n>=0:
#     print(np.prod(range(1,n+1)))
# else:
#     print('factorial is not defined for negative number')
    
#Using for loop
n=6
if n<1 :
    print('Factorial is not defined for negative number')
else:
    f=1
    for i in range(1, n+1):
        f*=i
    print(f)
        