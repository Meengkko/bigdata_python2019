from xml.etree.ElementTree import Element, parse
import xml.etree.ElementTree as ET


def show_summary():
    pass


def total_data_print():  # 여기서부터 파싱입니다.
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
