# break - позволяет выйти из цикла (не важно выполнилось условие или нет)

name = None

# while name != "Гвидо":
while True:
    name = input ("Кто создатель python?: ")
    if name == "Гвидо":
        break
    print ("Неверно")

print ("Верно") 

# continue - позволяет переходить на следующую итерацию цикла 
# (команды в цикле после continue не выполняются)

number = 0
n = int (input ("Введите n: "))

while number <= n:
    if number % 2 == 0:
        number += 1
        continue # с помощью него мы пропускаем четные числа(если число чет. то переходи в while)
    print (number) 
    number += 1

# В блоке else (после while) мы выполняем действия после того, как 
# вышли из цикла while когда условие цикла стало неверным (False)

while number <= 100:
    print (number)
    number += 1
    if number == 33:
        break       # Перейдет на "end" т.к. выходим не по условию
else:               # Выполнится тогда, когда мы выйдем из цикла
    print ('else - end')

print ("end")