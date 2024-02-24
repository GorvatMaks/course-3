start = int(input("Рік початку співпраці з фондом "))
end = int(input("Рік закінчення співпраці з фондом "))
while start <= end:
    if start%2 == 0 :
        print(f"{start} рік - серія")
    else:
        print(f"{start} рік - міжнародний")
    start+= 1

