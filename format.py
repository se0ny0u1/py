name = input('Введите имя: ')
age = input('Введите возраст: ')
a = (f"Привет {name} тебе {age} лет")
print(a)



sum = int(input('Введите сумму: '))
if sum >= 1000:
   z = sum * 0.1
   c = sum - z
   print(f"Сумма покупки со скидкой 10% равна: {c}")
else :
   print(f"Сумма покупки равна:  {sum}")
