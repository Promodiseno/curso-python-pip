def find_volume(length = 1, width = 1, depth = 1):
    return length * width * depth,width
result = find_volume(width=10)
result1 = find_volume(depth=2)
result2 = find_volume(length=4)
result3 = find_volume(2,5,10)
#entrada
print(result)
print(result1)
print(result2)
print(result3)
#salida
result_width, length = find_volume(5,3,8)

print(length)