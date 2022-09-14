import sys_date_lunar

def test_sys_date_lunar():
    assert sys_date_lunar("음력 1월1일") is True
    assert sys_date_lunar("음력 2019년 5월 5일") is True
    assert sys_date_lunar("올해 음력 5월 16일") is True
    assert sys_date_lunar("음력 설") is True