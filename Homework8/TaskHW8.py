# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения
# и удаления данных.
# Формат сдачи: pull-request.
import csv
import os
from os.path import exists
from csv import DictReader, DictWriter

#Создание файла
def create_file():
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер']) #массив данных. DictWriter - только для csv.
        f_writer.writeheader()

#получение данных от user
def get_info():
    enter = input("Введите Фамилию, Имя, Номер: ")
    mas_info = enter.split()
    return mas_info

#запись данных в файл (OK)
# fieldnames - заголовки
# writeheader - запись заголовков
def write_file(lst):
    with open('phone.csv', 'r', encoding='utf-8', newline='') as data:
        f_reader = DictReader(data) #получение данных из файла(чтение)
        res = list(f_reader) #список словарей
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]} #создаем словарь
        res.append(obj) #в список помещаем словарь в существующий список словарей
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер']) #массив данных.  DictWriter - только для csv.
        f_writer.writeheader() #обходит все элемеенты и дозаписывает
        f_writer.writerows(res)

#чтение данных из файла (OK). Можно навести красоту, чтобы выходил заголовок и ровные столбцы, но лень.
# Как будет время, сделать.
def read_file(file_name):
    with open('phone.csv', encoding='utf-8') as data:
        f_reader = data.read()
        print(f_reader)

# Функция поиска контакта (OK)
def find_contact(file_name):
    os.system("cls")
    enter = input("Введине данные контакта для поиска: ")
    res = []
    with open('phone.csv', "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if enter in person:
                res.append(person)
    if len(res) != 0:
        print(res)
    else:
        print(f"Контакт '{enter}' не найден.")

# Функция изменения контакта(OK)
def changeContact(file_name):  # Функция изменения информации в контакте
    with open('phone.csv', 'r', encoding='utf-8', newline='') as file:
        # Чтение в список словарей
        f_reader = DictReader(file)
        res = list(f_reader)

        index = int(input("Введите порядковый номер контакта, который нужно изменить: "))
        print(res[index])
        key = input("Введите ключ контакта, который нужно удалить: ")
        new_value = input("Введите новое значение: ")
        res[index][key] = new_value

    with open('phone.csv', 'w', encoding='utf-8', newline='') as file:
        f_writer = DictWriter(file, fieldnames=f_reader.fieldnames)  # массив данных.  DictWriter - только для csv.
        f_writer.writeheader()  # обходит все элемеенты и дозаписывает
        f_writer.writerows(res)


# Удаление данных из файла(OK)
def delContact(fileName):
    with open('phone.csv', 'r', encoding='utf-8', newline='') as file:
        # Чтение в список словарей
        f_reader = DictReader(file)
        res = list(f_reader)

        index = int(input("Введите порядковый номер контакта, который нужно удалить: "))
        print(res[index])
        res.pop(index)

    with open('phone.csv', 'w', encoding='utf-8', newline='') as file:
        f_writer = DictWriter(file, fieldnames=f_reader.fieldnames)  # массив данных.  DictWriter - только для csv.
        f_writer.writeheader()  # обходит все элемеенты и дозаписывает
        f_writer.writerows(res)

#Наведение красоты(интерфейс главного меню)
def drawMainMenu():
    print(" [q] -- Выход")
    print(" [r] -- Чтение")
    print(" [w] -- Запись")
    print(" [f] -- Поиск")
    print(" [c] -- Изменение")
    print(" [d] -- Удаление")

#файловый менеджер. Для постоянной работы
def main():
    while True: #бесконечная работа
        drawMainMenu()
        command = input('Введите команду: ')
        if command == 'q':  #команда выхода.
            break
        elif command == 'r': #команда чтения
            if not exists('phone.csv'): #проверка наличия файла
                create_file()
            print(read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
            write_file(get_info())
        elif command == 'f': #поиск
            if not exists('phone.csv'):
                create_file()
            find_contact('phone.csv')
        elif command == 'c': #изменение
            if not exists('phone.csv'):
                create_file()
            changeContact('phone.csv')
        elif command == 'd': #изменение
            if not exists('phone.csv'):
                create_file()
            delContact('phone.csv')


main()
