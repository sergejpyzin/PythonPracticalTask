# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = int(input("Введите трехзначное число:\n"))

firstNumber = number // 100
secondNumber = (number // 10) % 10
thirdNumber = number % 10

print(firstNumber + secondNumber + thirdNumber, end=" ")
print(f"({firstNumber} + {secondNumber} + {thirdNumber})", sep="+")
