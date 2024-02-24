balans = int(input("Введіть поточний баланс карти? - "))
buy = input("Хочете зробити покупку(так/ні)? - ").lower()
while buy == 'так' and balans != 0:
    price = int(input("Введіть ціну - "))
    if balans < price:
        print("Недоступно")
    else:
        balans -= price
        print(f"Сума {price}грн списана з рахунку.")
    buy = input("Хочете зробити покупку(так/ні)?").lower()
else:
    print(f"Доступна сума:{balans}грн")