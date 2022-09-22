import re
import main
from main import priRegex


def test_file():
    entity_name_list =[]
    value_list = []
    start_idx_list =[]
    end_idx_list =[]
    tagged_sentence = []
    Result =[]

    f = open("testsentence.txt", 'r') #텍스트 파일 불러오기
    lines = f.readlines() #한 줄씩 읽어서 lines 리스트에 저장
    for i in range(len(lines)): #lines리스트 돌기
        lines[i] = lines[i].strip() #\n제거
        if re.match(r'input\s:\s', lines[i]): #input인 경우
            input = re.sub(r'input\s:\s', '', lines[i]) #input지워주고, input 문장만 변수에 저장
        elif re.match(r'entity_name\s:\s', lines[i]): #entity name인 경우
            entity_name = re.sub(r'entity_name\s:\s', '', lines[i]) #entity name지워주고
            entity_name_list = entity_name.split(',') #엔티티 이름 ,기준으로 나눠서 리스트에 저장
        elif re.match(r'value\s:\s', lines[i]): #동일한 방식
            value = re.sub(r'value\s:\s', '', lines[i])
            value_list = value.split(',')
        elif re.match(r'start_idx\s:\s', lines[i]):
            start_idx = re.sub(r'start_idx\s:\s', '', lines[i])
            start_idx_list = start_idx.split(',')
        elif re.match(r'end_idx\s:\s', lines[i]):
            end_idx = re.sub(r'end_idx\s:\s', '', lines[i])
            end_idx_list = end_idx.split(',')
        elif re.match(r'tagged_sentence\s:\s', lines[i]):
            tagged_sentence = re.sub(r'tagged_sentence\s:\s', '', lines[i])
            Result = [entity_name_list, value_list, start_idx_list, end_idx_list, tagged_sentence] #한 문장의 output결과 Result에 저장
            assert Result == Regex(input) #main코드로 돌리고나온 결과와 동일한지 확인

'''
def test_date():
    pattern = main.date
    valid_date = [
        "오늘",
        "내일",
        "어제",
        "2018년 1월 15일",
        "1월 1일",
        "수요일",
    ]
    for date in valid_date:
        assert re.match(pattern, date)

def test_date_period():
    pattern = main.date_period
    valid_date_period = [
        "이번주",
        "올해",
        "주말",
        "2019년",
        "1월",
        "1일부터 10일까지"
    ]
    for date_period in valid_date_period:
        assert re.match(pattern, date_period)

def test_date_lunar():
    pattern = main.date_lunar
    valid_date_lunar = [
        "음력 1월 1일",
        "음력 2019년 5월 5일",
        "올해 음력 5월 16일",
        "음력 설날",
    ]
    for date_lunar in valid_date_lunar:
        assert re.match(pattern, date_lunar)

'''
