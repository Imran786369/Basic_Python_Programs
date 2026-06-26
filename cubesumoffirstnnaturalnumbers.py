#Using Mathematical Formula
n = 5
res = ((n * (n + 1)) // 2) ** 2
print(res)

#Using Brute Force approach
n=6
res=0
for i in range(1,n+1):
    res+=i**3
print(res)