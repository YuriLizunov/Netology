#!/usr/bin/env python
# coding: utf-8

# ### Задание 1

# In[3]:


Phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
Phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
print('Результат:')
if Phrase_1 > Phrase_2:
    print('Фраза 1 длинее фразы 2')
elif Phrase_1 < Phrase_2:
    print('Фраза 2 длинее фразы 1')
elif Phrase_1 == Phrase_2:
    print('Фразы равной длины')


# ### Задание 2

# In[4]:


y = int(input('Введите год: '))
if y % 4 != 0:
    print('Результат: Обычный год')
elif y % 100 == 0:
    if y % 400 == 0:
        print('Результат: Високосный год')
    else:
        print('Результат: Обычный год')
else:
    print('Результат: Високосный год')


# ### Задание 3

# In[5]:


date = int(input('Введите ваш день рождения:'))
month = int(input('Введите месяц вашего рождения:'))
year = int(input('Введите год вашего рождения:'))
                 
if (date >= 21 and date <= 31 and month == 3) or (month == 4 and date >= 1 and date <= 19):
                 print('Ваш знак зодиака: Овен')
elif (date >= 20 and date <= 30 and month == 4) or (month == 5 and date >= 1 and date <= 20):
                 print('Ваш знак зодиака: Телец')
elif (date >= 21 and date <= 31 and month==5) or (month == 6 and date >= 1 and date <= 21):
                 print('Ваш знак зодиака: Близнецы')
elif (date >= 22 and date<=30 and month == 6) or (month == 7 and date >= 1 and date <= 22):
                 print('Ваш знак зодиака: Рак')
elif (date >= 23 and date <= 31 and month == 7) or (month == 8 and date >= 1 and date <= 22):
                 print('Ваш знак зодиака: Лев')
elif (date >= 23 and date <= 31 and month == 8) or (month == 9 and date >= 1 and date <= 22):
                 print('Ваш знак зодиака: Дева')
elif (date >= 23 and date <= 30 and month == 9) or (month == 10 and date >= 1 and date <= 23):
                 print('Ваш знак зодиака: Весы')
elif (date >= 24 and date <= 31 and month==10) or (month == 11 and date >= 1 and date <= 22):
                 print('Ваш знак зодиака: Скорпион')
elif (date >= 23 and date <= 30 and month==11) or (month == 12 and date>=1 and date <= 21):
                 print('Ваш знак зодиака: Стрелец')
elif (date >= 22 and date <= 31 and month == 12) or (month==1 and date >= 1 and date <= 20):
                 print('Ваш знак зодиака: Козерог')
elif (date >= 21 and date <= 31 and month == 1) or (month == 2 and date >= 1 and date <= 18):
                 print('Ваш знак зодиака: Водолей')
elif (date >= 19 and date <= 29 and month == 2) or (month == 3 and date >= 1 and date <= 20):
                 print('Ваш знак зодиака: Рыбы')


# ### Задание 4

# In[10]:


width = int(input('Ведите ширину: '))
length = int(input('Ведите длину: '))
height = int(input('Ведите высоту: '))
if width < 15 and length < 15 and height < 15:
    print('Вам нужна коробка №1')  
elif (width > 15 and width < 50) or (height > 15 and height < 50) or (length > 15 and length < 50):
    print('Вам нужна коробка №2')
elif (length > 200):
    print('Вам нужна упаковка для лыж')
else:
    print('Вам нужна стандартная коробка №3')

