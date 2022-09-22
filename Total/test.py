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

    f = open("testsentence.txt", 'r')
    lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        if re.match(r'input\s:\s', lines[i]):
            input = re.sub(r'input\s:\s', '', lines[i])
        elif re.match(r'entity_name\s:\s', lines[i]):
            entity_name = re.sub(r'entity_name\s:\s', '', lines[i])
            entity_name_list = entity_name.split(',')
        elif re.match(r'value\s:\s', lines[i]):
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
            Result = [entity_name_list, value_list, start_idx_list, end_idx_list, tagged_sentence]
            assert Result == priRegex(input)

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
