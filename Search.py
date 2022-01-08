import jieba


def read_txt_data(file_name):
    with open(file_name, encoding='utf-8', errors='ignore') as file_object:
        lines = file_object.readlines()  # 读取每一行存在一个列表中

    data_string = []
    for line in lines:
        data = line.strip('\n').split()[0]  # strip()去除首尾换行符，并按空格划分  [0]表示只取每一行的第一个元素
        data_string.append(data)

    file_object.close()
    return set(data_string)  # 转换成集合的形式，方便接下来的词汇过滤


with open('辱骂.txt', encoding='utf-8', errors='ignore') as file_object:
    lines = file_object.readlines()  # 读取每一行存在一个列表中
for line in lines:
    data = line.strip('\n').split()[0]  # strip()去除首尾换行符，并按空格划分  [0]表示只取每一行的第一个元素
    jieba.add_word(data)  # 将txt文件里的词加入库里

s = '我干，老子今天打死你个傻逼玩意儿，你这人心真黑，我操，几个意思，你这人太没素质了，你是不是听不懂人话，我第一次遇见你这样的人，你还敢骂我？中华人民共和国真伟大，今天我真幸运，上了你的车，我真的太开心了'
result = jieba.lcut(s, cut_all=True)  # 进行分词
a = ['，', '？', '。', '！']
result2 = [w for w in result if w not in a]  # 去掉标点符号
set_result = set(result2)  # 将分词之后、去掉标点符号的列表转化为集合
print(s)  # 输出原文本
Abusive_words_list = read_txt_data("辱骂.txt")
num = len(set_result & set(Abusive_words_list))  # 求两个集合的交集
if num != 0:  # 输出结果
    print('‘{}’具有辱骂倾向'.format(set_result & set(Abusive_words_list)))
else:
    print('正常')
