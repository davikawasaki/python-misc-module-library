#! /usr/bin/env python
# Version: 0.1.1

import re


def convert_ws_header_vb_attributes(df):
    output_txt = ""
    for key in df.keys():
        variant_array = "\'Dim "
        i = 0
        for word in [w.capitalize().replace('\t', '') for w in str(key).lower().split("(")[0].split(" ")]:
            if i == 0:
                word = word.lower()
            if word != "" and word != "-":
                variant_array += word
            i += 1
        variant_array = variant_array.rstrip()
        variant_array += "() As Variant\n"
        output_txt += variant_array

    return output_txt


def remove_special_characters(text):
    _vec = ''.join(re.split(r'[^a-zA-Z]', text)).split()
    if len(_vec) == 1:
        return _vec[0]
    else:
        return text
