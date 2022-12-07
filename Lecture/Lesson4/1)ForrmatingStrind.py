# Форматирование строк
name = "Leo"
age = 30
print()

# 1. конкантенация
hello_str = "Привет, " + name + " тебе " + str(age) + " лет "
print ("1) Конкантенация: ", hello_str) 

# 2. %
hello_st = "Привет %s тебе %d лет"%(name, age) # s = string (поступит строка); d = digit (поступит число)
print ("2) %: ", hello_st)

# 3. format (самый удобный)
hello_s = 'Привет {} тебе {} лет'.format(name, age)
print ("3) format(): ", hello_s)

# 4. Example
top5 = "Первые 5 мест на соревнованиях: 1. Иванов 2. Петров 3. Сидоров 4. Орлов 5. Соколов"
start = top5.find("1")
end = top5.find("4")

top3 = top5[start : end]

result = "Поздравляем {} с успехом!".format(top3.upper())

print (result)
