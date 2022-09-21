import re

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


time=re.compile(r'(정오)?(오전)?((\d+분|\d+시|\d+초)\s+뒤?)?')
time_period=re.compile(r'((오전|오후)?)*\s?((아침|점심|저녁)?)*\s?((\d+시부터\s?\d+시까지)?)*')
date_time=re.compile(r'(내일|현재|오늘|모레|(\d+월\s?\d일))?\s((오전|오후)?\s?((\d+시)?\s?(\d+분)?))?')
date_time_period=re.compile(r'(([월화수목금토일]요일)|오늘|내일|모레|글피|어[제|젯]|(\d+월\s?\d일))?\s?((낮|밤|저녁|오전|오후)?)*\s?((아침|점심|저녁)?)*\s?((\d+시부터\s?\d+시까지)?)*')
number=re.compile(r'((일|이|삼|사|오|육|칠|팔|구|십)?|(하나|둘|셋|넷|다섯|여섯|일곱|여덟|아홉)?)*(((\d+)(명|개))?((하나|둘|셋|넷|다섯|여섯|일곱|여덟|아홉)\s?(명|개))?)*(열명|열개)?')
number_times=re.compile(r'(\d+(화|부|편|차|회|회차))*')
number_percent=re.compile(r'(\d+(퍼센트|프로|%))*')

number_ordinal = re.compile('(\d+번)|(첫?두?세?네?(열|(스[무|물])|(서른)|(마흔)|(쉰)|(예순)|(일흔)|(여든)|(아흔))?\s?[한두세네]?(다섯)?(여섯)?(일곱)?(여덟)?(아홉)?\s?번째)')
number_age = re.compile('(\d+[살세])|(((열)?(스[무물])?(서른)?(마흔)?(쉰)?(예순)?(일흔)?(여든)?(아흔)?)\s?([한두세네]*(다섯)?(여섯)?(일곱)?(여덟)?(아홉)?)\s?살)')
number_birthyear = re.compile('\d{1,4}년생')
number_rank = re.compile('\d+[등위]')
unit_duration = re.compile('(\d+(일|(주일)|(개월)|년)(\s?(동안))?)|(하루|이틀)|(([이|삼|사|오|육|칠|팔|구]십\s?)?[일|이|삼|사|오|육|칠|팔|구](일|(주일)|(개월)|년))|(\d+(시간)?\s?(\d+|반)?분?\s?\d*초?\s?동안)|(\d+(시간)?\s?(\d+|반)?분?\s?\d*초?\s?)')
number_decade = re.compile('\d{1,4}년대')
unit_length = re.compile('\d+\.?\d*\s?((mm|(밀리미터))|((?!cm²)cm|(센티미터))|((?!m²)m|(미터))|((?!km²)km|(킬로미터))|(in|(인치))|((?!ft²)ft|(피트))|((?!yd²)yd|(야드))|(ch|(체인))|(fur|(펄롱))|(mile|(마일)))')
unit_area = re.compile('\d+\.?\d*\s?((m²|(제곱미터))|(a|(아르))|(ha|(헥타르|(헥타아르)))|(km²|(제곱킬로미터))|(ft²|(제곱피트))|(yd²|(제곱야드))|(ac|(에이커))|(평)|(단)|(정))')


#은비
weight1 = r"mg|g|kg|t|kt|gr|oz|lb"
weight2 = r"milligram|gram|kilogram|tonne|metric ton|kiloton|grain|ounce|pound"
weight3 = r"밀리그램|그램|킬로그램|톤|킬로톤|그레인|온스|돈|냥|근|관"
weight4 = r"錢|兩|斤|貫"

volume1 = r"cc|mℓ|ml|dℓ|dl|ℓ|l|cm3|m3|in3|ft3|yd3|gal|gallon|bbl|barrel|fl. oz.|fl|"
volume2 = r"시시|밀리리터|데시리터|리터|세제곱센티미터|세제곱미터|세제곱인치|세제곱피트|" \
          r"세제곱야드|갤런|배럴|액량 온스|홉|되|말|섬"
volume3 = r"cubic centimeter|milliliters|deciliter|liter|cubic centimetre|fluid ounce|" \
          r"gallon|barrel"
volume4 = r"升|斗|苫"

pressure1 = r"atm|Pa|hPa|kPa|MPa|dyne/cm2|mb|bar|kgf/cm2|psi|mmHg|inchHg|mmH2O|inchH2O"
pressure2 = r"기압|파스칼|헥토파스칼|킬로파스칼|메가파스칼|다인/제곱센티미터|밀리바|바|" \
            r"킬로그램힘/제곱센티미터|프사이|수은주밀리미터|수은주인치|수주밀리미터|수주인치"
pressure3 = r"atmospheric pressure|pascal|hectopascal|kilopascal|megapascal|dyne/square centimeters|" \
            r"millibar|kgf/square centimeters|pound per square inch|millimeter of mercury|inch of mercury|" \
            r"millimeter of water|inch of water"

temperature1 = r"°C|°F|K|°R"
temperature2 = r"섭씨온도|화씨온도절대온도|란씨온도"
temperature3 = r"celsius|centigrade|fahrenheit scale|kelvin|rankine"

speed1 = r"m/s|m/h|km/s|km/h|in/s|in/h|ft/s|ft/h|mi/s|mi/h|kn|mach"
speed2 = r"미터 매 초|미터 매 시|킬로미터 매 초|킬로미터 매 시|인치 매 초|인치 매 시|피트 매 초|피트 매 시|" \
         r"마일 매 초|마일 매 시|노트|마하"
speed3 = r"meter per second|meter per hour|kilometer per second|kilometer per hour|inch per second|inch per hour|" \
         r"feet per second|feet per hour|mile per second|mile per hour|knot|mach"

data1 = r"bit|B|KB|KiB|MB|MiB|GB|GiB|TB|TiB|PB|PiB|EB|EiB|ZB|ZiB|YB|YiB"
data2 = r"비트|바이트|킬로바이트|키비바이트|메가바이트|메비바이트|기가바이트|기비바이트|테라바이트|테비바이트|" \
        r"페타바이트|페비바이트|엑사바이트|엑비바이트|제타바이트|제비바이트|요타바이트|요비바이트"
data3 = r"byte|kilobyte|kibibyte|megabyte|mebibyte|gigabyte|gibibyte|terabyte|tebibyte|petabyte|pebibyte|exabyte|" \
        r"exbibyte|zettabyte|zebibyte|yottabyte|yobibyte"

energy1 = r"J|cal|kcal|Wh|kWh|eV|erg"
energy2 = r"줄|칼로리|킬로칼로리|와트시|킬로와트시|마력|에르그|전자볼트"
energy3 = r"electron Volt"


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
    '@sys.unit.duration' : unit_duration,
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

    return value;

#priRegex(text)
