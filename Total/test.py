import re
import main
from main import priRegex

def test_Input_tagged_sentence():
    Input = input()
    Output = input()

    Result = priRegex(Input)
    assert Output == str(Result)

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

def test_date_period_lunar():
    pattern = main.date_period_lunar
    valid_date_period_lunar = [
        "음력 1월",
        "음력 2월",
    ]
    for date_period_lunar in valid_date_period_lunar:
        assert re.match(pattern, date_period_lunar)



def test_tagged_sentence():
    sentences = [
        "오늘 뉴스 들려줘1월 1일은 무슨 요일이야",
        "이번주 사수자리 운세 알려줘올해 무슨 해야",
    ]
    entity_name_list = [
        ['@sys.date', '@sys.date', '@sys.unit.duration'],
        ['@sys.date.period', '@sys.date.period', '@sys.fortune.starsign'],
    ]
    value = [
        ['오늘', '1월 1일', '1일'],
        ['이번주', '올해', '사수자리'],
    ]
    start_idx =[
        [0, 9, 12],
        [0, 15, 4],
    ]
    end_idx = [
        [1, 13, 13],
        [2, 16, 7],
    ]
    tagged_sentence = [
        '@sys.date 뉴스 들려줘@sys.date은 무슨 요일이야',
        '@sys.date.period @sys.fortune.starsign 운세 알려줘@sys.date.period 무슨 해야',
    ]
    i=0
    for sentence in sentences:
        Result = main.priRegex(sentence)
        #print(Result)
        assert Result[0] == entity_name_list[i], True
        assert Result[1] == value[i], True
        assert Result[2] == start_idx[i], True
        assert Result[3] == end_idx[i], True
        assert Result[4] == tagged_sentence[i], True
        i+=1
'''
