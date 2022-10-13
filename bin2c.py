#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import sys
import os
import platform

PY3 = sys.version_info[0] == 3


def _read_bin(filename):
    """ Read binary data from file and return as a C array
    :param filename: a filename of a file to read.
    :param varname: a C array variable name.
    """
    if not os.path.isfile(filename):
        print('File "%s" is not found!' % filename)
        return -1
    with open(filename, 'rb') as input_file:
        data = input_file.read()
    out = ""
    line = ""
    count = 0
    for byte in data:
        count += 1
        # print(byte)
        line += '0x%02x, ' % (byte if PY3 else ord(byte))
        # print(line)
        out += line
        line = ""
        if count == 30: # change line every 30 data
            out += "\n"
            count = 0
    return (out, len(data))


def _bin2c():
    name = imgname
    nameUpper = name.upper()
    (binRaw, data_size) = _read_bin(img_path)
    (dataRaw, data11_size) = _read_bin(img_path)
    print("read from %s" % img_path)
    # print(binRaw)
    
    if platform.system()=="Windows":
        bin2c_path = os.popen("where bin2c.exe").read().strip()
    elif platform.system()=="Linux":
        bin2c_path = os.popen("which bin2c.exe").read().strip()
    else:
        bin2c_path = sys.argv[0]
    if not os.path.isfile(bin2c_path):
        bin2c_path = sys.argv[0]
    print(bin2c_path)
    # print(sys.argv[0]) bin2c
    # print(__file__) C:\Users\new\AppData\Local\Temp\_MEI181202\bin2c.py
    template_path = os.path.join(os.path.dirname(bin2c_path), "sd_res_template.c")
    with open(template_path, "r") as template_file:
        output_lines = []
        lines = template_file.readlines()
        for line in lines:
            # print(line)
            line = line.replace(r"{NAME_LOWER}", name)
            line = line.replace(r"{NAME_UPPER}", nameUpper)
            line = line.replace(r"{DATA_SIZE}", str(data_size))
            line = line.replace(r"{BIN_RAW}", binRaw)
            line = line.replace(r"{DATA_RAW}", dataRaw)
            output_lines += line
        with open(cfile, "w") as output_file:
            output_file.writelines(output_lines)
        print("generated: %s" % cfile)


if __name__ == "__main__":
    # preprocess预处理
    # args = sys.argv[1:]
    # if len(args) != 2:
    #     raise ValueError("usage: python %s input_img_dir output_c_dir" % sys.argv[0])
    # img_dir, c_dir= args
    # if(not os.path.isdir(img_dir)):
    #     raise IOError("文件夹不存在,请重新输入图片所在文件夹: ")
    # if(not os.path.isdir(c_dir)):
    #     raise IOError("文件夹不存在,请重新输入图片所在文件夹: ")
    print("version: 20221013")
    img_dir = input("请输入图片所在文件夹: ")
    while(not os.path.isdir(img_dir)):
        img_dir = input("文件夹不存在,请重新输入图片所在文件夹: ")
    c_dir = input("请输入目标c文件存放的文件夹: ")
    while(not os.path.isdir(c_dir)):
        c_dir = input("文件夹不存在,请重新输入目标c文件存放的文件夹: ")
    img_paths = os.listdir(img_dir)
    for img_path in img_paths:
        if '.c' in img_path or os.path.isdir(img_path):
            print("skip: %s" % img_path)
            continue
        imgname = img_path.split('.')[0]
        img_path = os.path.join(img_dir, img_path)
        cfile = os.path.join(c_dir, imgname+".c")
        # 结构体名称判断
        if '-' in imgname:
            print("%s 存在\"-\"字符，c结构体名称将\"-\"改为\"_\"" % img_path)
            imgname = imgname.replace("-", "_")
        if ' ' in imgname:
            print("%s 存在空格，c结构体名称将空格改为\"_\"" % img_path)
            imgname = imgname.replace(" ", "_")
        if re.search(r"\W", imgname):
            print("%s 存在除字母数字下划线以外的特殊字符，程序中断" % img_path)
            os.system("pause")
            sys.exit(1)
        for char in imgname:
            if u'\u4e00' <= char <= u'\u9fff':
                print("%s 存在中文，程序中断" % img_path)
                os.system("pause")
                sys.exit(1)
        
        _bin2c()
    
    print("Finished!")
    os.system("pause")

