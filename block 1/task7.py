# todo: 7.1 Дано целое число A. Проверка достоверности высказывания: «Число A является четным».
# todo: 7.2 Дано целое число A. Проверка достоверности высказывания: «Число A является нечетным».
# Примечание: В задании требуется привести логическое значение True, если выражение
# для введенных исходных данных является истинным, и значение False в данном случае.

a=float(input())
if a % 2 == 0:
    print('Число A является четным')
else:
    print('Число А является нечетным')