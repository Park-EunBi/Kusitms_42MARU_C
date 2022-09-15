import re

text = input()

date = re.compile('(오늘|내일|어제|금일)|(\d+년 \d+월 \d+일)|(\d+월 \d+일)|([ㄱ-ㅣ가-힣]요일)')
date_period = re.compile(r'(이번[주해월])|(다음[주해월])|(저번[주해월])|(올해|작년|내년|전년|주말|평일|내후년)|((\d+년\s?)(\d+월)?)|((\d+년\s?)(\d+월\s?)?(\d+일\s?)?\s?부터 (\d+년\s?)(\d+월\s?)?(\d+일\s?)?\s?까지)')
date_lunar = re.compile(r'음력\s(\d+년\s?)?(\d+월\s?)?(\d+일\s?)?') #올해 음력/ 음력 설 추가 필요
date_period_lunar = re.compile(r'음력\s\d+월')


fortune_starsign = re.compile('[ㄱ-ㅣ가-힣]+자리')
fortune_zodiac = re.compile('[ㄱ-ㅣ가-힣]+띠') #뱀ㅁ띠 -> 이런것도 인식되는데 바꿔야하나?
currencyname = re.compile('([ㄱ-ㅣ가-힣]+달러)|(엔|유로|위안)') #명칭 엄청 다양하게 많음. 사전사용?
currency_code = re.compile('[A-Z]{3}')
url = re.compile('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')
bussiness_number = re.compile('[0-9]{3}-[0-9]{2}-[0-9]{5}]')
phone_number = re.compile('01[016789]-[0-9]{4}-[0-9]{4}]')
licenseplate_number = re.compile('[0-9]{2,3}\s[ㄱ-ㅣ가-힣][0-9]{4}')

regexes = {
    '@sys.date' : date,
    '@sys.date.period' : date_period,
    '@sys.date.lunar' : date_lunar,
    '@sys.date.period.lunars' : date_period_lunar,
    '@sys.fortune.starsign' : fortune_starsign,
    '@sys.fortune.zodiac' : fortune_zodiac,
    '@sys.currencyname' : currencyname,
    '@sys.currency.code' : currency_code,
    '@sys.url' : url,
    '@sys.bussiness.number' : bussiness_number,
    '@sys.phone.number' : phone_number,
    '@sys.licenseplate.number' : licenseplate_number,

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

