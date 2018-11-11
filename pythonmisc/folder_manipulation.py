#! /usr/bin/env python
# Version: 0.1.2

import glob
import os


def get_recursive_files_from_extensions(directory, ext_list, regex_filename):
    filename_list = []
    for ext in ext_list:
        filename_list += glob.glob(directory + regex_filename + ext)

    sub_folders = next(os.walk(directory))[1]
    if len(sub_folders) > 0:
        for sub_folder in sub_folders:
            sub_folder_path = directory + "/" + sub_folder
            filename_list += get_recursive_files_from_extensions(sub_folder_path, ext_list, regex_filename)

    return filename_list
