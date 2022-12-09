# dict
# Словарь объявляется так: my_dict = {key1: val1, key2: val2, ...}

# Получение элементов по ключу friend['name']
# Добавление значения в словарь friend['has_car'] = True
# Изменение значения friend['has_car'] = False
# Удаление значений в словаре remove friend['age']
# Оператор in 'age' in friend

friends = ['Max', 'Leo', 'Kate']
print (friends)
print()

# Добавляем возраст друга
print('Добавляем возраст друга: ')
friend = {
    'name': 'Max', # name = ключ, Max = значение
    'age': 23
}

print(friend)
print(type(friend))
print()

# __________________________________________________________
# Проверяем возраст:
print('Проверяем возраст:')
print('Age:', friend['age'])
print()

# Добавляем в словарь
print('Добавляем в словарь')
friend['has_car'] = True
print(friend)

# Удаляем переменную
print('Удаляем переменную: ')
del friend['age']
print(friend)
print()

# Опреатор in
print('Опреатор in')
if 'age' in friend:
    print ('Есть возраст!')
print()

if 'has_car' in friend:
    print ('Есть машина!')
print()

# Перебор словаря:
# по ключам
# по значениям
# по парам ключ, значение

# по ключам
print ('По ключам')
for key in friend.keys():  # friend.keys - перебор в списке friend по ключам keys(ключи)
    print(key)
print()

# по значениям
print ('По значениям: ')
for val in friend.values(): # friend.values - перебор в списке friend по значениям value (значение)
    print(val)
print()

# пары ключ значение
print ("Пары ключ значение:")
for item in friend.items(): # метод items - возвращает список из кортежа
    print(item)
print()

for key, val in friend.items():
    print(key)
    print(val)