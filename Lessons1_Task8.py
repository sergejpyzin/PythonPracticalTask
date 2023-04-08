# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить
# k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

widthChocolate = int(input("Введите кол-во долек  шоколадки 'n' (ширина):\n"))
lengthChocolate = int(input("Введите кол-во долек  шоколадки 'm' (длинна):\n"))
numbersSlicesChocolate = int(input("Введите кол-во долек  шоколадки 'k':\n"))

if numbersSlicesChocolate % 2 == 0 and numbersSlicesChocolate < widthChocolate * lengthChocolate:
    print(f"От шоколадки размером {widthChocolate} х {lengthChocolate} можно отломить {numbersSlicesChocolate} долек одним разломом по прямой")
else:
    print(f"От шоколадки размером {widthChocolate} х {lengthChocolate} нельзя отломить {numbersSlicesChocolate} долек одним разломом по прямой")