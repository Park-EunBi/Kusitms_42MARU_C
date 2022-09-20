import re
import regular

# entity_name : 개체명
# value : 값
# start_idx : 시작점
# end_idx : 끝점
# tagged_sentence : 치환한 결과

def find_sys(sentence):

    weight = re.compile(regular.weight) # 미리 컴파일
    volume = re.compile(regular.volume) # 미리 컴파일
    pressure = re.compile(regular.pressure) # 미리 컴파일
    temperature = re.compile(regular.temperature) # 미리 컴파일
    speed = re.compile(regular.speed) # 미리 컴파일
    data = re.compile(regular.data) # 미리 컴파일
    energy = re.compile(regular.energy) # 미리 컴파일
    currency = re.compile(regular.currency) # 미리 컴파일
    time = re.compile(regular.time)
    date = re.compile(regular.date)

    sys_list = [weight, volume, pressure, temperature, speed, data, energy, currency, time, date]
    sys_name = ["weight", "volume", "pressure", "temperature", "speed", "data", "energy", "currency", "time", "date"]

    replace_sentence = sentence
    split_sentence = sentence.split()

    final_result = []
    # 띄어쓰기 단위로 분리
    for word in split_sentence:
        for i in range(len(sys_list)):
            find = re.search(sys_list[i], word)
            if(find == None):
                continue
            else:
                search_entity = find
                end_idx = search_entity.end()
                if end_idx == 0:
                    continue
                value = search_entity.group()
                start_idx = search_entity.start()
                tagged_sentence = "@sys_{}".format(sys_name[i])
            word = tagged_sentence
            replace_sentence = replace_sentence.replace(value, word)
            if (word=="date") is True:
                txt = re.subn('(년|월|일)',tagged_sentence)
                print(txt)
            final_result = [tagged_sentence, value, start_idx, end_idx, replace_sentence]

    return final_result

sentence1 = "2022년3월21일에 보낸 메일 찾아줘"
sentence2 = "우유 100mg 사와"
sentence3 = "1GB 메모리"

print(find_sys(sentence1))
print()
print(find_sys(sentence2))
print()
print(find_sys(sentence3))