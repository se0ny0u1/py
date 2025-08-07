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