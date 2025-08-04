num1 = int(input("Введите любое число: "))
num2 = int(input("Введите любое число: "))
if num1 > num2:
    print(num1, "больше", num2)
elif num1 < num2:
    print(num1, "меньше", num2)
elif num1 == num2:
    print(num1, "равно", num2)


#age_control = int(input('Введите возраст: '))
#if age_control <= 5:
#   print("Вход  бесплатный")
#elif age_control <= 15:
#    print("Вход 100 сом")
#elif age_control <= 18:
#    print("Вход 200 сом")
#elif age_control >= 25:
#    print("Вход 500 сом")





week_day = int(input('Введите день недели (1-7): '))
a ={
    1 : "Понедельник",
    2 : "Вторник",
    3 : "Среда",
    4 : "Четверг",
    5 : "Пятница",
    6 : "Суббота",
    7 : "Воскресенье",
      }                  # наборы записываются с помощью фигурных скобок.Наборы используются для хранения нескольких элементов в одной переменной.
if 1 <= week_day <=7 :
    print(a[week_day]) # позиции от 1 до 7.Для доступа к элементам строки можно использовать квадратные скобки





number = int(input('Введите число: '))
if number % 2 == 0:
   print("Четный")
else :
   print("Нечетный")






time = int(input('Введите время суток: '))
if time <=5:
    print('Ночь')
elif time <=11:
    print('Утро')
elif time <= 17:
    print('День')
elif time <= 23:
    print('Вечер') 







x = int(input('Введите месяц (1-12): '))
month = {
    1 : "Январь",
    2 : "Февраль",
    3 : "Март",
    4 : "Апрель",
    5 : "Май",
    6 : "Июнь",
    7 : "Июль",
    8 : "Август",
    9 : "Сентябрь",
    10 : "Октябрь",
    11 : "Ноябрь",
    12 : "Декабрь"
}
print(month[x])






products = {
    "Яблоко" : 140,
    "Груша" : 125,
    "Апельсин" : 160,
    "Огурец" : 70
}
product = input("Введите название продукта: ")
if product in products:
    weight = int(input("Введите вес (кг): "))
    price = products[product] * weight
    print(f"Цена {price} сом")
else :
    print("Такого продукта нет в списке")