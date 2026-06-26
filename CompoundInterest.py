# #Using Exponentiation Operator
# P=1200
# R=5.4
# T=2
# A=P*(1+R/100)**T
# CI=A-P
# print("Compound Interest : ", CI)

#Using Built-in pow() Function
# P=10000
# R=10.25
# T=2
# Amt=P*(pow(1+R/100,T))
# CI = Amt-P
# print('Compound Interest : ', CI)

p=int(input("Enter principal amount: "))
r=int(input("Enter rate of interest: "))
t=int(input("Time in years: "))
Amt=p*(pow(1+r/100,t))
CI=Amt-p
print("Compound Interest: ", CI)
