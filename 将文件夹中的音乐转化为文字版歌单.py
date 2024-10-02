# -*- coding: utf-8 -*-
import re
import os
folder_path = "D:/Desktop/Favourite"  # 将这里替换为你的文件夹路径
output_file = "file_names.txt"  # 存储文件名的文本文件名称
file_names = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_names.append(os.path.join(root, file))
with open(output_file, "w", encoding='utf-8') as f:
    for name in file_names:
        f.write(name + "\n")
# 读取包含文件路径的 txt 文件
with open('file_names.txt', 'r',encoding='utf-8') as file:
    file_paths = file.readlines()
# 用于存储提取的文件名
filenames = []
# 提取文件名
for path in file_paths:
    path = path.strip()
    match = re.search(r'([^/\\]+)\.([^.]+)$', path)
    if match:
        filename = match.group(1)
        filenames.append(filename)
    else:
        print(f"未匹配到文件名和扩展名：{path}")

# 将文件名写入新的 txt 文件
with open('filenames.txt', 'w',encoding='utf-8') as output_file:
    for filename in filenames:
        output_file.write(filename + '\n')

# 删除中间产生的过程文件
os.remove('file_names.txt')