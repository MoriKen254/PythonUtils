#!/usr/bin/python
# -*- coding: utf-8 -*-
u"""
Copyright (c) 2016 Masaru Morita
This software is released under the MIT License.
See LICENSE file included in this repository.
"""
import os
from datetime import datetime as dt
import shutil


def main():
    #dir_path = r'C:\Users\masam\PycharmProjects\MyUtils\LocateDateFolder\TestFiles'
    dir_path = r'C:\Users\masam\Desktop\photos'
    os.chdir(dir_path)

    files = extract_file_names_in_dir(dir_path)

    for x in files:
        dt_str = extract_date_str_from_file(x)

        # create dir whose name is date if not existed
        if not os.path.exists(dt_str):
            os.mkdir(dt_str)

        # move the file to the dir
        if os.path.exists(x):
            shutil.move('./' + x, './' + dt_str)


def extract_file_names_in_dir(dir_path):
    files = []
    for x in os.listdir(dir_path):
        if os.path.isfile(dir_path + '/' + x):  # extract only files
            files.append(x)

    return files


def extract_date_str_from_file(file_name):
    dt_array = dt.fromtimestamp(os.stat(file_name).st_mtime)
    dt_str = dt_array.strftime('%Y%m%d')
    dt_str = dt_str[2:]

    return dt_str


if __name__ == '__main__':
    main()
