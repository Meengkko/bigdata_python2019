def show_candidate(candidate_list):
    print(candidate_list)


def make_idol(candidate_list):
    for idol_app in candidate_list:
        print("�ſ� ���̵�", idol_app, "�α� �޻��")


def make_world_star(candidate_list):
    for idol_app in candidate_list:
        print("���̵�", idol_app, "���彺Ÿ ���")


with open("������.txt", 'r') as app_file:
    data = app_file.read()
    candidate = data.split("�n")
    candidate.remove('')
    show_candidate(candidate)
    make_idol(candidate)
    make_world_star(candidate)