def taxi_cost(distance: int, wait_time: int = 0) -> int | None:
    if distance < 0 or wait_time < 0:
        return None
    
    base_cost = 80
    
    if distance == 0:
        total_cost = base_cost + 80 + (wait_time * 3)
    else:
        cost_distance = (distance / 150) * 6
        cost_wait = wait_time * 3
        total_cost = base_cost + cost_distance + cost_wait
    
    return round(total_cost)

# Ручное тестирование
print(taxi_cost(1500))  # 140
print(taxi_cost(2560))  # 182
print(taxi_cost(0, 5))  # 175
print(taxi_cost(42130, 8))  # 1789
print(taxi_cost(-300))  # None
