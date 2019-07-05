def search_visitor(name):
    with open("방명록.txt", 'r') as name_file:
        if name in name_file.read():
            return name
        else:
            return ''

while True:
    guest_name = input("이름을 입력하세요: ")
    if search_visitor(guest_name):
        print("%s님 다시 방문해주셔서 감사합니다. 즐거운 시간되세요." %guest_name)
    else:
        guest_birth = input("생년월일을 입력하세요 (예:801212): ")
        with open("방명록.txt", 'a') as add_info:
            data = "%s %s\n" % (guest_name, guest_birth)
            add_info.write(data)
        print("%s님 환영합니다. 아래 내용을 입력하셨습니다.\n%s %s"%(guest_name, guest_name, guest_birth))