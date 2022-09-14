import sys_date_period_lunar

def test_sys_date_period_lunar():
    assert sys_date_period_lunar("정월 보름은 음력 1월을 말합니다") is True
    assert sys_date_period_lunar("올해 무슨 해야") is True