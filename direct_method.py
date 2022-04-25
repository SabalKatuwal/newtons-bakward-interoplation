#interpolation # backward
import numpy as np
x=[5,10,15,20,25]
y=[46,90,120,170,2901]
m= int (input ("at which point you want the interpolated value:"))
n= len (x) -1
h=5 # the difference between x

p= (m - x[n])/h
coeff=p
k=1
sum=y[n]

for i in range (n, 1,-1) :
    y= np. diff (y)
    sum=sum+coeff*y[i-1]
    coeff=coeff* (p+k) / (k+1)
    k=k+1 
    print (sum)