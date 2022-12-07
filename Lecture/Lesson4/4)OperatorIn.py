# Позволяет проверить наличие элемента в списке
# 'Max' in friends 
# результат True или False
# Работает и со строками: 'S' in 'Supermen'
print()

hero = 'Superman'
if hero.find('man') != -1: # если искомого элемента нет, то возврат -1
    print ('Есть')
if 'man' in hero:
    print ('Есть!')

goals = ['стать гуру языка python', 'здоровье', 'накормить кота']

if 'здоровье' in goals:
    print ('Все хорошо!')