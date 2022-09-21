from mainJJW import *
import re

def test_number_ordinal():
    text = '플레이리스트 1번 틀어줘네 번째 playlist 재생'
    assert priRegex(text)==['1번', '네 번째', '1']

    text = '1번, 첫 번째, 열 번째, 백 번째'
    assert priRegex(text)==['1번', '첫 번째', '열 번째', ' 번째', '1']

def test_number_age():
    text = '내 아이는 1살입니다스무살에 대학에 입학했어요'
    assert priRegex(text)==['1살', '스무살', '1' ]


