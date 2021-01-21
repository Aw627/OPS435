#!/usr/bin/env python3

#author ID:hcawong

import subprocess


def free_space():
    a = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = a.communicate()
    stdout = output[0].decode('utf-8').strip()
    return stdout

print(free_space())
