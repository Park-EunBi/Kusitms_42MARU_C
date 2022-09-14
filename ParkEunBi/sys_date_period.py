import re
# '날짜'에 해당하는 엔티티를 태깅합니다.

# entity_name : 개체명
# value : 값
# start_idx : 시작점
# end_idx : 끝점
# tagged_sentence : 치환한 결과

def sys_date_period(sentence):
    date1 = r"[\d\d\d\d\S\s\d\d\S\s\d]\S부터|\S요일부터|오늘부터|내일부터|어제부터|" \
            r"모래부터|어저께부터|\d일\S부터|평일부터|주말부터|올해부터|작년부터|" \
            r"제작년부터|내후년부터|[\d\d\d\d\S\s\d\d\S\s\d]\전부터"  # 부터
    date2 = r"\S번주"  # 주차를 나타내는 말
    date3 = r"\d\d\d\d년|\d\d년|[\d]\d월|[\d]\d일|[\d\d]월|[\d\d]일"  # 숫자로 표현된 날자
    date4 = r"[\d\d\d\d\S\s\d\d\S\s\d]\S까지|\S요일까지|오늘까지|내일까지|어제까지" \
            r"모래까지|어저께까지|\d일\S까지|평일까지|주말까지|올해까지|작년까지|" \
            r"제작년까지|내후년부터"  # 까지
    date5 = r"오늘|내일|모래|글피|어제|어저께|다다음주|다음주|저번주|이번주|올해|다음해|내년|작년|제작년|내후년"

    date = date1 + "|" + date2 + "|" + date3 + "|" + date4 + "|" + date5

    date = re.compile(date)  # 미리 컴파일

    replace_sentence = sentence
    split_sentence = sentence.split()

    final_result = []
    for word in split_sentence:
        search_entity = re.search(date, word)

        if (re.search(date, word) == None):
            continue

        entity_name = "@sys_date_period"
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

sentence1 = "이번주 사수자리 운세 알려줘"
sentence2 = "2020년 3일전부터 내일까지 날씨 알려줘"
sentence3 = "올해 무슨 해야"

print(sys_date_period(sentence1))
print()
print(sys_date_period(sentence2))
print()
print(sys_date_period(sentence3))
