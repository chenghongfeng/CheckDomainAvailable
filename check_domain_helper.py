import os

def main():
    write_pinyin_file("PinyinsDomian.txt")
#读取拼音文件将所有可能的域名写入到指定文件中
def write_pinyin_file(file_name):
    pinyin_source_file = open("拼音组合.txt",encoding="UTF-8")
    file_name = os.getcwd()+"\\"+file_name
    domain_file = open(file_name,'w')
    pingyins = []
    #将拼音的组合读取到列表中
    for line in pinyin_source_file:
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
            pinyin = pinyin_first + pinyin_second
            domian_name = pinyin+".com\n"
            domain_file.writelines(domian_name)
    print(count)
            # rsp = Tencent.check_domian_tencent(domian_name)
            # if(rsp!=None):
            #     available = Tencent.check_domian_tencent(domian_name).Available
            #     if(available):
            #         available_domains.append(domian_name)
            #         print(domian_name)

if __name__=='__main__':
    main()
