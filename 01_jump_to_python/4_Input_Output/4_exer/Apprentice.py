def show_candidate(candidate_list):
    print(candidate_list)


def make_idol(candidate_list):
    for idol_app in candidate_list:
        print("신예 아이돌", idol_app, "인기 급상승")


def make_world_star(candidate_list):
    for idol_app in candidate_list:
        print("아이돌", idol_app, "월드스타 등극")


with open("연습생.txt", 'r') as app_file:
    data = app_file.read()
    candidate = data.split("굈")
    candidate.remove('')
    show_candidate(candidate)
    make_idol(candidate)
    make_world_star(candidate)