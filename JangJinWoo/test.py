import date

text = input()
value = date.checkDate(text)

if value=='ok':
    print(date.selectDate(text))

