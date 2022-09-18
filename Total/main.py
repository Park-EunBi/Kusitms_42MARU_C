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
number_decade = re.compile('\d{1,4}년대')
unit_length = re.compile('\d+\.?\d*\s?((mm|(밀리미터))|((?!cm²)cm|(센티미터))|((?!m²)m|(미터))|((?!km²)km|(킬로미터))|(in|(인치))|((?!ft²)ft|(피트))|((?!yd²)yd|(야드))|(ch|(체인))|(fur|(펄롱))|(mile|(마일)))')
unit_area = re.compile('\d+\.?\d*\s?((m²|(제곱미터))|(a|(아르))|(ha|(헥타르|(헥타아르)))|(km²|(제곱킬로미터))|(ft²|(제곱피트))|(yd²|(제곱야드))|(ac|(에이커))|(평)|(단)|(정))')


#은비
weight1 = r"\d+mg|\d+g|\d+kg|\d+t|\d+kt|\d+gr|\d+oz|\d+lb"
weight2 = r"\d+milligram|\d+gram|\d+kilogram|\d+tonne|\d+metric ton|\d+kiloton|\d+grain|\d+ounce|\d+pound"
weight3 = r"\d+밀리그램|\d+그램|\d+킬로그램|\d+톤|\d+킬로톤|\d+그레인|\d+온스|\d+돈|\d+냥|\d+근|\d+관"
weight4 = r"\d+錢|\d+兩|\d+斤|\d+貫"

volume1 = r"\d+cc|\d+mℓ|\d+ml|\d+dℓ|\d+dl|\d+ℓ|\d+l|\d+cm3|\d+m3|\d+in3|\d+ft3|\d+yd3|\d+gal|\d+gallon|\d+bbl|\d+barrel|\d+fl. oz.|\d+fl|"
volume2 = r"\d+시시|\d+밀리리터|\d+데시리터|\d+리터|\d+세제곱센티미터|\d+세제곱미터|\d+세제곱인치|\d+세제곱피트|" \
          r"\d+세제곱야드|\d+갤런|\d+배럴|\d+액량 온스|\d+홉|\d+되|\d+말|\d+섬"
volume3 = r"\d+cubic centimeter|\d+milliliters|\d+deciliter|\d+liter|\d+cubic centimetre|\d+fluid ounce|" \
          r"\d+gallon|\d+barrel"
volume4 = r"\d+升|\d+斗|\d+苫"

pressure1 = r"\d+atm|\d+Pa|\d+hPa|\d+kPa|\d+MPa|\d+dyne/cm2|\d+mb|\d+bar|\d+kgf/cm2|\d+psi|\d+mmHg|\d+inchHg|\d+mmH2O|\d+inchH2O"
pressure2 = r"\d+기압|\d+파스칼|\d+헥토파스칼|\d+킬로파스칼|\d+메가파스칼|\d+다인/제곱센티미터|\d+밀리바|\d+바|" \
            r"\d+킬로그램힘/제곱센티미터|\d+프사이|\d+수은주밀리미터|\d+수은주인치|\d+수주밀리미터|\d+수주인치"
pressure3 = r"\d+atmospheric pressure|\d+pascal|\d+hectopascal|\d+kilopascal|\d+megapascal|\d+dyne/square centimeters|" \
            r"\d+millibar|\d+kgf/square centimeters|\d+pound per square inch|\d+millimeter of mercury|\d+inch of mercury|" \
            r"\d+millimeter of water|\d+inch of water"

temperature1 = r"\d+°C|\d+°F|\d+K|\d+°R"
temperature2 = r"\d+섭씨온도|\d+화씨온도|\d+절대온도|\d+란씨온도|\d+도"
temperature3 = r"\d+celsius|\d+centigrade|\d+fahrenheit scale|\d+kelvin|\d+rankine"

speed1 = r"\d+m/s\d+|m/h|\d+km/s|\d+km/h|\d+in/s|\d+in/h|\d+ft/s|\d+ft/h|\d+mi/s|\d+mi/h|\d+kn|\d+mach"
speed2 = r"\d+미터 매 초|\d+미터 매 시|\d+킬로미터 매 초|\d+킬로미터 매 시|\d+인치 매 초|\d+인치 매 시|\d+피트 매 초|\d+피트 매 시|" \
         r"\d+마일 매 초|\d+마일 매 시|\d+노트|\d+마하"
speed3 = r"\d+meter per second|\d+meter per hour|\d+kilometer per second|\d+kilometer per hour|\d+inch per second|\d+inch per hour|" \
         r"\d+feet per second|\d+feet per hour|\d+mile per second|\d+mile per hour|\d+knot|\d+mach"

data1 = r"\d+it|\d+B|\d+KB|\d+KiB|\d+MB|\d+MiB|\d+GB|\d+GiB|\d+TB|\d+TiB|\d+PB|\d+PiB|\d+EB|\d+EiB|\d+ZB|\d+ZiB|\d+YB|\d+YiB"
data2 = r"\d+비트|\d+바이트|\d+킬로바이트|\d+키비바이트|\d+메가바이트|\d+메비바이트|\d+기가바이트|\d+기비바이트|\d+테라바이트|\d+테비바이트|" \
        r"\d+페타바이트|\d+페비바이트|\d+엑사바이트|\d+엑비바이트|\d+제타바이트|\d+제비바이트|\d+요타바이트|\d+요비바이트"
data3 = r"\d+byte|\d+kilobyte|\d+kibibyte|\d+megabyte|\d+mebibyte|\d+gigabyte|\d+gibibyte|\d+terabyte|\d+tebibyte|\d+petabyte|\d+pebibyte|\d+exabyte|" \
        r"\d+exbibyte|\d+zettabyte|\d+zebibyte|\d+yottabyte|\d+yobibyte"

energy1 = r"\d+J|\d+cal|\d+kcal|\d+Wh|\d+kWh|\d+eV|\d+erg"
energy2 = r"\d+줄|\d+칼로리|\d+킬로칼로리|\d+와트시|\d+킬로와트시|\d+마력|\d+에르그|\d+전자볼트"
energy3 = r"\d+electron Volt"


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
