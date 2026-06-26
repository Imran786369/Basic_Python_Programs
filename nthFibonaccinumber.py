# def fibonacci(n):
#     if n<=1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(9))

#Dynamic Programming (Space Optimized)
def fibonacci(n):
    if n<0:
        return "Incorrect Input"
    a,b =0,1
    for _ in range(n):
        a,b = b, a+b
    return a
print(fibonacci(9))

