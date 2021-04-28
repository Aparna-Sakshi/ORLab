import math
from itertools import combinations
#m number of equations
#arr is the coefficient matrix (list of lists)
#e is the error
#b is the value matrix

# 4x+y+2z=2
# 3x-y+5z=0.5
arr=[[4,3],[1,-1],[2,5]]
b=[2,0.5]
m=2
e=0.001
def Solutions(arr, b,e): 
    n=len(arr)#no. of variables
    m=len(arr[0])#no of eqn
    variables=["x"+str(i) for i in range(n)]  
    c=  list(combinations(arr, m))
    v=  list(combinations(variables, m))
    for A,vs in zip(c,v):        
        print("basic variables and their values are", end=" ")
        print(vs, end=" ")
        GaussSiedel(A, b, e)
        




def GaussSiedel(A,b,e):
    #variables with zero coefficients are removed    
    n=len(A)
    x=[0 for i in range(n)]
    x0=[0 for i in range(n)]
    for k in range(1000): 
               
        key=0
        for i in range(n):
            val=0
            for j in range(n):
                if j<i:
                    val=val+A[j][i]*x[j]
                elif j>i:
                    val=val+A[j][i]*x0[j]
            if A[i][i]!=0:
                x[i]=(b[i]-val)/A[i][i]
            #convergence check
            if abs(x[i]-x0[i])>e:
                key=1
        for i in range(n):    
            x0[i]=x[i]
        if key!=1:
            break
    flag=True
    for num in x:
        if num<0:
            flag=False            
    print(x, end=" ")
    if flag:
        print("which satisfies non-negativity constraint")
    else:
        print("which doesn't satisfy non-negativity constraint")
    

Solutions(arr, b, e)
#[0.357,0.572,0],[0.643,0,-0.286],[0,1.286,0.3571]
print("_____________________________________________________")

#Menu program
print("Enter the number of test cases")
t=int(input())
for k in range(t):
    print("Enter 2 spaced integers m and n, where m is number of equations, n is number of variables")
    m,n = map(int, input().split())
    arr=[[0 for i in range(m)] for j in range(n)]    
    b=[0 for i in range(m)]
    for i in range(m):
        print("Enter the coefficients of equations " +str(i)+": a1 a2 ... an b"+str(i))
        l=list(map(float, input().split()))
        for j in range(n):            
            arr[j][i]=l[j]
        b[i]=l[n]
    
        
    Solutions(arr, b, e)
    print("_____________________________________________________")
            
        
    
    


        
            
