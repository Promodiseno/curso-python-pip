def sum_range(min, max):
    sum = 0
    for x in range(min, max):
        sum += x
    return sum

result =  sum_range(5,8)
print(result +10)
