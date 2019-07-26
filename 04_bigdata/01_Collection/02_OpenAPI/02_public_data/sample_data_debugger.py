import json


with open("sample.json", encoding='UTF8') as json_file:
    json_object = json.load(json_file)
    json_string = json.dumps(json_object)
    student_json_big_data = json.loads(json_string)


pass
