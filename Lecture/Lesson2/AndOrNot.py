#  // - целая часть от деления
#  % - остаток от деления
#  ** - возведение в степень

print ("123 // 10 = ", 123 // 10)
print ("123 % 10 = ", 123 % 10) 

# and - и (ИСТИНА когда все ИСТИНА иначе ЛОЖЬ)
# or - или (ЛОЖЬ когда все ЛОЖЬ иначе ИСТИНА)
# not - не (ИСТИНА когда ЛОЖЬ, ЛОЖЬ когда ИСТИНА)

print()

ale = 71
age = int (input ("how old are you?: "))

print ("У вас юбилей: ", age % 5 == 0)

# not and or
print ("У НЕ юбилей: ", age % 5 != 0) # Используем либо not либо !=
print ("У НЕ юбилей: ", not age % 5 == 0)
print()

# and
print ("У вас юбилей и ваш средний возраст меньше ср прод жизни: ", age % 5 == 0 and age < ale)

# or
print ("У вас юбилей или ваш средний возраст меньше ср прод жизни: ", age % 5 == 0 or age < ale)

# приоритет в логических выражениях 
print ((1 > 2 and (0 < 5 or 0 < 2)) and 0 == 0)
