import re

text = input()

date = re.compile(r"""
                (오늘|내일|어제|금일) #오늘
                |(\d+년\s\d+월\s\d+일) #날짜
                |(\d+월\s\d+일) #월
                |([ㄱ-ㅣ가-힣]요일)#요일
                """, re.VERBOSE)
date_period = re.compile(r"""
                        (이번[주해월])
                        |(다음[주해월])
                        |(저번[주해월])
                        |(올해|작년|내년|전년|주말|평일|내후년)
                        |((\d+년\s?)(\d+월\s?)?(\d+일\s?)?\s?부터\s(\d+년\s?)(\d+월\s?)?(\d+일\s?)?\s?까지)
                        |((\d+년\s?)(\d+월)?)
                        """, re.VERBOSE)
#date_lunar = re.compile(r'음력\s(\d+년\s?)?(\d+월\s?)?(\d+일\s?)?') #올해 음력/ 음력 설 추가 필요
date_lunar = re.compile(r"""
                        음력\s@sys.date.period #꼼수 쓸려헀는데 망함ㅎ 수정필요
                        | 음력\s@sys.date 
                        | 음력\s(설|추석)
                        """, re.VERBOSE)
date_period_lunar = re.compile(r'음력\s\d+월')


number_ordinal = re.compile('(\d+번)|(첫?두?세?네?(열|(스[무|물])|(서른)|(마흔)|(쉰)|(예순)|(일흔)|(여든)|(아흔))?\s?[한두세네]?(다섯)?(여섯)?(일곱)?(여덟)?(아홉)?\s?번째)')
number_age = re.compile('(\d+[살세])|(((열)?(스[무물])?(서른)?(마흔)?(쉰)?(예순)?(일흔)?(여든)?(아흔)?)\s?([한두세네]*(다섯)?(여섯)?(일곱)?(여덟)?(아홉)?)\s?살)')
number_birthyear = re.compile('\d{1,4}년생')
number_rank = re.compile('\d+[등위]')
number_decade = re.compile('\d{1,4}년대')
unit_length = re.compile('\d+\.?\d*\s?((mm|(밀리미터))|((?!cm²)cm|(센티미터))|((?!m²)m|(미터))|((?!km²)km|(킬로미터))|(in|(인치))|((?!ft²)ft|(피트))|((?!yd²)yd|(야드))|(ch|(체인))|(fur|(펄롱))|(mile|(마일)))')
unit_area = re.compile('\d+\.?\d*\s?((m²|(제곱미터))|(a|(아르))|(ha|(헥타르|(헥타아르)))|(km²|(제곱킬로미터))|(ft²|(제곱피트))|(yd²|(제곱야드))|(ac|(에이커))|(평)|(단)|(정))')


fortune_starsign = re.compile('[ㄱ-ㅣ가-힣]+자리')
fortune_zodiac = re.compile('[ㄱ-ㅣ가-힣]+띠') #뱀ㅁ띠 -> 이런것도 인식되는데 바꿔야하나?
currencyname = re.compile(r"""
                          ([ㄱ-ㅣ가-힣]+달러)
                          |(엔|유로|위안|파운드)
                          |([ㄱ-ㅣ가-힣]+페소)
                          |([ㄱ-ㅣ가-힣]+실링)
                          """, re.VERBOSE)
currency_code = re.compile('[A-Z]{3}')
url = re.compile('(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?')
bussiness_number = re.compile('[0-9]{3}-[0-9]{2}-[0-9]{5}]')
phone_number = re.compile('01[0|1|6|7|8|9?]-?[0-9]{4}-?[0-9]{4}')
licenseplate_number = re.compile('[0-9]{2,3}\s[ㄱ-ㅣ가-힣][0-9]{4}')

regexes = {
    #최장 내용으로 대치하는 부분이 이 우선순위로 처리가 가능한가? 불가능하다면 다른 방안 고민..

    '@sys.date' : date,
    '@sys.date.period' : date_period,
    '@sys.date.lunar' : date_lunar,
    '@sys.date.period.lunars' : date_period_lunar,
    '@sys.number.ordinal': number_ordinal,
    '@sys.number.age': number_age,
    '@sys.number.birthyear': number_birthyear,
    '@sys.number.rank': number_rank,
    '@sys.number.decade': number_decade,
    '@sys.unit.length': unit_length,
    '@sys.unit.area': unit_area,
    '@sys.fortune.starsign' : fortune_starsign,
    '@sys.fortune.zodiac' : fortune_zodiac,
    '@sys.currencyname' : currencyname,
    '@sys.currency.code' : currency_code,
    '@sys.url' : url,
    '@sys.bussiness.number' : bussiness_number,
    '@sys.phone.number' : phone_number,
    '@sys.licenseplate.number' : licenseplate_number,

}

def priRegex(text):
    tagged_sentence = text
    entitiy_name_list = []
    value = []
    start_idx = []
    end_idx = []

    for k, v in list(regexes.items()):

        m = v.finditer(text)
        for i in m:
            tagged_sentence = tagged_sentence.replace((text[i.start():i.end()]), k)

            entitiy_name_list.append(k)  # entitiy name에 추가
            value.append(i.group()) #date value 수정 필요
            start_idx.append(i.start())
            end_idx.append(i.end()-1)


    for i in range(len(entitiy_name_list)):
        print('entitiy name =', entitiy_name_list[i])
        print('value = ', value[i])
        print('start_idx = ',start_idx[i])
        print('end_idx = ',end_idx[i])
        print('----')

priRegex(text)
