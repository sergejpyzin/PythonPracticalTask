# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*#
# 385916 -> yes
# 123456 -> no

ticketNumber = input("Введите шестизначый номер билета:\n")

sumFirstThreeNumber = int(ticketNumber[0]) + int(ticketNumber[1]) + int(ticketNumber[2])
sumLastThreeNumber = int(ticketNumber[3]) + int(ticketNumber[4]) + int(ticketNumber[5])

if sumLastThreeNumber == sumFirstThreeNumber:
    print("YES! Билет с номером", ticketNumber, "счастливый!")
else:
    print("NO! Билет с номером", ticketNumber, "несчастливый!")
