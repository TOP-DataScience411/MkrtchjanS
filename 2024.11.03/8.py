n = int(input())

def fib_line(n):
    if n<=0:
        return []
    elif n==1:
        return [1]
    
    fib = [1,1]

    for i in range(2,n):
        next = fib[-1]+fib[-2]
        fib.append(next)
    return fib

print(' '.join(map(str, fib_line(n))))

#17
#1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597