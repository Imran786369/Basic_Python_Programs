# def kdkr(a,b,c,d=523101):
#     print('Name  :',a)
#     print('Address  :',b)
#     print('Phone  :',c)
#     print("Pin number  :",d)

# kdkr("John","Hyd",10)

# # def SimpleInterest(p,t,r):
# #     si=(p*t*r)/100
# #     return si,p,t,r
# # simpInt,x,y,z=SimpleInterest(1000,2,4)
# # print('Simple Interest  :', simpInt)
# # print('My P value is ', x)
# # print('My T value is ', y)
# # print('My R value is ', z)

# # def SimpleInterest(p,t,r=4):
# #     si=(p*t*r)/100
# #     return si,p,t,r
# # simpInt=SimpleInterest(10000,t=2)
# # print('Simple Interest  :', simpInt)
# # print('My P value is ', x)
# # print('My T value is ', y)
# # print('My R value is ', z)

# # def SumOfThreeNums(x,y,z=10):
# #     res=x+y+z
# #     return res
# # sum=SumOfThreeNums(10,z=20,y=7)
# # print(sum)

# def kdkr(a):
#     for i in a:
#         print(i)
# a=[20,30,40,'mango']
# kdkr(a)

# #Using dictionary
# def kdkr(a):
#     print('My name is : ',a['name'])
#     print('My age is : ', a['age'])
#     print('My location is : ', a['location'])
# My_input = { 
#         'name' : 'Imran',
#          'age' : 24,
#         'location' : 'Delhi'}
# kdkr(My_input)

# def My_program(a):
#     b=a**2
#     c=a**3
#     d=a**4
#     return [b,c,d]
# x=My_program(2)
# print(x[0])
# print(x[1])
# print(x[2])

#Arbitary arguments
# def My_prog(*a):
#     b=a[0]+a[2]
#     c=a[3]+a[1]
#     d=a[0]+a[-1]
#     return [b,c,d]
# x=My_prog(20,30,40,60)
# print(x[0])
# print(x[1])
# print(x[2])

#Keyword Arbitary arguments
# def My_prog(**a):
#     b=a['w']+a['x']
#     c=a['m']+a['n']
#     d=a['o']+a['p']
#     return [b,c,d]
# x=My_prog(w=100,x=50,m=150,n=250,o='fruit',p='Banana')
# print(x[0])
# print(x[1])
# print(x[2])

# def My_add(x,y):
#     res=x+y
#     return res
# res=My_add(10,20)
# print(res)

res=lambda x,y:x+y
print(res(5,10))

    