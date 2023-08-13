print("specify mull,n,x,s(values)")
print("if you want to give multiple values of (x) just give space between each number")
print("if x value is one you could type direct and you have to mebction s value too")
import math
import statistics
mu_null = float(input('mu_null=' ))
n = int(input('n=' ))
table = 1.96
j = 500
x = input('x=' )
myarr = x.split(" ")
print(x)
for i in range(len(myarr)):
 myarr[i] = float(myarr[i])
print(myarr)
x_bar = sum(myarr)/len(myarr)
print('x_bar =' ,x_bar)
j = 501
if len(x) < 5:
 s = float(input('s='))
else:
 s = statistics.stdev(myarr)
print('s=' ,s) 
if len(x)<j:
 z3 = ((x_bar - mu_null) / ( s / math.sqrt(n)))
 print(z3,'z claculated value')
elif len(x)>j:
 z4 = ((x_bar - mu_null) / (s / math.sqrt(n)))
 print(z4, 'z claculated value')
if z3 < table:
 print('accept null hypothsis')
else:
 print('reject null hypothsis')
