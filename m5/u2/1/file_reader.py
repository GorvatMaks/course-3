#with open("m5/u2/1/my_file.txt") as file:
 #      string_list = string.split(" ")
  #      print(string_list)
   #     for sumvol in string_list:
    #        print(int(sumvol))
     #   break

#with open("m5/u2/1/my_file.txt") as file:
 #   radok = file.readlines()
 #   print(radok[1].split(" ")[4])
#sum = 0
#with open("m5/u2/1/my_file.txt") as file:
#    for odnuch in file:
 #       odnuch_spl = odnuch.split(" ")
  #      for sumvol in  odnuch_spl:
 #           if int(sumvol) == 1:
 #               sum = sum + 1
 #   print(sum)

#with open("m5/u2/1/my_file.txt") as file:
 #   radok = file.readlines()
 #   print(radok[13].split(" ")[7])
summa = 0
with open("m5/u2/1/my_file.txt") as file:
    for odnuch in file:
        odnuch_spl = odnuch.split(" ")
        for sumvol in  odnuch_spl:
            summa = summa + int(sumvol)
    print(summa)    