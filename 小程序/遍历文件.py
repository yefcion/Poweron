# -*- coding: utf-8 -*-

import os

file_path_list = []

def traverse(folder_path):
    fp = os.listdir(folder_path)
    for file in fp:
        tmp_path = os.path.join(folder_path,file)
        file_path_list.append(tmp_path)
    print(tmp_path)

path = 'G:/Visual studio/ShipC/ShipC'
traverse(path)
# print(tmp_path)
print(file_path_list)

input("press any key to quit...")

# 遍历指定路径下的一级目录文件，并加入列表



'''
子目录
        if not os.path.isdir(tmp_path):             # 当前目录
            print('文件: %s'%tmp_path)
        else:                                       # 子目录
            print('文件夹：%s'%tmp_path)
            traverse(tmp_path)
'''
