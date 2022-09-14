import sys_date
import sys

def test_sys_date() :
    assert sys_date("오늘 뉴스 들려줘 2022년 10월 1일은 무슨 요일이야") is True
    assert sys_date("이번주 사수자리 운세 알려줘") is True
    assert sys_date("올해 무슨 해야") is True