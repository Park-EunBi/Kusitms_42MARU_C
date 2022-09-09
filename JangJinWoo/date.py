import re

def checkDate(text):

    # 요일
    m = re.finditer('[월화수목금토일]요일', text)

    if m:
        return "ok";

    # 오늘, 내일, 어제, 모레, 글피, 다음주, 다다음주

    m = re.finditer('(오늘|내일|모레|글피|내일모레|다음주|다다음주)', text)

    if m:
        return "ok";

    # 날짜 09월 03일 | 9월 3일 | 09-03 // 2022년 9월 9일 | 2022-09-09 | 2022년 09월 09일

    m = re.finditer(
        '([0-9]{4}[년-].[0-9]{1,2}[월-].[0-9]{1,2}[일\s]|[0-9]{1,2}월.[0-9]{1,2}일|[0-9]{4}년|[0-9]{1,2}월|[0-9]{1,2}일)', text)

    if m:
        return "ok";


def selectDate(text):

    # 요일
    m = re.finditer('[월화수목금토일]요일', text)

    if m:
        for r in m:
            tagged_sentence = text.replace((text[r.start():r.end()]), '@sys.date')
            print("[ entity_name : @sys.date, value : {}, start_idx : {}, end_idx : {}, tagged_sentence : {} ]".format(
                r.group(), r.start(), r.end(), tagged_sentence));

    # 오늘, 내일, 어제, 모레, 글피, 다음주, 다다음주

    m = re.finditer('(오늘|내일|모레|글피|내일모레|다음주|다다음주)', text)
    if m:
        for r in m:
            tagged_sentence = text.replace((text[r.start():r.end()]),'@sys.date')
            print("[ entity_name : @sys.date, value : {}, start_idx : {}, end_idx : {}, tagged_sentence : {} ]".format(r.group(),r.start(),r.end(),tagged_sentence));




    #날짜 09월 03일 | 9월 3일 | 09-03 // 2022년 9월 9일 | 2022-09-09 | 2022년 09월 09일

    m = re.finditer('([0-9]{4}[년-].[0-9]{1,2}[월-].[0-9]{1,2}[일\s]|[0-9]{1,2}월.[0-9]{1,2}일|[0-9]{4}년|[0-9]{1,2}월|[0-9]{1,2}일)',text)

    if m:
        for r in m:
            tagged_sentence = text.replace((text[r.start():r.end()]), '@sys.date')
            print("[ entity_name : @sys.date, value : {}, start_idx : {}, end_idx : {}, tagged_sentence : {} ]".format(
                r.group(), r.start(), r.end(), tagged_sentence));