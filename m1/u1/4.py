balans = int(input("Введіть поточний баланс карти?"))
buy = input("Хочете зробити покупку(так/ні)?").lower()
while buy == 'так':
    price = int(input("Введіть ціну"))
    balans -= price
    print(f"Сума{price}грн списана з рахунку.")
    buy = input("Хочете зробити покупку(так/ні)?").lower()
else:
    print(f"Доступна сума:{balans}грн")