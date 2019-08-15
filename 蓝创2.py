import re

with open('data.json', 'r', encoding='utf-8') as f:
    l = f.read()
list = re.findall(r'"(.*?)":([0-9]+),', l)
dict = {}
for i in list:
    t = i
    dict[t[0]] = int(t[1])
res = sorted(dict.items(),key=lambda d:d[1],reverse=True)
with open('p2.txt','w+',encoding='utf-8') as f:
    f.write(res)

