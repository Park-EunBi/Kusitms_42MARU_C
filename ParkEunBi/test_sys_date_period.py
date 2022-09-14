import sys_date_period

def test_sys_date_period():
    assert sys_date_period("이번주 사수자리 운세 알려줘") is True
    assert sys_date_period("2020년 3일전부터 내일까지 날씨 알려줘") is True
    assert sys_date_period("올해 무슨 해야") is True