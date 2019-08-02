import re

mail_list = ["ddd@naver.com", "kkk@daum.net", "uuu@myhome.co.kr"]

p = re.compile(".*[@].*[.](?=com$|net$)")
for mail in mail_list:
    if p.match(mail):
        print(mail)
