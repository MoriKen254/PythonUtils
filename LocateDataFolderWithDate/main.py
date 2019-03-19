#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Copyright (c) 2016 Masaru Morita
This software is released under the MIT License.
See LICENSE file included in this repository.
"""
import os
from PIL import Image
from datetime import datetime as dt
import shutil
import copy



def main():
    dir_path = r'C:\Users\masam\PycharmProjects\MyUtils\LocateDateFolder\TestFiles'
    os.chdir(dir_path)

    files = extract_file_names_in_dir(dir_path)

    for x in files:
        root, ext = os.path.splitext(x)
        if ext == ".MOV" or ext == ".PNG":
            dt_str = extract_date_str_from_file(x)
        else:
            dt_str = get_date(x)

        # create dir whose name is date if not existed
        if not os.path.exists(dt_str):
            os.mkdir(dt_str)

        # move the file to the dir
        if os.path.exists(x):
            # shutil.copy2('./' + x, './' + dt_str + './' + x)
            shutil.move('./' + x, './' + dt_str)


def extract_file_names_in_dir(dir_path):
    files = []
    for x in os.listdir(dir_path):
        if os.path.isfile(dir_path + '/' + x):  # extract only files
            files.append(x)

    return files


def extract_date_str_from_file(file_name):
    dt_array = dt.fromtimestamp(os.stat(file_name). st_mtime)
    dt_str = dt_array.strftime('%Y%m%d')
    dt_str = dt_str[2:]

    return dt_str


def get_date(file_name):
    image = Image.open(file_name)
    exif = image._getexif()
    #if not 0x9003 in exif: continue
    time_str = exif[36867]
    dt_str = time_str[2:10]
    dt_str = dt_str.replace(":", "")
    dt_str_deep = copy.deepcopy(dt_str)
    image.close()

    return dt_str_deep


if __name__ == '__main__':
    main()
