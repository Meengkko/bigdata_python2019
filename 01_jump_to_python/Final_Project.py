# * 요구사항 Ver.1
# 1. Bulls and Cows 게임을 만든다.
# (Bulls and Cows는 0부터 9까지 무작위 숫자를 하나씩만 이용하여 3~5개의 자릿수를 가진 숫자를 이루고
# 플레이어가 이를 맞추는 게임이다. 플레이어는 숫자의 갯수에 맞추어 숫자를 입력하게 되는데
# 이때 각 공란에는 중복된 숫자가 들어가거나, 숫자가 들어가지 않을 수도 있다(이 경우 플레이어는 공백문자 입력)
# 플레이어가 입력한 숫자와 정답을 비교하여 숫자와 위치가 맞을경우 Bulls에 하나가 추가되고,
# 숫자만 맞을 경우 Cows에 1이 추가된다.
#
# 난이도는 상급, 중급, 하급으로 나눈다. 상급(5개 숫자, 6번시도), 중급(4개 숫자, 8번시도), 초급(3개 숫자, 10번시도)
#
# 2. 게임이 종료될 경우
# 플레이어가 맞힌경우:
# 1. 플레이어의 이니셜을 영문, 대문자로 3글자를 입력받되, 3글자를 넘어가면 맨앞부터 3글자를 저장한다.
# 2. 그외 플레이어가 시도한 횟수, 걸린시간을 차례대로 파일에 저장해둔다.
#
# 플레이어가 틀린경우:
# 넘어간다
#
# 3. 게임대기화면
# 플레이어는 게임을 하기위해 특정한 Input을 주어야한다.
# 프로그램이 수행되어 이러한 Input을 입력받기까지 대기화면을 설정해둔다.
# 대기화면은 일정한 시간(1~2초) 주기로 초급, 중급, 상급 플레이어의 상위10개 기록을 번갈아가면서 보여주며
# 동일한 시도 횟수의 경우 걸린시간을 기준으로 순위를 가른다.

# Step1] 입력, 출력
# 출력1(플레이어 순위) -> 입력1(게임시작) -> 출력2(난이도 선택) -> 입력2(난이도 선택)
# -> 출력3(선택 난이도, 시도한 횟수) -> 입력3(숫자 선택) -> 맞힌경우 ->
# 입력4(이니셜 입력)

# Step2] 기능 식별
# 1. Bulls and Cows 게임
# - 무작위 비복원 추출 (완료)
# - 사용자 입력으로부터 Bulls or Cows 식별후 출력 (완료)
# - 맞힌 경우, 그렇지 않은 경우 분기
# - 맞힌 경우 : 시도한 횟수와 걸린시간 return
# 2. 그 외...
# - 파일 저장
# - 플레이어 순위 출력

# Step3~] 함수 정의부터 테스팅

import time
from random import randint
from os import system


class BullsPlayer:
    def __init__(self, level):
        self.random_number = level + 2
        self.chance = 12 - 2*level
        self.tried_num = 0
        random_candid = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.quest = []
        for i in range(self.random_number):
            self.quest.append(random_candid.pop(randint(0, len(random_candid)-1)))
        # print(self.quest) # 답을 알려주는 기능

    def print_bulls_and_cows(self, guessed_input):
        bulls = 0
        cows = 0
        for i in range(len(self.quest)):
            if guessed_input[i] == self.quest[i]:
                cows = cows + 1
            elif guessed_input[i] in self.quest:
                bulls = bulls + 1

        self.tried_num = self.tried_num + 1
        if guessed_input == self.quest:
            return 0
        print(f"\nBulls: {bulls}, Cows: {cows}\n시도횟수: {self.tried_num}\n남은횟수: {self.chance-self.tried_num}\n")
        return 1


def get_top_ten(file_name):
    top_ten_record = []
    temp = []
    pivot = 1
    with open("%s" % file_name, 'r') as read_file:
        read_lines = read_file.readlines()

    read_lines = list(map(lambda x: x.strip().split(' '), read_lines))
    for i in range(len(read_lines)):
        read_lines[i][0] = int(read_lines[i][0])
    read_lines.sort()

    if len(read_lines) >= 10:
        read_lines = read_lines[:10]

    for list_member in read_lines:
        list_member.append(list_member.pop(0))
        list_member[0] = int(list_member[0])

    while read_lines:
        while read_lines and read_lines[0][2] == pivot:
            temp.append(read_lines.pop(0))
        pivot = pivot + 1
        if temp:
            temp.sort()
            top_ten_record.extend(temp)
            temp = []
    print(top_ten_record)
    return top_ten_record


def hall_of_fame(object_list):
    result_string = "   * HALL OF FAME *\nINIT\tT R Y\tS E C\n=======================\n"
    for list_to_string in object_list:
        result_string = result_string + "%s\t%d\t%.2f\n" % (list_to_string[1], int(list_to_string[2]), list_to_string[0]/1000)
    return result_string


def print_waiting_message(level_one, level_two, level_three):
    system('cls')
    print("     초급자 기록\n")
    print(level_one)
    time.sleep(5)
    system('cls')
    print("     중급자 기록\n")
    print(level_two)
    time.sleep(5)
    system('cls')
    print("     상급자 기록\n")
    print(level_three)
    time.sleep(5)
    system('cls')


file_dict = {1: "level1_log.txt", 2: "level2_log.txt", 3: "level3_log.txt"}
menu = '''    ## Bulls and Cows ##
    +++++++++++++++++++
    | 1. 게임을 한다. |
    | 2. 기록을 본다. |
    | 3. 종료를 한다. |
    ===================
'''

while True:
    system('cls')
    print(menu)
    player_option = input("입력 >>> ")
    if player_option == '1':
        while True:
            input_level = int(input("난이도를 입력하세요. (1.초급, 2.중급, 3.상급) : "))
            if input_level in [1, 2, 3]:
                break
            print("올바른 난이도를 선택하세요.")

        game_result = 0
        player1 = BullsPlayer(input_level)
        start_time = time.time()

        while player1.tried_num != player1.chance:
            input_num = list(map(lambda x: int(x) if x != ' ' else ' ',
                                 input('숫자열을 입력하세요. \n아무 숫자도 입력하지 않으려면 공백 입력: ')))[:input_level+2]
            try:
                game_result = player1.print_bulls_and_cows(input_num)
                if game_result == 0:
                    break
            except IndexError:
                print("숫자열을 잘못 입력하셨습니다.")

        end_time = time.time()
        if game_result == 0:
            winner_initial = input('축하합니다. 이니셜을 입력해주십시오: ').upper()[:3]
            winner_record = str(player1.tried_num) + ' ' + str(int(round(end_time - start_time, 1)*1000)) + ' ' + winner_initial
            try:
                with open(file_dict[input_level], 'a') as winner_log:
                    winner_log.write(winner_record+'\n')
            except FileNotFoundError:
                with open(file_dict[input_level], 'w') as initial_log:
                    initial_log.write(winner_record+'\n')

        elif game_result == 1:
            print("숫자를 맞추지 못하셨습니다 ㅜㅜ\n정답 : " + str(player1.quest))
            input("계속하시려면 아무키나 누르세요.")

    elif player_option == '2':
        record_three = [0, 0, 0]
        for i in range(1, 4):
            try:
                record_three[i-1] = hall_of_fame(get_top_ten(file_dict[i]))
            except FileNotFoundError:
                pass
        print_waiting_message(record_three[0], record_three[1], record_three[2])

    elif player_option == '3':
        print("게임을 종료합니다.")
        break

    else:
        print('올바른 명령을 입력하십시오!')
