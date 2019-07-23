from xml.etree.ElementTree import Element, parse
import xml.etree.ElementTree as ET


def indent(elem, level=0):
    i = "\n"+level*"\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i+"\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i

    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def show_summary():
    # number_dict = {"students": 0, "woman": 0, "advanced": 0, "ever": 0, "python": 0, "related": 0}
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

    with open("students_info2.xml", 'r', encoding='utf-8') as students_xml:
        students_text = students_xml.read()

    root_node = ET.fromstring(students_text)
    number_of_students = len(root_node)
    for student in root_node:
        if student.get("sex") == "여":
            number_of_woman += 1

        if int(student.find('age').text) in range(20, 30):
            age_histogram["20대"] += 1
            twenties.append((student.get("name"), int(student.find('age').text)))
        elif int(student.find('age').text) in range(30, 40):
            age_histogram["30대"] += 1
            thirties.append((student.get("name"), int(student.find('age').text)))
        else:
            age_histogram["40대"] += 1
            forties.append((student.get("name"), int(student.find('age').text)))

        for major_str in major_identifier:
            if major_str in student.find('major').text:
                related_major += 1

        try:
            if student.find('practicable_computer_languages').text:
                ever_program += 1
                for languages in student.find('practicable_computer_languages'):
                    if languages.get("name").lower() == "python" or "파이" in languages.get("name"):
                        python_user += 1

                    if languages.get("level") == "상":
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
    [print(i, ":", j, end=', ') for i, j in forties]
    print("\b\b]")


def insert_info():
    tree = parse("students_info2.xml")
    students_list = tree.getroot()
    new_id_num_int = int(students_list[len(students_list)-1].get("ID")[3:]) + 1
    new_id_num = "ITT" + "0" * (3 - len(str(new_id_num_int))) + str(new_id_num_int)
    student_name = input("이름을 입력하세요. (종료는 Enter)")
    if student_name == "":
        return
    student = Element('student')
    student.attrib['ID'] = new_id_num
    student.attrib['name'] = student_name
    student.attrib['sex'] = input("성별을 입력하세요.")
    ET.SubElement(student, "age").text = input("나이를 입력하세요.")
    ET.SubElement(student, "major").text = input("전공을 입력하세요.")
    practicable = Element('practicable_computer_languages')
    while True:
        language_name = input("-사용가능한 컴퓨터 언어를 입력하시오.\n\t언어 이름(종료는 Enter 입력): ")
        if language_name == "":
            students_list.append(student)
            indent(students_list)
            ET.dump(student)
            ET.ElementTree(students_list).write('students_info2.xml')
            return
        language = Element("language")
        language.attrib['name'] = language_name
        language.attrib['level'] = input("수준(상,중,하): ")
        language_period = Element('period')
        language_period.attrib['value'] = input("학습 기간(년/개월 단위) : ")
        language.append(language_period)
        practicable.append(language)
        student.append(practicable)


def show_individual_detail(node):
    print("\n%s (%s)\n\t-성별: %s\n\t-나이: %s\n\t-전공: %s\n\t사용 가능한 언어"
          % (node.get("name"), node.get("ID"), node.get("sex"), node.findtext("age"), node.findtext("major")), end="")
    try:
        if node.find('practicable_computer_languages').text:
            for languages in node.find('practicable_computer_languages'):
                print("\n\t\t->%s\t(학습기간: %s, Level: %s)"
                      % (languages.get("name"), languages.find('period').get("value")
                         , languages.get("level")), end="")
        else:
            print(": 없음")
    except AttributeError:
        print(": 없음")


def total_data_print():

    tree = parse("students_info2.xml")
    students_list = tree.getroot()

    for student in students_list:
        show_individual_detail(student)


def optional_printer(option, keyword):
    tree = parse("students_info2.xml")
    note = tree.getroot()
    option_dict = {1: "ID", 2: "name", 3: "age", 4: "major", 5: "name", 6: "value", 7: "level"}
    node_list_name = []
    for student in note.getiterator("student"):
        if option in range(1, 3):
            if keyword in student.get(option_dict[option]):
                node_list_name.append(student)
        elif option in range(3, 5):
            if keyword in student.find(option_dict[option]).text:
                node_list_name.append(student)
        elif option == 5 or option == 7:
            for language in student.find("practicable_computer_languages"):
                if keyword in language.get(option_dict[option]):
                    node_list_name.append(student)
                    break
        elif option == 6:
            for language in student.find("practicable_computer_languages"):
                if keyword in language.find("period").get(option_dict[option]):
                    node_list_name.append(student)
                    break
    if len(node_list_name) == 1:
        show_individual_detail(node_list_name[0])
    else:
        for std_node in node_list_name:
            print("%s (%s %s %s)" %
                  (std_node.get("ID"), std_node.get("name"), std_node.get("sex"), std_node.find("age").text))


def data_print():
    sub_menu = '''
<조회 서브 메뉴>
1. 개별 학생 조회
2. 전체 학생 조회
3. 상위 메뉴
메뉴 입력: '''

    while True:
        print(sub_menu)
        option = input()
        if option == '1':
            search_option = int(input("1. ID\n2. 이름\n3. 나이\n4. 전공\n5. 컴퓨터 언어 명"
                                      "\n6. 컴퓨터 언어 학습 기간\n7. 컴퓨터 언어 레벨\n8. 상위 메뉴\n메뉴 입력: "))
            search_keyword = input("검색어를 입력하세요: ")
            optional_printer(search_option, search_keyword)
        elif option == '2':
            total_data_print()
        elif option == '3':
            break


def amendment():
    object_id = input("수정할 학생의 ID를 입력하세요: ")
    tree = parse("students_info2.xml")  # 생성한 xml 파일 파싱하기
    note = tree.getroot()
    for parent in note.getiterator("student"):
        if object_id == parent.get("ID"):
            break

    print("1. 이름: %s" % parent.get("name"))
    print("2. 성별: %s" % parent.get("sex"))
    print("3. 나이: %s" % parent.findtext("age"))
    print("4. 전공: %s" % parent.findtext("major"))
    print("사용가능한 언어")
    index = 5
    for language_value in parent.getiterator("language"):
        if language_value:
            for period_value in language_value.getiterator("period"):
                print("%d. %s\n%d. 학습기간: %s\n%d. level: %s"
                      % (index, language_value.get("name"), index+1, period_value.get("value"), index+2, language_value.get("level")))
                index += 3
    amendment_index = int(input("수정할 항목의 번호를 입력하세요: "))
    amendment_cont = input("수정할 값을 입력하세요: ")

    if amendment_index == 1:
        parent.attrib["name"] = amendment_cont
    elif amendment_index == 2:
        parent.attrib["sex"] = amendment_cont
    elif amendment_index == 3:
        parent.find("age").text = amendment_cont
    elif amendment_index == 4:
        parent.find("major").text = amendment_cont
    if amendment_index > 4:
        program_amend = dict(enumerate(parent.getiterator("language")))[(amendment_index-5)//3]
        if amendment_index % 3 == 2:
            program_amend.attrib["name"] = amendment_cont
        elif amendment_index % 3 == 0:
            program_amend.find("period").attrib["value"] = amendment_cont
        elif amendment_index % 3 == 1:
            program_amend.attrib["level"] = amendment_cont
    ET.ElementTree(note).write("students_info2.xml")


def delete_info():
    object_id = input("삭제할 학생의 ID를 입력하세요: ")
    tree = parse("students_info2.xml")  # 생성한 xml 파일 파싱하기
    note = tree.getroot()
    for parent in note.getiterator("student"):
        if object_id == parent.get("ID"):
            break

    note.remove(parent)
    ET.ElementTree(note).write("students_info2.xml")
    print("삭제되었습니다.")


def main():
    menu = '''
[ 메인 메뉴 ]
1. 요약 정보
2. 입력
3. 조회
4. 수정
5. 삭제
6. 종료
메뉴 입력: '''

    while True:
        print("\n\n학생정보 XML 데이터 분석 시작...")
        option = input(menu)
        if option == '1':
            show_summary()
        elif option == '2':
            insert_info()
        elif option == '3':
            data_print()
        elif option == '4':
            amendment()
        elif option == '5':
            delete_info()
        elif option == '6':
            print("학생 정보 분석 완료!")
            break
        else:
            print("올바른 번호를 입력하세요!")


main()
