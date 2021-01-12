numbers = [1, 3, 5, 2, 5, 7, 4, 3, 2, 4, 5, 6, 0]
numbers.sort()
print(numbers)

previousnumber = numbers[0]
newlist=[]
newlist.append(numbers[0])

for counter in numbers:
    print (newlist)
    print (previousnumber)
    if previousnumber != numbers[counter]:
        newlist.append(numbers[counter])
    previousnumber = numbers[counter]
numbers = newlist
print(numbers)

