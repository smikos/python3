#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями)
""""
n1 = int(input("Количество 1:"))
n2 = int(input("Количество 2:"))
b1=(input("число 1: "))
a1 = {b1,}
for i in range(n1-1):
    x=(input("число 1: "))
    a1 = a1.union(x)
print(a1)

b2=(input("число 2: "))
a2 = {b2,}
for i in range(n2-1):
    x=(input("число 2: "))
    a2 = a2.union(x)
print(a2)

i = a1.intersection(a2)
print(i)
"""
#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
a = int(input("Количество кустов:"))
b = [int(i) for i in input("Кол-во ягод(через пробел): ").split()[:a]]
print(max([b[i]+b[i-1]+b[i-2] for i in range(a)]))