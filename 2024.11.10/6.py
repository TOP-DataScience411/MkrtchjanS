def orth_triangle(cathetus1: float = 0, cathetus2: float = 0, hypotenuse: float = 0) -> float:
    args = [cathetus1, cathetus2, hypotenuse]
    if args.count(0) != 1: 
        return None
    if cathetus1 and cathetus2:
        return (cathetus1**2 + cathetus2**2) ** 0.5
    elif cathetus1 and hypotenuse:
        if hypotenuse <= cathetus1:
            return None
        return (hypotenuse**2 - cathetus1**2) ** 0.5
    elif cathetus2 and hypotenuse:
        if hypotenuse <= cathetus2:  
            return None
        return (hypotenuse**2 - cathetus2**2) ** 0.5
    
    return None  

# Примеры
print(orth_triangle(cathetus1=3, hypotenuse=5))  # 4.0
print(orth_triangle(cathetus1=8, cathetus2=15))  # 17.0
print(orth_triangle(cathetus2=9, hypotenuse=3))  # None
