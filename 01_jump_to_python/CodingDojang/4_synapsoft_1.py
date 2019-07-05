NameString = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
nameBook = NameString.split(',')
kim = 0
lee = 0
jaeyoung = 0
for i in range(0, len(nameBook)):
    if nameBook[i][0] == "김":
        kim = kim + 1
    elif nameBook[i][0] == "이":
        lee = lee + 1
        if nameBook[i] == "이재영":
            jaeyoung += 1

print("1. 김씨: %d, 이씨: %d" %(kim, lee))
print("2. 이재영 : %d명" %(jaeyoung))
print("3. 중복을 제거한 이름 \n{0}".format(set(nameBook)))
print("4. 중복을 제거하고 오름차순 이름 \n{0}".format(sorted(set(nameBook))))
