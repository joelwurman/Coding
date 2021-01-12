numbers = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'

}
phone = (input('Phone: '))

output = ''
for item in phone:
    output += numbers[item] + ' '

print(output)