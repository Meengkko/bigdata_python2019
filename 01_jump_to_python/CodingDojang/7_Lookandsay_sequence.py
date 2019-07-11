def lookandsay(input_string, digit_limit):
    input_string = input_string + ' '
    output = ''
    letter_counter = 1
    for i in range(0, len(input_string) - 1):
        if input_string[i] == input_string[i + 1]:
            letter_counter = letter_counter + 1
        else:
            output += str(letter_counter) + input_string[i]
            letter_counter = 1

    if len(output) > digit_limit:
        return output[:digit_limit + 10]
    return output


j = 0
lim = 100
sequence = '1'
while j < lim:
    sequence = lookandsay(sequence, lim)
    j = j + 1

print(sequence[lim+1])
