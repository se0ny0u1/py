#def main(a, b, r, y):
 #   return(max(a, b, r, y))

#print(main(5, 7, 4, 22))

#def num(number):
#    return number %2 == 0

#print(num(8))





def num(number):
    return number > 0 
number = int(input("Введите число:"))

print(num(number))




def num(number):
    return number ** 2 
number = int(input("Введите число:"))
print(num(number))


def t(word):
    return word[0].isupper()
word = input("Введите слово:")
print(t(word))