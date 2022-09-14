import re

def selectLunarDate(text):
    regex1 = '음력 ([0-9]+월 [0-9]+일|[0-9]{4}년 [0-9]+월 [0-9]+일|설날)'
    regex = [regex1]

    for x in regex:
        m = re.finditer(x, text)

        if m:
            for r in m:
                tagged_sentence = text.replace((text[r.start():r.end()]), '@sys.date.lunar')
                print("[ entity_name : @sys.date.lunar, value : {}, start_idx : {}, end_idx : {}, tagged_sentence : {} ]".format(
                    r.group(), r.start(), r.end(), tagged_sentence));
