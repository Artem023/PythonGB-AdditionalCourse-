# for - перебор последовательности. Индекс не нужен
# for range - перебор последовательности. Индек нужен
# for range - необходимо пропустить некоторые элементы или идти с конца в начало
# while - цикл связан с условием, но не с последовательностью

# Параметры range:
# range(start_or_stop, stop[,step])
# start_or_stop - начало или конец последовательности
# stop - конец
# step - шаг

# __________________________________________________________________________
# когда нам пригодится range
winners = ['Max', 'Leo', 'Kate']
print()

# простой перебор 
print("Простой перебор:")
for winner in winners:
    print (winner)
print()

# for i in range()
print ("for i in range():")
for i in range(len(winners)): # i - перебор индексов, range(конечная позиция)    
    # print("For: ", i)
    print(i + 1, ')', winners[i])
print()

for i in range(1, len(winners) + 1): # i - перебор индексов, range(конечная позиция)    
    # print("For: ", i)
    print(i + 1, ')', winners[i - 1])
print()


# __________________________________________________________________________
# вывести нечетные числа от 1 до 5
print ("вывести нечетные числа от 1 до 5:")
numbers = [1, 3, 5]
for number in numbers:
    print(number) 

# Решение с параметром
print ("Решение с параметром:")
print (list(range(1, 10, 2)))
print()

for number in range(1, 10, 2):
    print(number)
print()

# __________________________________________________________________________
numbers = range(10) # можно создать последовательность с помощью range
print (numbers)
print (type(numbers))

print (list(numbers))

