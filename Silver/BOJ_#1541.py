line = input()
number = 0
integer = ""
add_flag = True
for char in line:
    if char == "-":
        if add_flag:
            number += int(integer)
            add_flag = not add_flag
        else:
            number -= int(integer)
        integer = ""
    elif char == "+":
        if add_flag:
            number += int(integer)
        else:
            number -= int(integer)
        integer = ""
    else:
        integer += char
if add_flag:
    number += int(integer)
else:
    number -= int(integer)
print(number)
