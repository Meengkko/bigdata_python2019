from xml.etree.ElementTree import Element, parse
import xml.etree.ElementTree as ET


def show_summary():

    number_of_students = 0
    number_of_woman = 0
    advanced_programmer = 0
    ever_program = 0
    python_user = 0
    related_major = 0
    major_identifier = ["컴퓨터", "통계"]
    age_histogram = {"20대": 0, "30대": 0, "40대": 0}
    twenties = []
    thirties = []
    forties = []

    with open("students_info.xml", 'r', encoding='utf-8') as students_xml:
        students_text = students_xml.read()

    root_node = ET.fromstring(students_text)
    number_of_students = len(root_node)
    for student in root_node:
        if student.items()[1][1] == "여":
            number_of_woman += 1

        if int(student.find('age').text) in range(20, 30):
            age_histogram["20대"] += 1
            twenties.append((student.items()[0][1], int(student.find('age').text)))
        elif int(student.find('age').text) in range(30, 40):
            age_histogram["30대"] += 1
            thirties.append((student.items()[0][1], int(student.find('age').text)))
        else:
            age_histogram["40대"] += 1
            forties.append((student.items()[0][1], int(student.find('age').text)))

        for major_str in major_identifier:
            if major_str in student.find('major').text:
                related_major += 1

        try:
            if student.find('practicable_computer_languages').text:
                ever_program += 1
                for languages in student.find('practicable_computer_languages'):
                    if languages.items()[0][1].lower() == "python":
                        python_user += 1

                    if languages.items()[1][1] == "상":
                        advanced_programmer += 1
            else:
                pass
        except AttributeError:
            pass

    print("<요약정보>")
    print("*전체 학생수 : %d명" % number_of_students)
    mannum = number_of_students - number_of_woman
    print("*성별\n\t-남학생: %d명 (%.1f%%)\n\t-여학생: %d명 (%.1f%%)"
          % (mannum, (mannum/number_of_students) * 100, number_of_woman, (1-mannum/number_of_students)*100))
    print("*전공여부\n\t-전공자(컴퓨터 공학, 통계): %d명 (%.1f%%)" % (related_major, related_major/number_of_students*100))
    print("\t-프로그래밍 언어 경험자: %d명 (%.1f%%)" % (ever_program, ever_program/number_of_students*100))
    print("\t-프로그래밍 언어 상급자: %d명 (%.1f%%)" % (advanced_programmer, advanced_programmer/number_of_students*100))
    print("\t-파이썬 경험자: %d명 (%.1f%%)" % (python_user, python_user/number_of_students*100))

    print("*연령대\n\t-20대: %d명 (%.1f%%) [" % (age_histogram["20대"], age_histogram["20대"]/number_of_students*100), end='')
    [print(i, ":", j, end=', ') for i, j in twenties]
    print("\b\b]")
    print("\t-30대: %d명 (%.1f%%) [" % (age_histogram["30대"], age_histogram["30대"] / number_of_students*100), end='')
    [print(i, ":", j, end=', ') for i, j in thirties]
    print("\b\b]")
    print("\t-40대: %d명 (%.1f%%) [" % (age_histogram["40대"], age_histogram["40대"] / number_of_students*100), end='')
    [print(i, ":", j, end=', ') for i, j in twenties]
    print("\b\b]")


def total_data_print():
    tree = parse("students_info.xml")
    students_list = tree.getroot()

    for student in students_list:
        print("\n\n%s\n\t성별: %s\n\t나이: %s\n\t전공: %s\n\t사용 가능한 언어"
              % (student.items()[0][1], student.items()[1][1],
                 student.find('age').text, student.find('major').text), end="")
        try:
            if student.find('practicable_computer_languages').text:
                for languages in student.find('practicable_computer_languages'):
                    print("\n\t\t->%s\t(학습기간: %s, Level: %s)"
                          % (languages.items()[0][1], languages.find('period').items()[0][1]
                             , languages.items()[1][1]), end="")
            else:
                print(": 없음", end="")
        except AttributeError:
            print(": 없음", end="")


def main():
    menu = '''
==================
1. 요약 정보
2. 전체 데이터 조회
3. 종료
==================
메뉴 입력: '''

    while True:
        print("\n\n학생정보 XML 데이터 분석 시작...")
        option = input(menu)
        if option == '1':
            show_summary()
        elif option == '2':
            total_data_print()
        elif option == '3':
            print("학생 정보 분석 완료!")
            break
        else:
            print("올바른 번호를 입력하세요!")


main()
