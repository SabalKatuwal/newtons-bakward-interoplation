import numpy as np

n = int(input("Enter the no of values:"))

x = np.zeros(n)
y = np.zeros((n,n))

#input x and y
for i in range(n):
    x[i] = float(input("enter value for x["+ str(i) +"] :"))
    y[i][0] = float(input( 'enter value for y['+str(i)+'] :'))

#for calculating difference
for j in range(1,n):    
    for i in range(n-1,j-2,-1):     
        y[i][j] = y[i][j-1]-y[i-1][j-1] 

# j runs from 1 to 4
# when j=1: 
#   i runs from 4 to 0
#       when i = 4
#       y[4][1] = y[4][0]- y[3][0]


#for printing difference table
for i in range(0,n):
    print('%0.4f' %(x[i]), end='    ')
    for j in range(0, i+1):
        print('\t%0.4f' %(y[i][j]), end='   ')
    print()

# i runs from 0 to 4
#   x[i] will be printed
#   when i = 0;
#       j runs from 0 to 0
#       y[0][0] will be printed
#   when i = 1;
#       j runs from o to 1
#       y[1][0] y[1][1] will be printed

# finding p
A = float(input("enter the value to interpolate :"))

p = float((A - x[n-1])/(x[n-1]-x[n-2]))

inter = y[n-1,0]


for i in range(1,n-1):
    if i == 1:
        p = (p+i-1)
    else:
        p = p*(p+i-1)
    
    inter = inter + (p * y[n-1,i] )/np.math.factorial(i)

print(f"The result of newtons backward intepolation at {A} is "+'%0.4f' %inter);
