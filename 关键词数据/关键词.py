import re, json, os

os.chdir("F:\\大道之君\\Breakingthrough-Techonologies-Data-Analysis\\关键词数据\\关键词raw")
file = open("Quantumwires.txt")
#  示例：Keywords = [ ['Physical layer security','secrecy rate','potent'],\
# ['Optimization',' resonant converter'] ]
Keywords = []
Keywords_freq = {}  # 计算每个关键词的频数
for line in file:
    if 'DE ' in line:
        # keyline是DE 后面的关键词组成的列表
        keyline = re.findall(r"DE (.*)\n", line)[0].strip().split(";")
        keyword = []
        for word in keyline:
            if word != '' and not word.isspace():  # 判断word是否为空或只包含制表符\空格和换行符
                word = word.lower().strip()
                keyword.append(word)
                # 如果word首次出现，默认设为1，否则自加1.
                if word in Keywords_freq.keys():
                    Keywords_freq[word] += 1
                else:
                    Keywords_freq[word] = 1
        Keywords.append(keyword)
file.close()
# 把Keywords_freq转换成一个元组，按值的大小.从大到小排序
Keywords_freq = sorted(Keywords_freq.items(), key=lambda v: v[1], reverse=True)
#  print(Keywords_freq)
os.chdir("F:\\大道之君\\Breakingthrough-Techonologies-Data-Analysis\\关键词数据\\关键词Data")
json_file = "Quantumwires.json"
with open(json_file, 'w') as f_obj:
    json.dump(Keywords, f_obj)
    f_obj.write("\n")
    json.dump(Keywords_freq, f_obj)
