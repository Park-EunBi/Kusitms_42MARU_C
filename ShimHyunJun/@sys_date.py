#-*-coding:utf-8-*-
import re,sys
def sys_date():
    source =raw_input("예시문:") #raw_string input
    #"안녕 시리야 2021년 3월19일에 보낸 메일 찾아줘" # 예시 문자열
    p = re.compile(r'((\d*년?\s?)?(\d+월\s?)?(\d+일\s?))+|((작년)|(오늘)|(어제)|(모레)|(글피)|(내일))+|((월요일)|(화요일)|(수요일)|(목요일)|(금요일)|(토요일)|(일요일))+')
    m = p.finditer(source)  #source문자열로부터 패턴에 맞는 match객체를 담은 이터러블obj를 리턴 
    value=''
    for matchNum, match in enumerate(m, start=1): # 매치idx & match객체   # m매치객체를 idx1번부터 열거
        print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        value = value + match.group()   
    print(value)
   
        
    print("-----------------Result-----------------")
    print("entity_name: @{name}".format(name=sys._getframe().f_code.co_name)) #entity_name
    p = re.compile('올해|년|작년|월|일') #대체 대상 추가 가능
    someValue =p.sub('-',value)
    if someValue[0] is '-':
        someNewValue = someValue[1:-1]+" 00:00:00"
    else:
        someNewValue = someValue[0:-1]+" 00:00:00"
    print("value: "+ someNewValue)           #value
    
    print("start_idx: "+str(match.start()))  #start_idx
    print("end_idx: "+str(match.end()))      #end_idx 
    
    #print("tagged_sentence:")      
    
    #value값들 List자료로 묶어서취합 
sys_date()

"""
#entity_name
문장에서 찾아낸 개체명. 
e.g) 2022년3월21일에 보낸 메일 찾아줘 ⇒ @sys.date

#value
문장에서 찾아낸 개체명의 value
e.g) 2022년3월21일에 보낸 메일 찾아줘 ⇒ 2022-03-21 00:00:00

#start_idx
문장에서 개체명이 시작하는 위치
e.g) 2022년3월21일에 보낸 메일 찾아줘 ⇒ 0
//
#end_idx
문장에서 개체명이 끝나는 위치
2022년3월21일에 보낸 메일 찾아줘 ⇒ 9

#tagged_sentence
문장을 개체명으로 치환한 결과
2022년3월21일에 보낸 메일 찾아줘 ⇒ @sys.date에 보낸 메일 찾아줘
=> re.sub

여러개의 정규식을 순차적으로 순환해 정해진 결과를 반환하는 모듈을 작성하면 됩니다.

정규식은 따로 공부 하시면되고 복잡한 정규식을 나름 잘 정리한 예제는 아래 github 확인하시면 됩니다.
"""

