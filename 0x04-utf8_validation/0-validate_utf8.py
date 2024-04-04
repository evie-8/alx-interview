#!/usr/bin/python3
'''module to validate UTF-8
'''


def validUTF8(data):
    '''Return truedata is valid utf8, else false
    '''
    count = 0
    for num in data:
        if count == 0:
            if num & 128 == 0:
                count = 0
            elif num & 224 == 192:
                count = 1
            elif num & 240 == 224:
                count = 2
            elif num & 248 == 240:
                count = 3
            else:
                return False
        else:
            if num & 192 != 128:
                return False
            count -= 1
    if count == 0:
        return True
    return False
