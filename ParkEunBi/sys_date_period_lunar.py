import re
# 날짜 중에서 '음력 기간'에 해당하는 엔티티를 태깅합니다.

# entity_name : 개체명
# value : 값
# start_idx : 시작점
# end_idx : 끝점
# tagged_sentence : 치환한 결과

def sys_date_period_lunar(sentence):
    date0 = r"음력"
    date1 = r"\d\d\d\d년|\d\d년|[\d]\d월|[\d]\d일|[\d\d]월|[\d\d]일" # 숫자로 표현된 날자
    date2 = r"\S번주" # 주차를 나타내는 말
    date3 = r"오늘|내일|모래|글피|어제|어저께|다다음주|다음주|저번주|" \
            r"이번주|올해|다음해|내년|작년|제작년|내후년" # 날짜를 가리키는 말 (데이터 필요)
    date4 = r"설날|설|추석|생일|정월대보름|정월 대보름|정월|대보름|보름" # 특정 날짜를 나타내는 말

    date = date0 +"|" + date1 + "|" + date2 + "|" + date3 + "|" + date4

    date = re.compile(date) # 미리 컴파일

    replace_sentence = sentence1
    split_sentence = sentence1.split()

    final_result = []
    for word in split_sentence:
        search_entity = re.search(date, word)

        if(re.search(date, word) == None):
            continue

        entity_name = "@sys_date_lunar"
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

sentence1 = "정월 보름은 음력 1월을 말합니다"
sentence2 = "음력 8월은 음력에서 여덟 번째 달이다"
print(sys_date_period_lunar(sentence1))
print()
print(sys_date_period_lunar(sentence2))