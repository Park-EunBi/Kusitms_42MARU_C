import re

def selectDate(text):
    regex1 = '[월화수목금토일]요일'
    regex2 = '(오늘|내일|모레|글피|내일모레)'
    regex3 = '([0-9]{4}[년-]\s?[0-9]{1,2}[월-]\s?[0-9]{1,2}[일\s]|[0-9]{1,2}월\s?[0-9]{1,2}일|[0-9]{4}년|[0-9]{1,2}월|[0-9]{1,2}일)'

    regex=[regex1,regex2,regex3]

    for x in regex:
        m=re.finditer(x,text)

        if m:
            for r in m:
                tagged_sentence = text.replace((text[r.start():r.end()]), '@sys.date')
                print("[ entity_name : @sys.date, value : {}, start_idx : {}, end_idx : {}, tagged_sentence : {} ]".format(
                        r.group(), r.start(), r.end(), tagged_sentence));
