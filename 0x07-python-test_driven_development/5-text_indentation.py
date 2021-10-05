#!/usr/bin/python3


def text_indentation(text):

    match = ".?:"

    if type(text) is not str:
        raise TypeError("text must be a string")

    idx = 0

    while idx < len(text):
        print(text[idx], end="")
        if text[idx] in match:
            print("\n")
            while(text[idx + 1] == ' ' ):
                idx += 1
        idx += 1
