# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа

summa = int(input("Сумма двух чисел равна: "))
multy = int(input("Произведение двух чисел равна: "))
first_number = 0
second_number = 0
for i in range (summa):
    for j in range (multy):
        if i + j == summa and i * j == multy:
            first_number = i
            second_number = j
            break

print(first_number, second_number)