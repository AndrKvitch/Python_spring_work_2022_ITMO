#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу

mass = [1, 8, 25, 64, 8, 10, 99, 89, 77, 10]
count = 0
out = []
for i in mass:
    i = mass[count] + 1
    count += 1
    out.append(i)
print(out)



