# **π¬**QA(Question Answering) λ° TA(Text Analytics) νλ«νΌ κ°λ°, 42MARU


## β¨ νλ‘μ νΈ κΈ°κ° : 2022λ 09μ 4μΌ ~ 2022λ 09μ 23μΌ

## β¨ Team: Cμ‘°

- μν°ν° κ°λ°: λ°μλΉ, μ¬νμ€, μ₯μ§μ°, μ΅νμ
- νμ€νΈ μ½λ μμ±: μ¬νμ€, μ₯μ§μ°, μ΅νμ
- λ λμ€ μ°κ²°, μ¬μ  κ΅¬μΆ : λ°μλΉ

## β¨ ****Description****

ν¬ν°ν¬λ§λ£¨λ μΈμ΄ μΈκ³΅μ§λ₯(AI) κΈ°μ  κΈ°λ°μΌλ‘ λ°©λν λ°μ΄ν° μμμ μ¬μ©μμ μ§μλ₯Ό
μλ―Έμ μΌλ‘ μ΄ν΄νκ³  μ΄μ λ§λ βλ¨ νλμ μ λ΅βμ λμΆν΄λ΄λ QA(Question Answering)
λ° TA(Text Analytics) νλ«νΌμ κ°λ°νλ μΈκ³΅μ§λ₯ μ€ννΈμμλλ€.  

<aside>
π‘ μ°λ¦¬λ **βμΈμμ λͺ¨λ  μ§λ¬Έμ λν λ¨ νλμ μ λ΅μ μ°Ύλ μΌβ**μ νκ³  μμ΅λλ€.

</aside>

μ, λ¨ νλμ μ λ΅μ μ°Ύλ κ²μ΄ μ€μν κΉμ?
μνλ μ λ³΄λ₯Ό μ°ΎκΈ° μν΄ λ΄λΆ μμ€ν λ° ν¬νΈμμ ν€μλ κΈ°λ°μΌλ‘ κ²μνλ©΄ κ²μ ν€μλκ° ν¬ν¨λμ΄ μλ λ¬Έμλ₯Ό λμ΄ν΄μ£Όλ λ°©μμΌλ‘ κ²°κ³Όλ₯Ό μ κ³΅νκΈ° λλ¬Έμ μ§λ¬Έμ λ§λ λ΅μ μ°ΎκΈ° μν΄ λ λ€μ λ¬Έμλ€μ μΌμΌν μ½μ΄λ³΄λ λ±μ μ¬νμ κ³Όμ μ κ²ͺκ³ μμ΅λλ€. 

μ κ³Όμ μ Search(κ²μ)λΌκ³  νλ€λ©΄, μ°λ¦¬λ κ²μμ λμ΄ μ λ΅μ μ°Ύλ QA(Question Answering)μ
μ§νλ μλ΅ μλ£¨μμ ν΅ν΄ λ¬Έμλ₯Ό μ΄ν΄νκ³  μνλ μ λ³΄λ₯Ό κΌ­ μ§μ΄μ νλμ μ λ΅μ μ κ³΅ν©λλ€. 

## β¨ **assignment**

> μμ€νμ λ±λ‘λ κ°μ²΄λͺμ νΉμ  λ¬Έμ₯μμ μΆμΆνλ python module κ°λ°
> 

## β¨Β ****Development Environment & Language****
<div align=center> 
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=Redis&logoColor=white">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">
    <br>
</div>

## β¨Β ****Detail****

## 1. μ κ·ννμ

- κ³Όμ  λͺ©ν : νΉμ  λ¬Έμ₯μμ **μν°ν°λͺ λ° κ·Έμ κ΄λ ¨λ μ¬λ¬ μ λ³΄λ€μ μΆμΆ**νλ python module κ°λ°
- μ κ·ννμ νμ© : μν°ν°λͺμ ν΄λΉνλ μ κ·ννμμ μμ±ν΄ μν°ν°λͺ μ λ¬΄λ₯Ό νλ³νκ³  κ·Έμ κ΄λ ¨λ μ λ³΄λ₯Ό ν λ²μ μΆμΆνκ³ μ ν¨.

---

### μ κ· ννμ μμ± λ°©λ²

1. re λͺ¨λ νμ©
νμ΄μ¬μμ μ κ· ννμμ μ§μνκΈ° μν΄ μ κ³΅νλ re λͺ¨λμ νμ©νλ€.

```
import re

text = input()

```

1. finditer λ©μλ μ΄μ©
μ κ·μκ³Ό λ§€μΉλλ μ¬λ¬ λ¬Έμμ΄μ μΆμΆνκΈ° μν΄ finditer λ©μλλ₯Ό μ¬μ©νλ€. μ΄λ κ²°κ³Όκ°μΌλ‘ λ°λ³΅ κ°λ₯ν κ°μ²΄λ‘ λλ €μ£Όκ³  μ΄μ λν μμΈν κ°μ λ³΄κ³  μΆλ€λ©΄ forλ¬Έμ νμ©ν΄μΌ νλ€. λν match κ°μ²΄λ‘ λλ €μ£ΌκΈ° λλ¬Έμ match κ°μ²΄μ λ©μλλ₯Ό νμ©ν΄ startIndex(μμμΈλ±μ€), endIndex(λ§μ§λ§μΈλ±μ€), group(μΌμΉνλ κ°)μ μ μ μλ€.

```
 m = v.finditer(text)
        for i in m:
            tagged_sentence = tagged_sentence.replace((text[i.start():i.end()]), k)

            entitiy_name_list.append(k)
            value.append(i.group())
            start_idx.append(i.start())
            end_idx.append(i.end()-1)

```

- re.VERBOSE νμ©
μ κ·μμ μμ±νλ€λ³΄λ λ§€μ° κΈΈμ΄μ Έμ κ°λμ±μ΄ λ¨μ΄μ§λ λ¬Έμ μ μ΄ λ°μνλ€. κΈΈμ΄κ° κΈ΄ μ κ·μμ μ€ λ¨μλ‘ κ΅¬λΆνκΈ° μν΄μ re.VERBOSE νμ©νλ€.

```
date = re.compile(r"""
                (μ€λ|λ΄μΌ|μ΄μ |κΈμΌ) #μ€λ
                |(\\d+λ\\s\\d+μ\\s\\d+μΌ) #λ μ§
                |(\\d+μ\\s\\d+μΌ) #μ
                |([γ±-γ£κ°-ν£]μμΌ)#μμΌ
                """, re.VERBOSE)

```

## 2. λ λμ€ μ¬μ  κ΅¬μΆ

κ΅­κ°λͺ, κ΅­λ΄ μ§λͺ, ν΄μΈ μ£Ό μ΄λ¦, ν΄μΈ λμλͺ, ν΄μΈ ν΅νλͺκ³Ό κ°μ΄ μ½λ λ΄μμ μ§μ  μ κ·μμΌλ‘ μμ±νκΈ° νλ  κ°μ²΄λͺλ€μ λ λμ€λ₯Ό νμ©νμ¬ μ¬μ μ κ΅¬μΆν λ€ μ κ·μμΌλ‘ λ³ν

1. μ¬μ  κ΅¬μΆ
    1. csv νμμ μ€ν λ°μ΄ν° μ νλ³΄
    2. νμν λ°μ΄ν°λ₯Ό λ λμ€μ μ μ₯ν  μ μλ νμμΌλ‘ λ³ν
    3. λ λμ€ λ°μ΄ν°λ² μ΄μ€μ μ μ₯
    
    ```
    # μμ - κ΅­κ°λͺ
    nation = []
    with open('nation_code.csv') as csvfile:
        next(csvfile)
        read = csv.reader(csvfile)
        for row in read:
            nation.append(row[7])
    nation = " ".join(nation)
    
    rd.set("nation", nation) # κ° μ μ₯
    
    ```
    
2. μ κ·μ λ³ν
    
    λ λμ€μ μ μ₯λ κ°λ€μ λΆλ¬μ μ κ·μμΌλ‘ κ°κ³΅
    
    ```
    # μμ - nation
    nation = rd.get("nation")
    
    nation = nation.split(' ')
    re_nation = nation[0]
    for i in range(1, len(nation)):
        re_nation = re_nation + "|" + nation[i]
    
    ```
    
    ```
    # μ κ·μμΌλ‘ λ³νλ νμ€νΈμ μΌλΆ
    κ°λ|κ°λ΄|κ°μ΄μλ|κ°λΉμ|κ³Όνλ§λΌ|κ·Έλ λλ€|κ·Έλ¦¬μ€|κΈ°λ|κΈ°λλΉμ¬μ°|λλ―ΈλΉμ ...
    
    ```
    
3. main.pyμμ μ¬μ©
    
    κ°κ³΅λ κ°λ€μ main.pyμμ λΆλ¬μ λ€λ₯Έ μ κ·μλ€κ³Ό λμΌν λ°©μμΌλ‘ μ¬μ©
    
    ```
    ...
          '@sys.location' : location,
        '@sys.nation' : nation,
        '@sys.state' : state,
        '@sys.city' : city,
        '@sys.currencyname' : currencyname,
    ...
    
    ```
    

### μ€ν κ²°κ³Ό

```
μ€λ κ°λ λ μ¨ μ΄λ?
entitiy name = @sys.date
value =  μ€λ
start_idx =  0
end_idx =  1
----
entitiy name = @sys.nation
value =  κ°λ
start_idx =  3
end_idx =  4
----
@sys.date @sys.nation λ μ¨ μ΄λ?

```

## 3. λ©μΈ ν¨μ μμ±

- *μν°ν°, μ κ·μ λμλλ¦¬. **

μμμ μμ±ν μ κ·μλ€κ³Ό, κ° μν°ν° μ΄λ¦μ λμλλ¦¬ ννλ‘ μ μ₯ν©λλ€. λμλλ¦¬μ μ ν μμλ‘ μ κ·ννμμ μ€νν  μμ μ΄κΈ°μ, μ°μ μμλ₯Ό μ κ²½μ¨μ λ°°μΉν¨

```
```python
# μμ
regexes = {
'@sys.date.lunar': date_lunar,
'@sys.date.period.lunars': date_period_lunar,
'@sys.date' : date,
'@sys.date.period' : date_period,
'@sys.date.lunar' : date_lunar,
'@sys.date.period.lunars' : date_period_lunar,
```

```

### Regexν¨μ

**Regex ν¨μμ κ°λ¨ν μλ λ°©μ**

1. regexes λμλλ¦¬λ₯Ό forλ¬Έμ λλ©΄μ, μν°ν°μ ν΄λΉνλ μ κ·ννμμ finditer λ©μλ μ¬μ©
2. μ΅μ₯ μν°ν° νμΈ
3. date μν°ν° νμ λ³ν
4. outputκ° μ μ₯, tagged_sentenceλ λμ ν΄μ μμ 

### μ΅μ₯ μν°ν° νλ³ λ°©μ

1. κ° μν°ν° valueμ start_idxκ° κ²ΉμΉλ νλ³. λ§μ½ κ²ΉμΉλ κ²½μ°end_idxκ° λ κΈ΄ κ° μ±ν
    
    ```
    β¦
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
    β¦
    
    ```
    
    1. κΈ΄ λ¨μ΄ μ€κ°μ valueκ°μ΄ μ‘΄μ¬νλ κ²½μ°.
    *ex) '2022λ3μ23μΌ'λΌλ μν°ν° valueμμ '3μ'μ΄ μ€λ³΅μΌλ‘ νμ*
    μ΄μ μ μΆμΆλ valueκ° μ€ start_idxκ° λ μκ³ , end_idxλ κΈ΄ λ¨μ΄κ° μλμ§ νλ³
    
    ```
    β¦
       for j in range(len(start_idx)): #μ€κ°μ κ»΄μλ κ²½μ°
                s_idx = int(start_idx[j])
                e_idx = int(end_idx[j])
                if s_idx <i.start() and e_idx > i.end()-1:
                    flag = 1
    β¦
    
    ```
    
    1. μ λκ°μ§μ μνμ§ μμΌλ©΄ flagκ°μ 0
    λ°λΌμ ν΄λΉ κ²½μ°λ μ€λ³΅λμ§ μλ μλ‘μ΄ μν°ν° κ°μ μΆμΆν κ²μΌλ‘ νλ¨νκ³  entity_name, value, start_idx, end_idx, tagged_sentenceλ₯Ό μ μ₯

### date μν°ν° νμ λ³ν

date νμμ 2022λ 09μ 23μΌ 00:00:00μ νμμΌλ‘ λ°ν

1. μν°ν°κ° sys.dateμΈ κ²½μ° μ€ λ/μ/μΌ νμ νμΈ
2. ν΄λΉ κ²½μ°, 'λ'μ '-'λ‘ λ³ν
3. '3'μ/μΌκ³Ό κ°μ 1μλ¦¬ μ μ«μ νλ³ ν '03'μΌλ‘ ν¬λ§·ν ν λ³ν

### Returnκ°

entity_name, value, start_idx, end_idx, tagged_sentenceμ μ μ₯λμ΄ μλ λ°μ΄ν°λ€μ νλμ resultλ¦¬μ€νΈλ‘ λ³νν΄ λ°ν

```
#input = μ΄λ²μ£Ό μ¬μμλ¦¬ μ΄μΈ μλ €μ€μ¬ν΄ λ¬΄μ¨ ν΄μΌ
#returnκ°
[['@sys.date.period', '@sys.date.period', '@sys.fortune.starsign'], ['μ΄λ²μ£Ό', 'μ¬ν΄', 'μ¬μμλ¦¬'], ['0', '15', '4'], ['2', '16', '7'], '@sys.date.period @sys.fortune.starsign μ΄μΈ μλ €μ€@sys.date.period λ¬΄μ¨ ν΄μΌ']

## 4. νμ€νΈμ½λ μμ±

* pythonμ νμ€νΈμ½λ κ²μ¦ λͺ¨λ `pytest` νμ©ν¨.
* μ λνμ€νΈ
ν¨μ,ν΄λμ€ λ±μ 'unit'μ΄ μνλ κ²°κ³Όκ°μ λ¦¬ν΄νλμ§
νμΈνλ νμ

### 4.1 Pytest
* pytestλ test_μ λμ΄λ₯Ό μ λνμ€νΈ λμ νμΌ/ν¨μλ‘ μΈμν¨.

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
μ μ½λμ test_μ λμ΄κ° λΆμ ν¨μλ₯Ό μ μνκ³ 
`assertλ¬Έ`μ ν΅ν΄ test Pass/Failμ κ²μ¦νλ€.

### 4.2 pytest μ€νλͺλ Ήμ΄
* pytest [-v,-s : μ΅μ] [μ€ννμΌλͺ]<br> \-v: verbose, κ²°κ³Όλ₯Ό μμΈν μΆλ ₯<br> \-s: κ²μ¦κ²°κ³Όμ printλ¬Έ μΆλ ₯ 
* pytest test_math_func.py::test_add <br> νΉμ  νμΌμ νΉμ  ν¨μλ§ κ²μ¦μ΄ κ°λ₯ν¨.
* pytest -v -k "add or string" <br>\-k: ν¨μλͺκ²μμ΅μ, add λλ stringμ΄ λ€μ΄κ° ν¨μλ₯Ό κ²μ¦ μ€νν¨.
* pytest -v -m number <br>\-m:@pytest.mark.number 'number'λ‘ λ§νΉλ ν¨μλ₯Ό `pytest -m number`λ‘ κ²μ¦κ°λ₯ν¨.

### 4.3 νμ€νΈμ½λ

```python
def test_file():
    entity_name_list =[]
    value_list = []
    start_idx_list =[]
    end_idx_list =[]
    tagged_sentence = []
    Result =[]

    f = open("testsentence.txt", 'r') #νμ€νΈ νμΌ λΆλ¬μ€κΈ°
    lines = f.readlines() #ν μ€μ© μ½μ΄μ lines λ¦¬μ€νΈμ μ μ₯
    for i in range(len(lines)): #linesλ¦¬μ€νΈ λκΈ°
        lines[i] = lines[i].strip() #\nμ κ±°
        if re.match(r'input\s:\s', lines[i]): #inputμΈ κ²½μ°
            input = re.sub(r'input\s:\s', '', lines[i]) #inputμ§μμ£Όκ³ , input λ¬Έμ₯λ§ λ³μμ μ μ₯
        elif re.match(r'entity_name\s:\s', lines[i]): #entity nameμΈ κ²½μ°
            entity_name = re.sub(r'entity_name\s:\s', '', lines[i]) #entity nameμ§μμ£Όκ³ 
            entity_name_list = entity_name.split(',') #μν°ν° μ΄λ¦ ,κΈ°μ€μΌλ‘ λλ μ λ¦¬μ€νΈμ μ μ₯
        elif re.match(r'value\s:\s', lines[i]): #λμΌν λ°©μ
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
            Result = [entity_name_list, value_list, start_idx_list, end_idx_list, tagged_sentence] #ν λ¬Έμ₯μ outputκ²°κ³Ό Resultμ μ μ₯
            assert Result == Regex(input) 
```
μ€λͺ) main.pyμ Regex(input)λ₯Ό νΈμΆν΄ λ¦¬ν΄λ°μ κ°κ³Ό testsentence.txt νμΌμ μμ Ouputκ°μ μ μ²λ¦¬ν Resultκ°μ assert Result == Regex(input) μ ν΅ν΄ κ²μ¦νλ€.

