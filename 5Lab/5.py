import re
a=open(r"row.txt",'r',encoding="UTF-8")
s=a.read()
def match_str(text):
    pattern = r"a.*b$"
    if re.search(pattern, text):
        return "Match found"
    else:
        return "Match not found"

print(match_str(s))