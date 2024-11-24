def numbers_strip(numbers: list[float], n: int = 1, *, copy: bool = False) -> list[float]:
    if n < 0 or n > len(numbers) // 2:
        raise ValueError("Параметр n должно быть неотрицательным и быть меньше или равен половине списка.")

    if len(numbers) <= 2 * n:
        return []
    
    for i in range (n):
        numbers.remove(min(numbers))
        numbers.remove(max(numbers))
    
    return numbers

# Пример 1
sample = [1, 2, 3, 4]
sample_stripped = numbers_strip(sample)
print(sample_stripped)  # [2, 3]
print(sample is sample_stripped)  # True

# Пример 2
sample = [10, 20, 30, 40, 50]
sample_stripped = numbers_strip(sample, 2, copy=True)
print(sample_stripped)  # [30]
print(sample is sample_stripped)  # False
