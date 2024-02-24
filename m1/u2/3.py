lesson = input("Хочете відвідати урок?(так/ні)").lower()
lit = dict()

while lesson == "так":
    tema = input("Введіть тему")
    if tema in lit:
        lit[tema] += 1
    else:
        lit[tema] = 1
    lesson = input("Хочете відвідати урок?(так/ні)").lower()
emaun_les = sum(lit.values())
emaun_tem = len(lit)
print(f"Загальна кількість уроків: {emaun_les}")
print(f"Розглянуто тем: {emaun_tem}")