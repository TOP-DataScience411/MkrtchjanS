def central_tendency(*numbers):
    """Функция вычисляет центральные тенденции (моду, медиану, среднее арифметическое, среднее геометрическое и среднее гармоническое) для переданных чисел."""
    res = dict()
    nums = [num for i in numbers for num in i]  
    nums.sort()

    n = len(nums)
    if n % 2 == 1:
        res['median'] = nums[n // 2]
    else:
        res['median'] = (nums[n // 2 - 1] + nums[n // 2]) / 2

    res['arithmetic'] = sum(nums) / n

    product = 1
    for el in nums:
        product *= el
    res['geometric'] = product ** (1/n)

    reciprocal_sum = sum(1 / el for el in nums)
    res['harmonic'] = n / reciprocal_sum

    return res

print(central_tendency([1, 2, 3, 4, 5]))
# {'median': 3, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
