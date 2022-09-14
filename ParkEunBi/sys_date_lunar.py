import re
# 날짜 중에서 '음력'에 해당하는 엔티티를 태깅합니다.

# entity_name : 개체명
# value : 값
# start_idx : 시작점
# end_idx : 끝점
# tagged_sentence : 치환한 결과

def sys_date_lunar(sentence):
    date0 = r"음력"
    date1 = r"\d\d\d\d년|\d\d년|[\d]\d월|[\d]\d일|[\d\d]월|[\d\d]일" # 숫자로 표현된 날자
    date2 = r"\S번주" # 주차를 나타내는 말
    date3 = r"오늘|내일|모래|글피|어제|어저께|다다음주|다음주|저번주|이번주|올해|다음해|내년|작년|제작년|내후년" # 날짜를 가리키는 말 (데이터 필요)
    date4 = r"설날|설|추석|보름|생일|정월" # 특정 날짜를 나타내는 말

    date = date0 +"|" + date1 + "|" + date2 + "|" + date3 + "|" + date4

    date = re.compile(date) # 미리 컴파일

    replace_sentence = sentence
    split_sentence = sentence.split()

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

sentence1 = "음력 1월1일"
sentence2 = "음력 2019년 5월 5일"
sentence3 = "올해 음력 5월 16일"
sentence4 = "음력 설"

print(sys_date_lunar(sentence1))
print()
print(sys_date_lunar(sentence2))
print()
print(sys_date_lunar(sentence3))
print()
print(sys_date_lunar(sentence4))