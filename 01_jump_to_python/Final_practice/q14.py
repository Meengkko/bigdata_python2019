input_string = input("공백 없이 문자열 입력") + ' '
result = ''
letter_counter = 1

for i in range(0, len(input_string) - 1):
    if input_string[i] == input_string[i + 1]:
        letter_counter = letter_counter + 1
    else:
        result = result + input_string[i] + str(letter_counter)
        letter_counter = 1

print(result)
