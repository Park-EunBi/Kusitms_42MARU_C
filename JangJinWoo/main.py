import re


text = input()


date = re.compile('([월화수목금토일]요일)|(오늘|내일|모레|글피|내일모레)|(\d{4}[년-]\s?\d{1,2}[월-]\s?\d{1,2}[일\s]|\d{1,2}월\s?\d{1,2}일|\d{4}년|\d{1,2}월|\d{1,2}일)')
number_ordinal = re.compile('(\d+번)|(첫?두?세?네?(열|(스[무|물])|(서른)|(마흔)|(쉰)|(예순)|(일흔)|(여든)|(아흔))?\s?[한두세네]?(다섯)?(여섯)?(일곱)?(여덟)?(아홉)?\s?번째)')
number_age = re.compile('(\d+[살세])|(((열)?(스[무물])?(서른)?(마흔)?(쉰)?(예순)?(일흔)?(여든)?(아흔)?)\s?([한두세네]*(다섯)?(여섯)?(일곱)?(여덟)?(아홉)?)\s?살)')
number_birthyear = re.compile('\d{1,4}년생')
number_rank = re.compile('\d+[등위]')
number_decade = re.compile('\d{1,4}년대')
unit_length = re.compile('\d+\.?\d*\s?((mm|(밀리미터))|((?!cm²)cm|(센티미터))|((?!m²)m|(미터))|((?!km²)km|(킬로미터))|(in|(인치))|((?!ft²)ft|(피트))|((?!yd²)yd|(야드))|(ch|(체인))|(fur|(펄롱))|(mile|(마일)))')
unit_area = re.compile('\d+\.?\d*\s?((m²|(제곱미터))|(a|(아르))|(ha|(헥타르|(헥타아르)))|(km²|(제곱킬로미터))|(ft²|(제곱피트))|(yd²|(제곱야드))|(ac|(에이커))|(평)|(단)|(정))')
unit_duration = re.compile('(\d+(시간)?\s?(\d*|반)분?\s?\d*초?\s?동안)')
regexes = {
    '@sys.date' : date,
    '@sys.number.ordinal' : number_ordinal,
    '@sys.number.age' : number_age,
    '@sys.number.birthyear' : number_birthyear,
    '@sys.number.rank' : number_rank,
    '@sys.number.decade' : number_decade,
    '@sys.unit.length' : unit_length,
    '@sys.unit.area' : unit_area
}


def Regex(test):
    tagged_sentence = text

    for k, v in list(regexes.items()): #k : key, v:value
        m = v.finditer(text)

        if m:
            for r in m :
                tagged_sentence = tagged_sentence.replace((test[r.start():r.end()]), k)

                print("[ entity_name : {}, value : {}, start_idx : {}, end_idx : {}]".format(
                        k,r.group(), r.start(), r.end()))

    print("tagged_sentence : ",tagged_sentence)


Regex(text)

