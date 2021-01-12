list = [0, 3, 6, 5, 7, 3, 5, 6, 7, 4, 8, 4, 3, 2, 5]
print(list)
maxnumber = list[0]
for counter in list:
    if counter > maxnumber:
        maxnumber = counter;
        print (maxnumber)