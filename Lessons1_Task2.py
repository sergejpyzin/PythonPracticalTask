# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# Решение задачи без использования свойств строк

number = int(input("Введите трехзначное число:\n"))

firstNumber = number // 100
secondNumber = (number // 10) % 10
thirdNumber = number % 10

print(firstNumber + secondNumber + thirdNumber, end=" ")
print(f"({firstNumber} + {secondNumber} + {thirdNumber})")



# Решение задачи c использованием свойств строк

number = input("Введите трехзначное число:\n")

sumDigitalNumbers = int(number[0]) + int(number[1]) + int(number[2])

print(sumDigitalNumbers, end=" ")
print(f"({number[0]} + {number[1]} + {number[2]})")
