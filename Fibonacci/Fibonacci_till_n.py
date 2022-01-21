# Fibonacci
# 1 1 2 3 5 8 13 21 34 ...n 

def fibList(n):
    if n <= 0:
        print('Invalid Input')
    elif n == 1:
        fib = [1]
    elif n == 2:
        fib = [1,1]
    else:
        fib = [1,1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
    return fib
n = 3
print(*fibList(n))

# recursive
# 1 1 2 3 5 8...
def fibRec(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibRec(n-1) + fibRec(n-2)
 
# Driver Program
# print(fibRec(n))