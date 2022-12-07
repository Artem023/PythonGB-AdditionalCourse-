# Список, который нельзя изменять
# Записывается в круглых скобках
# roles = ('user', 'manager', 'admin')
# служит для защиты от изменений

print ('СОРЕВНОВАНИЯ ПО PYTHON')
count = int (input ('Введите количество участников: '))
i = count
members = []

while i > 0:
    name = input ('Кто занял {} место?: '.format(i))
    members.append(name)
    i-=1

# кто учавствовал в соревновании (по алфавиту sorted())
print ('В соревновании учавствовали: ', sorted(members))

# переворот списка с помощью MEMBERS.reverse()
members.reverse()

# нам нужно взять первые 3 места
result  = members[:3]

result = 'Победители: {}. Поздравляем!'.format(result)
print(result)