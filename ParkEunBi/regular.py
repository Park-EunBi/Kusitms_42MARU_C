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

currency = r"AED|AFN|ALL|AMD|AOA|ARS|AUD|AWG|AZN|BAM|BBD|BDT|BGN|BHD|BIF|BMD|BND|BOB|BRL|BSD|" \
           r"BTN|BWP|BYN|BZD|CAD|CDF|CLP|CNY|COP|CRC|CUP|CZK||DJF|DKK|DOP|DZD|EGP|ERN|ETB|EUR|" \
           r"FJD|FKP|GBP|GEL|GHS|GIP|GMD|GNF|GTQ|GYD|HKD|HNL|HRK|HTG|HUF|IDR|ILS|INR|IQD|IRR|ISK|" \
           r"JMD|JOD|JPY|KES|KGS|KPW|KRW|KWD|KYD|KZT|LAK|LBP|LKR|LRD|LSL|LYD|MAD|MDL|MGA|MKD|MMK|" \
           r"MNT|MOP|MRU|MUR|MVR|MWK|MXN|MYR|MZN|NAD|NIO|NOK|NPR|NZD|OMR|PAB|PEN|PGK|PHP|PKR|PLN|" \
           r"PYG|QAR|RON|RSD|RUB|RWF|SAR|SBD|SCR|SDG|SEK|SGD|SHP|SLL|SOS|SRD|STN|SYP|SZL|THB|TJS|" \
           r"TMT|TN|TOP|TRY|TTD|TWD|TZS|UAH|UGX|USD|UYU|UZS|VEF|VND|VUV|WST|XAF|XCD|XPF|YER|ZAR|ZMW|ZWL"

weight = weight1 +"|" + weight2 + "|" + weight3 + "|" + weight4
volume = volume1 +"|" + volume2 + "|" + volume3 + "|" + volume4
pressure = pressure1 +"|" + pressure2 + "|" + pressure3
temperature = temperature1 +"|" + temperature2 + "|" + temperature3
speed = speed1 +"|" + speed2 + "|" + speed3
data = data1 +"|" + data2 + "|" + data3
energy = energy1 +"|" + energy2 + "|" + energy3











