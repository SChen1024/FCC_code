#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os

# 输入 指定 txt 文件路径, 创建文件的后缀 txt js
# 读取指定文件的txt 文档
# 在 txt 的同级目录下面建立相应的文件


def ReadArg():
    """
     通过sys模块来识别参数demo, http://blog.csdn.net/ouyang_peng/
    """
    print('参数个数为:', len(sys.argv), '个参数。')
    print('参数列表:', str(sys.argv))
    print('脚本名为：', sys.argv[0])
    for i in range(1, len(sys.argv)):
        print('参数 %s 为：%s' % (i, sys.argv[i]))
    return sys.argv

def ReadTxtLists(file):
    '''
    读物 txt 文件中的文件列表
    '''
    res =[]
    with open(file,'r') as f:
        for line in f:
            line.strip('\n')
            line = ''.join(line.split())
            res.append(line)
    return res

def CreateFile(file):
    with open(file, 'a'):
        os.utime(file,None)

def main():
    argv = ReadArg()
    suffix = "txt"     # 默认后缀

    # 只有两个参数表示没有 给后缀名
    if(len(argv) >= 3):
        suffix = argv[2]
    
    file_name= argv[1]

    # 读取得到所有的文件名
    files = ReadTxtLists(file_name)

    (filepath, filename) = os.path.split(file_name)

    # 计数 生成拼接文件 
    # 最终创建文件 如果存在 不更新文件
    cnt = 0
    for file in files:
        cnt += 1
        file_str = filepath + "\\" + str(cnt).zfill(2) + "_" + file + "." + suffix
        CreateFile(file_str)
        print(file_str+'\n')
if __name__ == "__main__":
    main()

