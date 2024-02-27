start = int(input("Рік початку обліку"))
end = int(input("Рік закінчення обліку "))
bet = dict()
while start <= end:
    tema = input(f"Хочете додати до проектів {start} року (так/ні) ").lower()
    if tema == "так" :
        tema2 = input("Введіть тему")
        dani  = input("Введіть дані про кількість заявок (у рядок через пробіл!!!)").split()
        dani = list(map(int,dani))
        if tema in bet:
            bet[tema2] += 1
        else:
            bet[tema2] = 1
    else:
        start+= 1
key_list = list(bet.keys())
print("РЕЗУЛЬТАТИ АНАЛІЗУ:")
for e in range(len(bet)):
    print(f"{key_list[1]} - {bet[tema2]} - проектів")
    print(f"{key_list[2]} - {bet[tema2]} - проектів")