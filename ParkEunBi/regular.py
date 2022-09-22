import set_redis_eunbi
import redis
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

currency = r"\d+원|\d+달러|\d+위안|\d+센트|\d+파운드|\d+엔|\d+유로|\d+프랑|\d+루피" \
           r"\S+원|\S+달러|\S+위안|\S+센트|\S+파운드|\S+엔|\S+유로|\S+프랑|\S+루피"

weight = weight1 +"|" + weight2 + "|" + weight3 + "|" + weight4
volume = volume1 +"|" + volume2 + "|" + volume3 + "|" + volume4
pressure = pressure1 +"|" + pressure2 + "|" + pressure3
temperature = temperature1 +"|" + temperature2 + "|" + temperature3
speed = speed1 +"|" + speed2 + "|" + speed3
data = data1 +"|" + data2 + "|" + data3
energy = energy1 +"|" + energy2 + "|" + energy3



# Redis에 저장된 값 불러오기, 정규식 변환
rd = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)

# 1. nation
nation = rd.get("nation")
# str 형식으로 받아와서
# 정규식으로 변형하려면 list 로 변경해야 한다
nation = nation.split(' ')
re_nation = nation[0]
for i in range(1, len(nation)):
    re_nation = re_nation + "|" + nation[i]

# 2. location - 국내 지역
location = rd.get("location")
location = location.split(' ')
re_location = location[0]
for i in range(1, len(location)):
    re_location = re_location + "|" + location[i]

# 3. state - 해외 주 단위
states = rd.get("states")
states = states.split(' ')
re_states = states[0]
for i in range(1, len(states)):
    re_states = re_states + "|" + states[i-1]

# 4. city - 해외 도시명
city = rd.get("city")
city = city.split(' ')
re_city = city[0]
for i in range(1, len(city)):
    re_city = re_city + "|" + city[i]

# 5.  currencyname - 통화명 (달러, 엔화 등등)
currencyname = rd.get("currencyname")
currencyname = currencyname.split(' ')
re_currencyname = currencyname[0]
for i in range(1, len(currencyname)):
    re_currencyname = "\d+\s?" + re_currencyname + "|" + currencyname[i]








