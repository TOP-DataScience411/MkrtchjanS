def product (nums)-> float:
    if not nums:
        return 1.0
    return float(nums[0]) * abs(product(nums[1:]))
    
print(product(range(10, 60, 10))) #12000000.0
print(product((0.12, 0.05, -0.09, 0.0, 0.21))) #0.0
