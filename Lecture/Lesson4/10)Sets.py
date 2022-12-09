# МНОЖЕСТВА
# во множестве не может быть 2-ъ одинаковых элементов
# cities = ['Moscow', 'Paris', 'New York']
print()
cities = ['Moscow', 'Paris', 'New York', 'Paris', 'Moscow', 'Moscow']

print(type(cities))
print(cities)
print()

# Чтобы убрать повторения приводим к типу set
print('Убрали повторения')
cities = set(cities)
print (cities)
print()

# ДЕЙСТВИЯ
# добавление элемента cities.add('Burma')
# удаление cities.remove('Moscow')
# длинна множества len
# оператор in цикл for
# работа с несколькими множествами

# Добавление
print('Добавление элемента')
cities.add('Burma')
print (cities)
print()

# Удаление ээлемента
print('Удаление элемента: ')
cities.remove('Burma') 
print(cities)
print('Paris' in cities) # Проверяем есть ли слово в множестве
for city in cities:
    print(city)
print()

# Операции со множествами
# Объединение |
# Пересечение &
# Разность -
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты' }
kate_things = {'Телефон', 'Шорты', 'Зонтик', ' Помада'}

# Какие вещи взяли вместе?
print('Какие вещи взяли вместе:', (max_things | kate_things)) # объединяем
print()

# Какие вещи повторяются?
print('Какие вещи повторяются: ', max_things & kate_things) # пересечение
print()

# Какие вещи взял max, но не взяла kate?
print('Какие вещи взял max, но не взяла kate: ', max_things - kate_things)
print()

# Какие вещи взяла kate, но не взял max?
print('Какие вещи взяла kate, но не взял max: ', kate_things - max_things)