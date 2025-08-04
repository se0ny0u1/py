# upper(): Преобразует все символы строик в верхний регистр.

text = "Привет, мир!"
upper_text= text.upper() # upper_text = "ПРИВЕТ, МИР!"
print(upper_text)

# lower(): Преобразует все символы строки в нижний регистр.

message = "Python"
lower_message = message. lower() # lower_message = "python"

# count(): Возвращает количество вхождений подстроки в строке.

sentence = "Python - прекрасный язык программирвания, Python"
count_python = sentence.count("Python") #count_python = 2

# replace(): Заменяет все вхождения одной подстроки на другую.

phrase = "Я люблю Python"
updated_phrase = phrase.replace("Python", "программирование") 

text = "Python Programming"
substring = text[0:20]
print(substring)






# expandtabs() = Задает размер табуляции строки. Метод expandtabs()устанавливает размер табуляции равным указанному количеству пробелов.

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x) # x = H e l l o


# title() = Преобразует первый символ каждого слова в верхний регистр.

txt = "Welcome to my world"
x = txt.title()
print(x) # x = Welcome To My World

# swapcase() = Меняет регистры местами, строчные буквы становятся прописными и наоборот.

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x) #x = hELLO mY nAME iS peter

# rindex() = Выполняет поиск в строке указанного значения и возвращает последнюю позицию, в которой оно было найдено.

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x) # x = 12

# find() = Выполняет поиск в строке указанного значения и возвращает позицию, в которой оно было найдено.

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) # x = 7

txt = "Hello, welcome to my world." #Где в тексте впервые встречается буква «e», если поиск выполняется только между позициями 5 и 10?:
x = txt.find("e", 5, 10)
print(x) # x = 8