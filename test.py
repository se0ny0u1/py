users = []
username = input("Введите имя пользователя: ")
password = int(input("Введите пароль: "))
confirm_password = int(input("Подтверддите пароль: "))
if password != confirm_password :
    print("Ошибка, пароли не совпали")
else :
    print(f"Пользователь {username} успешно зарегистрирован")
    users.append([username,password])
