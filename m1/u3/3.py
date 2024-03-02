def func(*args):
    indeks = 0
    for i in args:
        indeks = indeks + 1
        print(f"Число {i} це {indeks} аргумент")
print("Результат:")
func(5, 600, 12)


print("Результат:")
func(83,761,71,75,82,91)