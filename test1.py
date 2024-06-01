alpha='abcdefghigklmnopqrstuvwxyz'
alphaup='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = int(input('Введите число, на которое надо сдвинуть текст:'))

summary = ''
def changeChar(char):
    if char in alpha:
        return alpha[(alpha.index(char) + number) % len(alpha)]
    elif char in alphaup:
        return alphaup[(alphaup.index(char) + number) % len(alphaup)]
    else:
         return char
with open ('Color of the night_engl.txt') as myfile:
    for line in myfile:
        for char in line:
            summary+=changeChar(char)
with open ('Color of the night_engl.txt', 'w') as myfile:
    myfile.write (summary)