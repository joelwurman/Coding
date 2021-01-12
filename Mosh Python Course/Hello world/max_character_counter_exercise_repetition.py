sentence = 'This is a common interview question'

max_char_count, max_char, *variables = 0, '', set(sentence)

for char in str(sentence):
    if max_char_count < (sentence.count(char)):
        max_char_count = (sentence.count(char))
        max_char = char
    print(char)
print(max_char, ' = ', max_char_count)

# if sentence.count(sentence, char) > maximum:
#     print(char)
