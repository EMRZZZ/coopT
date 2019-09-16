import sys
import getopt
import re

opts, args = getopt.getopt(sys.argv[1:], '-u:-o,-f:-o,-h')
print(opts[0][0])  # opts为二元组的列表，第一个是选项，第二个是其后的参数
print(opts[0][1])
opt = opts[0][0]
url = opts[0][1]


def checkURL(url):
    if re.match('.|<|>|]', url):   # 需要修改，从数据库读取关键词并匹配
        print("ok")
    else:
        print("failed")


def checkFile(fileName):
    with open('./'+fileName, 'r') as f:
        for line in f.readlines():
            if re.match('.|<|>|]', line):  
                print(line)
            else:
                continue  # 或者记录下有问题的url并输出文件，再继续下去


'''
file = 'file.txt'
with open('./'+file, 'r') as f:
    for line in f.readlines():
        print(line.strip())
'''

for o, a in opts:
    if o in '-u':
        checkURL(opts[0][1])
    if o in '-f':
        checkFile(opts[0][1])
    if o in '-h':
        print('URLCheck.py [-u] url, [-f] fileName.txt')
