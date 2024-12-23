username=input('Имя пользователя:')#имя пользователя
title=input('Заголовок:')#заголовок заметки
content=input('Описание:')#описание заметки
status=input('Статус:')#статус заметки
created_date=input('Дата создания:') #дата создания заметки в формате "день-месяц-год", например "10-11-2024"
issue_date=input('Дедлайн:') #дата истечения заметки например "10-12-2024"
zagolovok2=input('Дополнительный заголовок 1 :')
zagolovok3=input('Дополнительный заголовок 2 :')

note = [username,content,status,created_date,issue_date,
       [title, zagolovok2, zagolovok3]
]
print(note)
