
numbers = []
for element in range(1,11):
    numbers.append(element*2)

print(numbers)

numbers2 = [elemento * 2 for elemento in range(1,11)]
print(numbers2)

numbers3 = [elemento * 3 for elemento in range(1,11) if elemento % 2 == 0]
print(numbers3)

