# **💬**QA(Question Answering) 및 TA(Text Analytics) 플랫폼 개발, 42MARU


## ✨ 프로젝트 기간 : 2022년 09월 4일 ~ 2022년 09월 23일

## ✨ Team: C조

- 엔티티 개발: 박은비, 심현준, 장진우, 최혜영
- 테스트 코드 작성: 심현준, 장진우, 최혜영
- 레디스 연결, 사전 구축 : 박은비

## ✨ ****Description****

포티투마루는 언어 인공지능(AI) 기술 기반으로 방대한 데이터 속에서 사용자의 질의를
의미적으로 이해하고 이에 맞는 ‘단 하나의 정답’을 도출해내는 QA(Question Answering)
및 TA(Text Analytics) 플랫폼을 개발하는 인공지능 스타트업입니다.  

<aside>
💡 우리는 **“세상의 모든 질문에 대한 단 하나의 정답을 찾는 일”**을 하고 있습니다.

</aside>

왜, 단 하나의 정답을 찾는 것이 중요할까요?
원하는 정보를 찾기 위해 내부 시스템 및 포털에서 키워드 기반으로 검색하면 검색 키워드가 포함되어 있는 문서를 나열해주는 방식으로 결과를 제공하기 때문에 질문에 맞는 답을 찾기 위해 또 다시 문서들을 일일히 읽어보는 등의 재탐색 과정을 겪고있습니다. 

위 과정을 Search(검색)라고 한다면, 우리는 검색을 넘어 정답을 찾는 QA(Question Answering)의
진화된 응답 솔루션을 통해 문서를 이해하고 원하는 정보를 꼭 집어서 하나의 정답을 제공합니다. 

## ✨ **assignment**

> 시스템에 등록된 개체명을 특정 문장에서 추출하는 python module 개발
> 

## ✨ ****Development Environment & Language****
<div align=center> 
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=Redis&logoColor=white">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
    <br>
</div>

## ✨ ****Detail****

## 1. 정규표현식

- 과제 목표 : 특정 문장에서 **엔티티명 및 그와 관련된 여러 정보들을 추출**하는 python module 개발
- 정규표현식 활용 : 엔티티명에 해당하는 정규표현식을 작성해 엔티티명 유무를 판별하고 그와 관련된 정보를 한 번에 추출하고자 함.

---

### 정규 표현식 작성 방법

1. re 모듈 활용
파이썬에서 정규 표현식을 지원하기 위해 제공하는 re 모듈을 활용한다.

```
import re

text = input()

```

1. finditer 메소드 이용
정규식과 매치되는 여러 문자열을 추출하기 위해 finditer 메소드를 사용했다. 이는 결과값으로 반복 가능한 객체로 돌려주고 이에 대한 상세한 값을 보고 싶다면 for문을 활용해야 한다. 또한 match 객체로 돌려주기 때문에 match 객체의 메서드를 활용해 startIndex(시작인덱스), endIndex(마지막인덱스), group(일치하는 값)을 알 수 있다.

```
 m = v.finditer(text)
        for i in m:
            tagged_sentence = tagged_sentence.replace((text[i.start():i.end()]), k)

            entitiy_name_list.append(k)
            value.append(i.group())
            start_idx.append(i.start())
            end_idx.append(i.end()-1)

```

- re.VERBOSE 활용
정규식을 작성하다보니 매우 길어져서 가독성이 떨어지는 문제점이 발생했다. 길이가 긴 정규식을 줄 단위로 구분하기 위해서 re.VERBOSE 활용했다.

```
date = re.compile(r"""
                (오늘|내일|어제|금일) #오늘
                |(\\d+년\\s\\d+월\\s\\d+일) #날짜
                |(\\d+월\\s\\d+일) #월
                |([ㄱ-ㅣ가-힣]요일)#요일
                """, re.VERBOSE)

```

## 2. 레디스 사전 구축

국가명, 국내 지명, 해외 주 이름, 해외 도시명, 해외 통화명과 같이 코드 내에서 직접 정규식으로 작성하기 힘든 개체명들은 레디스를 활용하여 사전을 구축한 뒤 정규식으로 변환

1. 사전 구축
    1. csv 형식의 오픈 데이터 셋 확보
    2. 필요한 데이터를 레디스에 저장할 수 있는 형식으로 변환
    3. 레디스 데이터베이스에 저장
    
    ```
    # 예시 - 국가명
    nation = []
    with open('nation_code.csv') as csvfile:
        next(csvfile)
        read = csv.reader(csvfile)
        for row in read:
            nation.append(row[7])
    nation = " ".join(nation)
    
    rd.set("nation", nation) # 값 저장
    
    ```
    
2. 정규식 변환
    
    레디스에 저장된 값들을 불러와 정규식으로 가공
    
    ```
    # 예시 - nation
    nation = rd.get("nation")
    
    nation = nation.split(' ')
    re_nation = nation[0]
    for i in range(1, len(nation)):
        re_nation = re_nation + "|" + nation[i]
    
    ```
    
    ```
    # 정규식으로 변환된 텍스트의 일부
    가나|가봉|가이아나|감비아|과테말라|그레나다|그리스|기니|기니비사우|나미비아 ...
    
    ```
    
3. main.py에서 사용
    
    가공된 값들을 main.py에서 불러와 다른 정규식들과 동일한 방식으로 사용
    
    ```
    ...
          '@sys.location' : location,
        '@sys.nation' : nation,
        '@sys.state' : state,
        '@sys.city' : city,
        '@sys.currencyname' : currencyname,
    ...
    
    ```
    

### 실행 결과

```
오늘 가나 날씨 어때?
entitiy name = @sys.date
value =  오늘
start_idx =  0
end_idx =  1
----
entitiy name = @sys.nation
value =  가나
start_idx =  3
end_idx =  4
----
@sys.date @sys.nation 날씨 어때?

```

## 3. 메인 함수 작성

- *엔티티, 정규식 딕셔너리. **

앞에서 작성한 정규식들과, 각 엔티티 이름을 딕셔너리 형태로 저장합니다. 딕셔너리에 적힌 순서로 정규표현식을 실행할 예정이기에, 우선순위를 신경써서 배치함

```
```python
# 예시
regexes = {
'@sys.date.lunar': date_lunar,
'@sys.date.period.lunars': date_period_lunar,
'@sys.date' : date,
'@sys.date.period' : date_period,
'@sys.date.lunar' : date_lunar,
'@sys.date.period.lunars' : date_period_lunar,
```

```

### Regex함수

**Regex 함수의 간단한 작동 방식**

1. regexes 딕셔너리를 for문을 돌면서, 엔티티에 해당하는 정규표현식을 finditer 메서드 사용
2. 최장 엔티티 확인
3. date 엔티티 형식 변환
4. output값 저장, tagged_sentence는 누적해서 수정

### 최장 엔티티 판별 방식

1. 각 엔티티 value의 start_idx가 겹치는 판별. 만약 겹치는 경우end_idx가 더 긴 값 채택
    
    ```
    …
                if str(i.start()) in start_idx:
                idx = start_idx.index(str(i.start()))
                if int(end_idx[idx]) >= i.end()-1:
                    continue
                tagged_sentence = tagged_sentence.replace(entitiy_name_list[idx], value[idx])
                print(i.group())
                value[idx] = i.group()
                entitiy_name_list[idx] = k
                end_idx[idx] = i.end() - 1
                tagged_sentence = tagged_sentence.replace((text[i.start():i.end()]), k)
                flag = 1
    …
    
    ```
    
    1. 긴 단어 중간에 value값이 존재하는 경우.
    *ex) '2022년3월23일'라는 엔티티 value안에 '3월'이 중복으로 표시*
    이전에 추출된 value값 중 start_idx가 더 작고, end_idx더 긴 단어가 있는지 판별
    
    ```
    …
       for j in range(len(start_idx)): #중간에 껴있는 경우
                s_idx = int(start_idx[j])
                e_idx = int(end_idx[j])
                if s_idx <i.start() and e_idx > i.end()-1:
                    flag = 1
    …
    
    ```
    
    1. 위 두가지에 속하지 않으면 flag값은 0
    따라서 해당 경우는 중복되지 않는 새로운 엔티티 값을 추출한 것으로 판단하고 entity_name, value, start_idx, end_idx, tagged_sentence를 저장

### date 엔티티 형식 변환

date 형식은 2022년 09월 23일 00:00:00시 형식으로 반환

1. 엔티티가 sys.date인 경우 중 년/월/일 형식 확인
2. 해당 경우, '년'을 '-'로 변환
3. '3'월/일과 같은 1자리 수 숫자 판별 후 '03'으로 포맷팅 후 변환

### Return값

entity_name, value, start_idx, end_idx, tagged_sentence에 저장되어 있는 데이터들을 하나의 result리스트로 변환해 반환

```
#input = 이번주 사수자리 운세 알려줘올해 무슨 해야
#return값
[['@sys.date.period', '@sys.date.period', '@sys.fortune.starsign'], ['이번주', '올해', '사수자리'], ['0', '15', '4'], ['2', '16', '7'], '@sys.date.period @sys.fortune.starsign 운세 알려줘@sys.date.period 무슨 해야']

## 4. 테스트코드 작성

* python의 테스트코드 검증 모듈 `pytest` 활용함.
* 유닛테스트
함수,클래스 등의 'unit'이 원하는 결과값을 리턴하는지
확인하는 행위

### 4.1 Pytest
* pytest는 test_접두어를 유닛테스트 대상 파일/함수로 인식함.

```
\# content of test_math_func.py
import math_func

def test_add():
	assert math_func.add(7,3) == 10
	assert math_func.add(7) == 9
	assert math_func.add(5) == 7

def test_product():
	assert math_func.product(5,5) == 25
	assert math_func.product(5) == 10
	assert math_func.product(7) == 14
```
위 코드와 test_접두어가 붙은 함수를 정의하고
`assert문`을 통해 test Pass/Fail을 검증한다.

### 4.2 pytest 실행명령어
* pytest [-v,-s : 옵션] [실행파일명]<br> \-v: verbose, 결과를 자세히 출력<br> \-s: 검증결과에 print문 출력 
* pytest test_math_func.py::test_add <br> 특정 파일의 특정 함수만 검증이 가능함.
* pytest -v -k "add or string" <br>\-k: 함수명검색옵션, add 또는 string이 들어간 함수를 검증 실행함.
* pytest -v -m number <br>\-m:@pytest.mark.number 'number'로 마킹된 함수를 `pytest -m number`로 검증가능함.

### 4.3 테스트코드

```python
def test_file():
    entity_name_list =[]
    value_list = []
    start_idx_list =[]
    end_idx_list =[]
    tagged_sentence = []
    Result =[]

    f = open("testsentence.txt", 'r') #텍스트 파일 불러오기
    lines = f.readlines() #한 줄씩 읽어서 lines 리스트에 저장
    for i in range(len(lines)): #lines리스트 돌기
        lines[i] = lines[i].strip() #\n제거
        if re.match(r'input\s:\s', lines[i]): #input인 경우
            input = re.sub(r'input\s:\s', '', lines[i]) #input지워주고, input 문장만 변수에 저장
        elif re.match(r'entity_name\s:\s', lines[i]): #entity name인 경우
            entity_name = re.sub(r'entity_name\s:\s', '', lines[i]) #entity name지워주고
            entity_name_list = entity_name.split(',') #엔티티 이름 ,기준으로 나눠서 리스트에 저장
        elif re.match(r'value\s:\s', lines[i]): #동일한 방식
            value = re.sub(r'value\s:\s', '', lines[i])
            value_list = value.split(',')
        elif re.match(r'start_idx\s:\s', lines[i]):
            start_idx = re.sub(r'start_idx\s:\s', '', lines[i])
            start_idx_list = start_idx.split(',')
        elif re.match(r'end_idx\s:\s', lines[i]):
            end_idx = re.sub(r'end_idx\s:\s', '', lines[i])
            end_idx_list = end_idx.split(',')
        elif re.match(r'tagged_sentence\s:\s', lines[i]):
            tagged_sentence = re.sub(r'tagged_sentence\s:\s', '', lines[i])
            Result = [entity_name_list, value_list, start_idx_list, end_idx_list, tagged_sentence] #한 문장의 output결과 Result에 저장
            assert Result == Regex(input) 
```
설명) main.py의 Regex(input)를 호출해 리턴받은 값과 testsentence.txt 파일의 예시 Ouput값을 전처리한 Result값을 assert Result == Regex(input) 을 통해 검증한다.

