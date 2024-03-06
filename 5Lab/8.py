import re
a=open(r"row.txt",'r',encoding='UTF-8')
s=a.read()
def uppercase(text):
    split=re.findall(r"[A-Z][^A-Z]*",text)
    return split
print(uppercase(s))