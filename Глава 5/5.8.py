# 5.8 Hello Admin: создайте список из пяти и более имен пользователей, включающий имя 'admin'.
# Представьте, что вы пишете код, который выводит приветственное сообщение для каждого пользователя после его входа на сайт. Переберите элементы списка и выведите сообщение для каждого пользователя:
admins = ['Саша', 'Санчоус', 'Кирюха', 'Руслан', 'Максон']
name = 'Павлик'
if name in admins:
    print(f"Привет, полковник! {name}, хочешь посмотреть репорт о состоянии?")
else:
    print(f"Привет, {name}! Спасибо, что вновь пользуешься нашим сервисом!")
