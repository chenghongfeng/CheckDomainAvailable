import requests
import json

import Tencent
#def ReadPinyin(file_name):

pingyins = []
available_domains = []

file = open("拼音组合.txt",encoding="UTF-8")
for line in file:
    if(line[0] == "-"):
        continue
    line_list = line.split()
    del line_list[0]
    pingyins.extend(line_list)
pingyins.append("")
print(pingyins)
print(len(pingyins))
count = 0
for pinyin_first in pingyins:
    for pinyin_second in pingyins:
        count = count +1
        print(count)
        pinyin = pinyin_first + pinyin_second
        domian_name = pinyin+".com"
        rsp = Tencent.CheckDomianTencent(domian_name)
        if(rsp!=None):
            available = Tencent.CheckDomianTencent(domian_name).Available
            if(available):
                available_domains.append(domian_name)
                print(domian_name)
        

print(available_domains)  
file.close()