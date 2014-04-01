#!/usr/bin/python

import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split('\t')
        if len(data) == 5 and data[0] != 'user_ptr_id':
            lst = list(data)
            lst.insert(1, 'A')
            print '\t'.join(lst)
        elif len(data) == 19 and data[0] != 'id':
            lst = list(data)
            key = lst[3]
            lst.pop(4)
            lst.insert(0, 'B')
            lst.insert(0, key)
            print '\t'.join(lst)
