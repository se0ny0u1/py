#Неупорядоченные коллекции уникальных элементов

mu_set = {1, 2, "apple", 3.14}

#add() - Добавляет элементв множество

my_set = {1, 2, 3}
my_set.add(4) 

#remove() - удаляет элемент из множества

my_set = {1, 2, 3}
my_set.remove(2)

#union() - объединение двух множеств

my_set = {1, 2, 3}
my_set2 = {2, 3, 4}
union_set = my_set.union(my_set2)

#intersectin() - пересечение двух множеств

my_set = {1, 2, 3}
my_set2 = {2, 3, 4}
intersection_set = my_set.intersection(my_set2
                                       )
#discard() - removes the specified item from the set.

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

#pop() - удаляет рандомный элемент

fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

#Получение подкортежа с определенным диапазоном индексов

my_tuple = (10, 20, 30, 40)
seubtuple = my_tuple[1:4]

#Шаг среза для кортежа

items = ('apple', 'orange', 'banana', 'grape')
sliced_item = items[::2]