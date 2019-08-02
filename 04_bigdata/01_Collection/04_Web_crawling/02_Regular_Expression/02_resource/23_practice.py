import re


def space_to_underbar(sub_str):
    p = re.compile(' ')
    s = p.sub("_", sub_str)
    if s:
        return s
    return None


def underbar_to_space(sub_str):
    p = re.compile('_')
    s = p.sub(" ", sub_str)
    if s:
        return s
    return None


testStr1 = 'I was born in the Busan, and now I am studying in Daegu'
print(space_to_underbar(testStr1))

testStr2 = 'I_was_born_in_the_Busan,_and_now_I_am_studying_in_Daegu'
print(underbar_to_space(testStr2))
