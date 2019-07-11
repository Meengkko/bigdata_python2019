with open("sample.txt", 'r') as score_file:
    list_numbers = score_file.read().split('\n')
    sum_numbers = sum(list(map(lambda x: int(x.strip()), list_numbers)))
    len_number = len(list_numbers)
    

print(len_number)
with open("result.txt", 'w') as write_file:
    write_file.write(f"{sum_numbers}\n{sum_numbers/len_number}")
