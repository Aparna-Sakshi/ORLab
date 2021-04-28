import math
from itertools import combinations

# m number of equations
# arr is the coefficient matrix (list of lists)
# e is the error
# b is the value matrix
# z is the coefficients of objective function
# objective is either to minimize or maximize the objective func


e = 0.001

def objective_func(z, values, vs):
    z_len=len(z)
    vs_len=len(vs)
    val=0
    for i in range(vs_len):
        idx=int(vs[i][1])-1
        if idx<z_len:
            val+=z[idx]*values[i]
    return val
            
        
        
        

def Solutions(arr, b, e, z, objective):
    n = len(arr)  # no. of variables
    m = len(arr[0])  # no of eqn
    variables = ["x" + str(i+1) for i in range(n)]
    c = list(combinations(arr, m))
    v = list(combinations(variables, m))
    
    if objective == "max":
        opt_val=-9999999999
    else:
        opt_val=+9999999999
    
    opt_values=None
    val =-1
    
    
    print("All feasible solutions and value of objective function")
    for A, vs in zip(c, v):
        values,isFeasible=GaussSiedel(A, b, e)
        if isFeasible:
            print(" are the values for ", end=" ")
            print(vs, " with value of objective func =", end=" ")
            val=objective_func(z, values, vs)
            print(val)
            #finding optimal solution
            cond=False
            if objective == "max":
                cond=(opt_val<val)
            else:
                cond=(opt_val>val)            
            if cond:
                opt_val=val
                opt_values =(values,vs)
                
    print("Optimal solution is ", opt_values, " and optimal value is ", opt_val)
        
            
            
            
            
        
        


def GaussSiedel(A, b, e):
    # variables with zero coefficients are removed
    n = len(A)
    x = [0 for i in range(n)]
    x0 = [0 for i in range(n)]
    for k in range(1000):

        key = 0
        for i in range(n):
            val = 0
            for j in range(n):
                if j < i:
                    val = val + A[j][i] * x[j]
                elif j > i:
                    val = val + A[j][i] * x0[j]
            if A[i][i] != 0:
                x[i] = (b[i] - val) / A[i][i]
            # convergence check
            if abs(x[i] - x0[i]) > e:
                key = 1
        for i in range(n):
            x0[i] = x[i]
        if key != 1:
            break
    flag = True
    for num in x:
        if num <= 0 or math.isnan(num):
            flag = False
    
    if flag:
        print(x, end=" ")
        #print("which satisfies non-negativity constraint")
        return (x,True)
    else:
        #print("which doesn't satisfy non-negativity constraint")
        return (x,False)



print("_____________________________________________________")

# Menu program
print("Enter the number of test cases")
t = int(input())
for k in range(t):

    print("Enter 2 spaced integers m and n, where m is number of constraint equations , n is number of variables")
    m, n = map(int, input().split())
    print("enter the coefficients of objective function")
    z = list(map(float, input().split()))
    print("Do you want to minimize or maximize? Type min to minimize and max to maximize")
    objective=input()    
    arr = [[0 for i in range(m)] for j in range(n+m)]
    b = [0 for i in range(m)]
    print("Now you have to enter the inequalities one by one")
    for i in range(m):
        print("Enter the type of constraint a1*x1+a2*x2+...+an*xn >=/<= b. Type >= or <=")
        constraint = input()
        print("Enter the coefficients of equations " + str(i) + ": a1 a2 ... an b" + str(i))
        lstr = input().split()
        l = []
        if constraint == "<=":
            l = list(map(float, lstr))
        else:
            l = list(map(lambda value: -float(value), lstr))
        for j in range(n):
            arr[j][i] = l[j]
        #adding slack variable
        arr[i+n][i] = 1
        b[i] = l[n]

    Solutions(arr, b, e, z, objective)
    print("_____________________________________________________")

