status = ' --- '
print('-'*20)
print(' Заголовок: test ')
print(' Статус :', status )
print('-'*20)
Status = ['Выход ','в процессе ', 'отложенно ' , 'завершенно ' ]

print(' Хотите изменить статус ? выберете из списка')
#Вывод статусов на экран
for i in range (len(Status)):
    print(f' {i}. {Status[i]}')
#Выбор статуса
choise = int(input('Введите статус из списка : '))
if choise == 0:
    print('Выход')
if choise == 1:
    status = Status[1]
if choise == 2:
    status = Status[2]
if choise == 3:
    status = Status[3]
#Вывод измененный статус
print('')
print('Статус успешно обновлен')
print('-'*20)
print('Заголовок: test ')
print('Статус :', status )
print('-'*20)
