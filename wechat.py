# coding:utf-8
import itchat
import re
import jieba
from wordimage import wordimage


itchat.auto_login(enableCmdQR=2, hotReload=True)
# itchat.send('Hello, filehelper', toUserName='filehelper')
friends = itchat.get_friends(update=True)[0:]

def friend_sex():
    male = female = other = 0
    for friend in friends[1:]:
        if friend['Sex'] == 1:
            male += 1
        elif friend['Sex'] == 0:
            female += 1
        else:
            other += 1
    f_nums = len(friends[1:])
    print("男性好友： %.2f%%" % (float(male) / f_nums * 100) + "\n" +
          "女性好友： %.2f%%" % (float(female) / f_nums * 100) + "\n" +
          "不明性别好友： %.2f%%" % (float(other) / f_nums * 100))

def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable
#调用函数得到各变量，并把数据存到csv文件中，保存到桌面
# NickName = get_var("NickName")
# Sex = get_var('Sex')
# Province = get_var('Province')
# City = get_var('City')
# Signature = get_var('Signature')
# from pandas import DataFrame
# data = {'昵称': NickName, '性别': Sex, '省份': Province,
#         '城市': City, '签名': Signature}
# frame = DataFrame(data)
# frame.to_csv('data1.csv', index=True, encoding='GB18030')

siglist = []
for i in friends[1:]:
    signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
    rep = re.compile("1f\d+\w*|[<>/=]")
    signature = rep.sub("", signature)
    siglist.append(signature)
text = "".join(siglist)
wordlist = jieba.cut(text, cut_all=True)
word_space_split = ' '.join(wordlist)

wordimage(word_space_split)
