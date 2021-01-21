#!/usr/bin/env python3

#Author: Ho Chun Adrian Wong
#Author ID: hcawong
#Date Created: 2020/09/30

import sys


if len(sys.argv) ==2:
    timer = int(sys.argv[1])
else:
    timer = 3
while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')
