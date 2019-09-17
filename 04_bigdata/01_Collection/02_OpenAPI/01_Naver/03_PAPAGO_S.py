import os
import sys
import urllib.request
client_id = ""
client_secret = ""
url = "https://openapi.naver.com/v1/language/translate"


def main():
    source = {"1": "ko", "2": "en", "3": "ja", "4": "zh-CN", "5": "zh-TW"}
    target = {"1": "ko", "2": "en", "3": "ja", "4": "zh-CN", "5": "zh-TW"}

    source_choice = input("1.한국어\n2.영어\n3.일본어\n4.중국어(간체)\n5.중국어(번체)\n번역할 대상 언어를 선택하십시오. : ")
    target_choice = input("1.한국어\n2.영어\n3.일본어\n4.중국어(간체)\n5.중국어(번체)\n어느 언어로 번역하시겠습니까? : ")

    sentence = input("번역할 문장을 입력하세요.")
    encText = urllib.parse.quote(sentence)
    data = "source=" + source[source_choice] + "&target=" + target[target_choice] + "&text=" + encText

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()

    if(rescode==200):
        response_body = response.read().decode()
        response_dict = eval(response_body)
        translated_str = response_dict["message"]["result"]["translatedText"]
        print("\n\n 번역전 문장: %s \n 번역된 문장: %s" % (sentence, translated_str))
    else:
        print("Error Code:" + rescode)


if __name__ == "__main__":
    main()
