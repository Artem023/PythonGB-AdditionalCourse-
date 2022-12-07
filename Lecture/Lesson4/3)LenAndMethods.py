# len(friend) - длинна строки
# friend.find('a') - ищем символ 'а' в строке
# friend.split() - разбиаение строки через пробелы
# friend.isdigit() - проверяет состоит ли строка только из чисел
# friend.upper() - приведение строки к верхнему регистру
# friend.lower() - приведение строки к нижнему регистру

friends = "Максим Леонид"
print (friends)

# len(friend)
print ("len():", len(friends))

# friend.find('a')
print ("friends.find('a'):", friends.find('Лео')) # ищем подстроку в строке

# friend.split()
print ("friends.split(): ", friends.split()) # если между словами есть разделители, например friends = "Максим;Леонид", то
                                             # пишем friends.split(;)
# friend.isdigit()
number = "123"
print ("friends.isdigit():", friends.isdigit()) # метод возвращает True или False
print ("number.isdigit():", number.isdigit())

