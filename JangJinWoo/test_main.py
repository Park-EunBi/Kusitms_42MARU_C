import pytest
from JangJinWoo.sys.date import date

def test_selectDate_validator():
    assert date.selectDate('오늘 뉴스 들려줘1월 1일은 무슨 요일이야') is 'a'



