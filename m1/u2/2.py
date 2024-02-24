a  = input("Введіть дані ").split()
a = list(map(int,a))
mauns = "січень лютий березень квітень травень червень липень серпень вересень жовтень листопад грудень".split()
max = []
min = []
for i in range(1, 12):
    if a[i] > a[i-1]:
        max.append(mauns[i])
    elif a[i] < a[i-1]:
        min.append(mauns[i])
print(max)
print(min)