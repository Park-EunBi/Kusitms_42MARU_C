import re

def selectLunarPeriod(text):

    regex1= '음력\s?[0-9]+월'

    regex=[regex1]

    for x in regex:
        m = x.finditer(x,text)

        if m:
            for r in m:
                tagged_sentence = text.replace((text[r.start():r.end()]), '@sys.date.period.lunar')
                print(
                    "[ entity_name : @sys.date.period.lunar, value : {}, start_idx : {}, end_idx : {}, tagged_sentence : {} ]".format(
                        r.group(), r.start(), r.end(), tagged_sentence));






