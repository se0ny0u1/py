# Набор пар ключ - значение

dict = {
    'name': 'Akyl',
    'age' : '45',
    'phone number': '0700029222',
    'INN': '216102007009'
}


# keys() - Возвращает все ключи словаря

dict = {
    'name': 'Akyl',
    'age' : 45,
    'phone number': '0700029222',
    'INN': '216102007009'
}
a = dict.keys()
print(a)

my_dict = {'name': 'John', 'age': '25', 'city': 'New York'}
all_keys = my_dict.keys() #'name', 'age', 'city'

#values() - Возвращает все значения словаря

data = {'x': 10, 'y':20, 'z': 30}
all_values = data.values() #[10, 20, 30]

#items() - Возвращает все пары ключ-значение словаря в виде кортежей

my_dict = {'name': 'Alice', 'age': 25, 'city': 'Paris'}
all_items = my_dict.items() #all_items = [('name', 'Alice'),('age',(30))]

#get() - Возвращает значение по ключу;

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x) #'Mustang'


#pop() - Убирает пары ключ-значение

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")

print(x) #x = {'brand': 'Ford', 'year': 1964}

#update() - Добавляет пары ключ-значение

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car) #car = {"brand": "Ford","model": "Mustang","year": 1964,"color":"White"}






num = int(input('Первое число: '))
operator = input('Выберите оператора (+, -, *, /): ')
num2 = int(input('Второе число: '))
if operator == '+':
    result = num + num2
elif operator == '-':
    result = num - num2
elif operator == '/':
    result = num / num2
elif operator == '*':
    result = num * num2
else:
    print("ОШИБКА")
print('Результат: {} {} {} = {}'.format(num, operator, num2, result)) #"My name is {}, I'm {}".format("John",36) (example)
