import re

text = input()

date = re.compile('(오늘|내일|어제|금일)|(\d+년 \d+월 \d+일)|(\d+월 \d+일)|([ㄱ-ㅣ가-힣]요일)')
date_period = re.compile(r'(이번[주해월])|(다음[주해월])|(저번[주해월])|(올해|작년|내년|전년|주말|평일|내후년)|((\d+년\s?)(\d+월)?)|((\d+년\s?)(\d+월\s?)?(\d+일\s?)?\s?부터 (\d+년\s?)(\d+월\s?)?(\d+일\s?)?\s?까지)')
date_lunar = re.compile(r'음력\s(\d+년\s?)?(\d+월\s?)?(\d+일\s?)?') #올해 음력/ 음력 설 추가 필요
date_period_lunar = re.compile(r'음력\s\d+월')


regexes = {
    '@sys.date' : date,
    '@sys.date.period' : date_period,
    '@sys.date.lunar' : date_lunar,
    '@sys.date.period.lunars' : date_period_lunar,
}

def Regex(text):
    #전체 엔티티
    for k, v in list(regexes.items()):
        m = v.finditer(text)
        for i in m:
            tagged_sentence = text.replace((text[i.start():i.end()]), k)

            #하나씩 출력
            print(f'entity name : {k}\n'
                  f'value : {i.group()}\n'
                  f'start_idx : {i.start()}\n'
                  f'end_idx : {i.end()}\n'
                  f'tagged_sentence : {tagged_sentence}\n')

Regex(text)
'''
tagged_sentence = text
entitiy_list = []

for k, v in list(regexes.items()):
    m = v.finditer(text)
    if m is not None:
        entitiy_list.append(k)
    for i in m:
        tagged_sentence = tagged_sentence.replace((text[i.start():i.end()]), k)
    #value랑 start,end는 하나씩 출력해야하는데..? 음..?
    
    
def is_valid_date(text):
    m = date.match(text)
'''

