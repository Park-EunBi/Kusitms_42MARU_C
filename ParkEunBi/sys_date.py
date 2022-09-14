import re
# 날짜 중에서 '기간 범위' 에 해당하는 엔티티를 태깅합니다.

# 2019년은 sys.date 에도 포함되고, sys.date.period 에도 포함되는데
# 이럴 땐 상위 엔티티를 따르는 건지, 하위 엔티티를 따르는건지?

# entity_name : 개체명
# value : 값
# start_idx : 시작점
# end_idx : 끝점
# tagged_sentence : 치환한 결과

def sys_date(sentence):
    date1 = r"\d\d\d\d년|\d\d년|[\d]\d월|[\d]\d일|[\d\d]월|[\d\d]일" # 숫자로 표현된 날자
    date2 = r"\S요일" # 요일
    date3 = r"오늘|내일|모래|글피|어제|어저께|다다음주|다음주|저번주|이번주|올해|다음해|내년|작년|제작년|내후년" # 날짜를 가리키는 말 (데이터 필요)

    date = date1 +"|" + date2 +"|" + date3

    date = re.compile(date) # 미리 컴파일

    replace_sentence = sentence
    split_sentence = sentence.split()


    final_result = []
    # 띄어쓰기 단위로 분리
    for word in split_sentence:
        search_entity = re.search(date, word)

        if(re.search(date, word) == None):
            continue

        entity_name = "@sys_date"
        value = search_entity.group()
        start_idx = search_entity.start()
        end_idx = search_entity.end()
        tagged_sentence = entity_name
        word = tagged_sentence
        replace_sentence = replace_sentence.replace(value, word)

        result = {"entity_name": entity_name, "value": value, "start_idx": start_idx, "end_idx": end_idx, \
                  "replace_sentence": replace_sentence}

        final_result.append(result)

    return final_result

sentence1 = "오늘 뉴스 들려줘 2022년 10월 1일은 무슨 요일이야"
sentence2 = "이번주 사수자리 운세 알려줘"
sentence3 = "올해 무슨 해야"
print(sys_date(sentence1))
print()
print(sys_date(sentence2))
print()
print(sys_date(sentence3))