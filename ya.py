# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
s = ["яблоко", "банан", "киви", "арбуз"]
i = 0
for f in s:
    i = i + 1
    print(str(i) + '.', '{:>7}'.format(f))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

s = ["яблоко", "банан", "киви", "арбуз"]
s1 = ["яблоко", "банан", "киви", "арбуз", "груша"]
s2 = s + s1
print(set(s2))
