friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ['admin', 'guest', 'user']

if 'Max' in friends:
    print ('У меня есть друг')

if 'M' in friend_name:
    print ('Буква М есть в имени друга')

# for - преимущество отдавать этому циклу
# особенно припереборе последовательностей
# и кога нам не надо манипулировать счетчиком индекса и условием индекса 
for friend in friends: # -friend- -переменная цикла- -in- -переменная для перебора-
    print(friend)
print()

for letter in friend_name:
    print (letter)
print()

for role in roles:
    print (role)
print()


# while
i = 0
while i < len(friends):
    friend = friends[i]
    print (friend)
    i += 1 