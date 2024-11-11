def prime_n(num):
    if num < 2:
        return False 
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  
    return True  
    
def count_n(n):
    if n < 1:
        return 0  
    
    down_line = 10 ** (n - 1)
    up_line = 10 ** n - 1    
    count = 0

    for num in range(down_line, up_line + 1):
        if prime_n(num):
            count += 1
            
    return count

n = int(input())

print(count_n(n))

#3
#143