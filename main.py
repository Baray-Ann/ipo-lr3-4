import math #Подключение библиотеки math
x=int(input("Введите значение переменной x: ")) #Введение с клавиатуры переменной x
#Оператор if-else для выполнения различных действий в зависимости от условия
if x<0: #Оператор if с условием что переменная х меньше нуля
    f=x**2 #Функция f(x) равная переменной x в квадрате
else: #Оператор else если переменная х больше или равна нулю
    f=math.sqrt(x) #Функция f(x) равная корню из переменной x
print("Ответ ", f) #Вывод на консоль значения функции f(x)