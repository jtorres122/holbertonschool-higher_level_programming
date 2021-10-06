#!/usr/bin/python3
'''

Module contains function that indents a text

'''


def text_indentation(text):
    '''
    Function indents a text every iteration of specific characters
    '''

    match = ".?:"

    if type(text) is not str:
        raise TypeError("text must be a string")

    idx = 0

    while idx < len(text):
        print(text[idx], end="")
        if text[idx] in match:
            print("\n")
            while(text[idx + 1] == ' '):
                idx += 1
        idx += 1
