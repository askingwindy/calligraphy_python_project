#!/usr/bin/env python
# coding: utf-8

import sys

EXCLUSION_CHAR_LIST = ['；', '。', '\n', '\t', '，', '\r', '\r\n']

def openFile(filePath):
    """ open a file, and load the content
    :param filePath: file path
    :return:
    """

    file = open(filePath, "r");

    content = [];

    for line in file.readlines():
        content.append(line)

    file.close()
    return content;


def statistic(content, exception_words):
    """
    statistic word and its count number in the specific rows
    :param content: file content , line[]
    :param exception_words: we execute before in statistic_exists_words()
    :return:
    """
    ss = ''
    ee = ''
    try:
        ss = input('plz input count start line no (default first line if not enter) :')  # start statistic line no
    except:
        ss = '1'
    try:
        ee = input('plz input count end line no (default last line if not enter) :')  # end statistic line no
    except:
        ee = sys.maxint

    # print content
    word_dict = {}
    line_no = 0

    for line in content:
        line_no += 1;
        if line_no > int(ee):
            break;
        elif line_no < int(ss):
            continue;
        for i in line:
            if i in exception_words:
                continue
            if i in EXCLUSION_CHAR_LIST:
                continue
            if i not in word_dict:
                word_dict[i] = 1;
            else:
                word_dict[i] += 1;
    return word_dict;


def statistic_exists_words(content):
    ss = ''
    ee = ''
    try:
        ss = input('plz input start line no which u want to except statistic (default first line if not enter) :')  # start statistic line no
    except:
        ss = '1'
    try:
        ee = input('plz input existed end line no which u want to except statistic (default last line if not enter) :')  # end statistic line no
    except:
        ee = '-1'
    if ee == '-1':
        return []

    word_dict = {}
    line_no = 0;
    for line in content:
        line_no += 1;
        if line_no > int(ee):
            break;
        elif line_no < int(ss):
            continue;
        for i in line:
            if i in EXCLUSION_CHAR_LIST:
                continue
            if i not in word_dict:
                word_dict[i] = 1;
            else:
                word_dict[i] += 1;
    except_words = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)

    except_words = except_words[0:10]
    print(except_words)

    rst = []
    for item in except_words:
        rst.append(item[0])
    return rst;


if __name__ == '__main__':
    """
    统计道德经中的中文字的个数top10
    """
    content = openFile('./data/daodejing.data');

    # 拿到需要排除统计的行，它会计算出这些行之间的top10
    exception_words = statistic_exists_words(content)

    # 拿到本次需要统计的行数中的字与其出现次数
    r = statistic(content, exception_words)

    ff = sorted(r.items(), key=lambda x: x[1], reverse=True)

    # output a list, containing top 10 highest frequency characters
    print (ff)