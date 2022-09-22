import redis
import csv

# set_redis 에 정보 저장
rd = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)


## 국가명
nation = []
with open('nation_code.csv') as csvfile:
    next(csvfile)
    read = csv.reader(csvfile)
    for row in read:
        nation.append(row[7])
# nation.remove("한글명")
nation = " ".join(nation)

rd.set("nation", nation) # 값 저장


## 국내 지역
location = []
si_do = []
si_gun_gu = []
eup_myeon_dong = []
ri = []
with open('location.csv') as csvfile:
    next(csvfile)
    read = csv.reader(csvfile)
    for row in read:
        si_do.append(row[1])
        si_gun_gu.append(row[2])
        eup_myeon_dong.append(row[3])
        ri.append(row[4])

si_do = list(set(si_do))
si_gun_gu = list(set(si_gun_gu))
eup_myeon_dong = list(set(eup_myeon_dong))
ri = list(set(ri))

## 빈 문자열 제거
si_gun_gu = ' '.join(si_gun_gu).split()
eup_myeon_dong = ' '.join(eup_myeon_dong).split()
ri = ' '.join(ri).split()

location = si_do + si_gun_gu + eup_myeon_dong + ri
location = " ".join(location)

rd.set("location", location) # 값 저장


## 주 이름
states = []
with open('states.csv') as csvfile:
    next(csvfile)
    read = csv.reader(csvfile)
    for row in read:
        states.append(row[0])
        states.append(row[2])
states = " ".join(states)
rd.set("states", states) # 값 저장


## 해외 도시명
city = []
with open('city.csv') as csvfile:
    next(csvfile)
    read = csv.reader(csvfile)
    for row in read:
        city.append(row[2])
city = set(city)
city = " ".join(city)
rd.set("city", city) # 값 저장


## 통화명
currencyname = []
with open('currencyname.csv') as csvfile:
    next(csvfile)
    read = csv.reader(csvfile)
    for row in read:
        currencyname.append(row[2])
currencyname = '  '.join(currencyname).split()
currencyname = " ".join(currencyname)
rd.set("currencyname", currencyname) # 값 저장