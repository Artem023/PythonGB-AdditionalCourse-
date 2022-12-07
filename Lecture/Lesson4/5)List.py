# some_list = ['hello, 123. True]
print()
# Можно объявить пустой список
empty_list = []

# Можно объявить список и заполнить его элементами
friends = ['Max', 'Leo', 'Kate']

# тип списка - list
print ("1) Type: ", type(friends))
print()

# есть индексы
print ('2) Первый друг - ', friends[1])
print()

# можно применить срезы
print ("3) Срезы: ", friends[0 : 2])
print (friends[2 : ])
print (friends[ : -2])
print()

# len(friends) - длинна списка
print ("4) Длинна списка:", len(friends))
print()

# friends.append('Ron') - добавление нового элемента
print ("5) Добавление нового элемента: ", friends.append('Ron'))
print (friends)
print ("Длинна списка:", len(friends))
print()

# friends.pop() - удаляем элемент и возвращаем его
friends.pop()
print ("6) Удаление последнего элемента: ", friends)
print ("Длинна списка:", len(friends))
print()

# friends.clear - очищает весь список
friends.clear()
print("7) Удаление списка: ",friends)

friends = ['Max', 'Leo', 'Kate']

# friends.remove ('Ron') - удаление объекта из списка
friends.remove('Kate')
print ("Удаление конкретного элемента: ", friends)
print()

# del friends[i] - удаляет элемент по индексу
del friends[0]
print ("Удаление конкретного элемента по индексу: ", friends)
