import json


def input_student_info(json_data):
    if json_data:
        new_std_id_num = int(json_data[len(json_data)-1]["student_ID"][3:])+1
        new_std_id = "ITT" + "0"*(3-len(str(new_std_id_num))) + str(new_std_id_num)
    else:
        new_std_id = "ITT001"
    new_json_info = {"student_ID": new_std_id}
    new_json_info["student_name"] = input("이름 (예: 홍길동 ): ")
    new_json_info["student_age"] = input("나이 (예: 29): ")
    new_json_info["address"] = input("주소 (예: 대구광역시 동구 아양로 135): ")
    new_json_info["total_course_info"] = {"num_of_course_learned": input("과거 수강 횟수 (예: 1): ")}
    while True:
        course_taking = input("현재 수강 과목이 있습니까? (예: y/n)")
        if 'y' == course_taking.lower()[0]:
            course_detail = {"course_code": input("강의코드 (예: IB171106, OB0104 ..): ")}
            course_detail["course_name"] = input("강의명 (예: IOT 빅데이터 실무반): ")
            course_detail["teacher"] = input("강사 (예: 이현구): ")
            course_detail["open_date"] = input("개강일 (예: 2017-11-06): ")
            course_detail["close_date"] = input("종료일 (예: 2018-09-05): ")
            try:
                new_json_info["total_course_info"]["learning_course_info"].append(course_detail)
            except KeyError:
                new_json_info["total_course_info"]["learning_course_info"] = [course_detail]
        elif 'n' == course_taking.lower()[0]:
            break
        else:
            print("올바른 입력을 하십시오!(y/n)")
    json_data.append(new_json_info)
    return json_data


def show_individual(individual):
    print("학생 ID: %s\n이름: %s\n나이: %s\n주소: %s\n수강정보\n+ 과거 수강 횟수: %s\n+ 현재 수강 과목"
          % (individual["student_ID"], individual["student_name"]
             , individual["student_age"], individual["address"],
             individual["total_course_info"]["num_of_course_learned"]))
    try:
        for course_info in individual["total_course_info"]["learning_course_info"]:
            print("\t강의 코드: %s\n\t강의명: %s\n\t강사: %s\n\t개강일: %s\n\t종료일: %s"
                  % (course_info["course_code"], course_info["course_name"], course_info["teacher"],
                     course_info["open_date"], course_info["close_date"]))
    except KeyError:
        print("\t없음")


def show_group(individual_list):
    print("\n복수 개의 결과가 검색되었습니다.\n------ 요약 결과 ------")
    [print("학생 ID: " + individual["student_ID"] + "학생 이름: " + individual["student_name"]) for individual in individual_list]


def show_student_info(show_json):
    json_keys = ["student_ID", "student_name", "student_age", "address", "course_name", "teacher"]
    show_menu = '''아래 메뉴를 선택하세요.
1. 전체 학생정보 조회
 검색 조건 선택
2. ID 검색
3. 이름 검색
4. 나이 검색
5. 주소 검색
6. 과거 수강 횟수 검색
7. 현재 강의를 수강중인 학생
8. 현재 수강 중인 강의명
9. 현재 수강 강사
10. 이전 메뉴
메뉴를 선택하세요: '''
    show_option = int(input(show_menu))
    if show_option == 1:
        for indi_student in show_json:
            print("학생 ID: %s\n이름: %s\n나이: %s\n주소: %s\n수강정보\n+ 과거 수강 횟수: %s\n+ 현재 수강 과목"
                  % (indi_student["student_ID"], indi_student["student_name"]
                     , indi_student["student_age"], indi_student["address"], indi_student["total_course_info"]["num_of_course_learned"]))
            try:
                for course_info in indi_student["total_course_info"]["learning_course_info"]:
                    print("\t강의 코드: %s\n\t강의명: %s\n\t강사: %s\n\t개강일: %s\n\t종료일: %s"
                          % (course_info["course_code"], course_info["course_name"],course_info["teacher"],course_info["open_date"],course_info["close_date"]))
            except KeyError:
                print("\t없음")
    elif show_option in range(2, 10):
        search_word = input("검색어를 입력하세요: ")
        search_list = []
        for indi_student in show_json:
            if show_option in range(2, 6):
                if search_word in str(indi_student[json_keys[int(show_option)-2]]):
                    search_list.append(indi_student)
            elif show_option == 6:
                if search_word == str(indi_student["total_course_info"]["num_of_course_learned"]):
                    search_list.append(indi_student)
            elif show_option == 7:
                if "learning_course_info" in list(indi_student["total_course_info"].keys()):
                    search_list.append(indi_student)
            elif show_option in range(8, 10):
                for course in indi_student["total_course_info"]["learning_course_info"]:
                    if search_word in course[json_keys[show_option - 4]]:
                        search_list.append(indi_student)
                        break

        if len(search_list) == 1:
            show_individual(search_list[0])
        else:
            show_group(search_list)


def info_amendment(amendment_json):

    student = {}
    search_id = input("수정할 학생 ID를 입력하세요: ")
    for student in amendment_json:
        if student["student_ID"] == search_id:
            break
    while True:
        amend_input = ''
        show_individual(student)
        option = input("1. 학생 이름\n2. 나이\n3. 주소\n4. 과거 수강 횟수\n5. 현재 수강 중인 강의 정보\n0. 이전 메뉴\n메뉴 번호를 입력하세요.: ")
        if int(option) in range(1, 5):
            amend_input = input("변경할 값을 입력하세요: ")
        if option == "1":
            student["student_name"] = amend_input
        elif option == "2":
            student["student_age"] = amend_input
        elif option == "3":
            student["address"] = amend_input
        elif option == "4":
            student["total_course_info"]["num_of_course_learned"] = amend_input
        elif option == "5":
            while True:
                amend_dict = {"1": "course_code", "2": "course_name", "3": "teacher", "4": "open_date", "5": "close_date"}
                lower_option = input("1. 강의 코드\n2. 강의명\n3. 강사\n4. 개강일\n5. 종료일\n0. 취소")
                if int(lower_option) in range(1, 6):
                    course_index = input("몇 번째 강의 정보를 변경하시겠습니까? (현재 수강중인 강의 %d강)" % (len(student["total_course_info"]["learning_course_info"])))
                    lower_amend_input = input("변경할 값을 입력하세요: ")
                    student["total_course_info"]["learning_course_info"][int(course_index)-1][amend_dict[lower_option]] = lower_amend_input
                elif lower_option == '0':
                    break
        elif option == "0":
            break

    return amendment_json


def delete_info(delete_json):

    student = {}
    search_id = input("삭제할 학생 ID를 입력하세요: ")
    for student in delete_json:
        if student["student_ID"] == search_id:
            break
    delete_option = input("삭제 유형을 선택하세요.\n1. 전체 삭제\n2. 현재 수강 중인 특정 과목정보 삭제\n3. 이전 메뉴\n메뉴 번호를 선택하세요: ")
    if delete_option == "1":
        delete_json.remove(student)
    elif delete_option == "2":
        print_course(student)
        input_index = input("삭제할 강의 번수를 입력하십시오: ")
        student["total_course_info"]["learning_course_info"].remove(student["total_course_info"]["learning_course_info"][int(input_index)-1])

    return delete_json


def print_course(student_data):
    for index, course in enumerate(student_data["total_course_info"]["learning_course_info"]):
        print("**%d번째 강의**\n==============\n\n1. 강의 코드: %s\n2. 강의명: %s\n3. 강사: %s\n4. 개강일: %s\n5. 종료일: %s\n\n"
              % (index+1, course["course_code"], course["course_name"], course["teacher"], course["open_date"], course["close_date"]))


def user_interface():
    menu = '''
<< JSON 기반 학생 정보 관리 프로그램 >>
 1. 학생 정보입력
 2. 학생 정보조회
 3. 학생 정보수정
 4. 학생 정보삭제
 5. 프로그램 종료
 메뉴를 선택하세요: '''
    with open("ITT_Student.json", encoding='UTF8') as json_file:
            json_object = json.load(json_file)
            json_string = json.dumps(json_object)
            student_json_big_data = json.loads(json_string)
    while True:
        # returned_json_big_data = []
        while True:
            option = input(menu)
            if option == '1':
                returned_json_big_data = input_student_info(student_json_big_data)
                break
            elif option == '2':
                show_student_info(student_json_big_data)
            elif option == '3':
                returned_json_big_data = info_amendment(student_json_big_data)
                break
            elif option == '4':
                returned_json_big_data = delete_info(student_json_big_data)
                break
            elif option == '5':
                return 0
            else:
                print("올바른 명령이 아닙니다")
        if option == '1' or option == '3' or option == '4':
            with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                readable_result = json.dumps(returned_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                outfile.write(readable_result)
                print('ITT_Student.json SAVED')


def main():
    is_exit = 1
    while is_exit:
        try:
            is_exit = user_interface()
        except FileNotFoundError:
            new_user_input = input("환영합니다.\n신규 데이터를 생성하시겠습니까? (y,n)")
            if new_user_input.lower()[0] == 'y':
                with open('ITT_Student.json', 'w', encoding='utf8') as outfile:
                    new_json_data = []
                    returned_json_big_data = input_student_info(new_json_data)
                    readable_result = json.dumps(returned_json_big_data, indent=4, sort_keys=True, ensure_ascii=False)
                    outfile.write(readable_result)
                    print('ITT_Student.json SAVED')
            else:
                return


if __name__ == "__main__":
    main()
