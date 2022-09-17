import re
import regular

# entity_name : 개체명
# value : 값
# start_idx : 시작점
# end_idx : 끝점
# tagged_sentence : 치환한 결과

def sys_weight(sentence):
    # 이 부분 사용성 좋게 변경 필요
    # 루프 돌며 사용할 수 있도록

    # 이 부분을 루프 돌면 될 것 같다
    weight = regular.weight
    weight = re.compile(weight) # 미리 컴파일

    replace_sentence = sentence
    split_sentence = sentence.split()


    final_result = []
    # 띄어쓰기 단위로 분리
    for word in split_sentence:
        search_entity = re.search(weight, word)
        if(re.search(weight, word) == None):
            continue
        entity_name = "@sys_weight"
        value = search_entity.group()
        start_idx = search_entity.start()
        end_idx = search_entity.end()
        tagged_sentence = entity_name
        word = tagged_sentence
        replace_sentence = replace_sentence.replace(value, word)

        # list 로 변경
        # result = {"entity_name": entity_name, "value": value, "start_idx": start_idx, "end_idx": end_idx, \
        #           "replace_sentence": replace_sentence}

        final_result = [entity_name, value, start_idx, end_idx, replace_sentence]

    return final_result

sentence1 = "mg 오늘 뉴스 들려줘 kg 2022년 10월 1일은 무슨 요일이야"

# sentence2 = "이번주 사수자리 운세 알려줘"
# sentence3 = "올해 무슨 해야"

print(sys_weight(sentence1))
print()
# print(sys_weight(sentence2))
# print()
# print(sys_weight(sentence3))

# 숫자 범위 어디까지 허용?
# 여러개의 엔티티가 포함되어있을 때 결과는 하나만 출력
# 그럼 찾은 value 값도 마지막 하나만 출력?
# 결과 값만 하나로 출력하고 value 같은 건 하나의 리스트에 전부 담아서 제공해야 하나?