def find_minimum(numbers):
    if not len(numbers):
        return None
    min_num = float('inf')
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

numbers = [8, 5, 9, 3, 10]
result = find_minimum(numbers)
print("Минимальное число:", result)