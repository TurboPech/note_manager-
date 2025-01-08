zagolovok = []
print('Введите заголовок (или оставьте пустым для завершения)')
i = 1
# ввод заголовков
while True :
    stroka = input(f'Заголовок {i} :')
    # Проверка есть ли такой заголовок в списке
    if zagolovok.count(stroka)>0:
        print('такая строка уже есть, добавить? да / нет')
        choise = input(':')
        if choise == 'нет':
            stroka = input(f'Заголовок {i} :')
    # Проверка на ввод пустой строки
    if stroka == '':
        print(zagolovok)
        break
    # Добавление заголовка в список
    zagolovok.append(stroka)
    i += 1
