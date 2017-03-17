#!/bin/python
import sys
n = int(raw_input().strip())

vowels = ['a', 'e', 'i', 'o', 'u']
consonents = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

if n == 1:
    for i in vowels:
        print i
    for i in consonents:
        print i
elif n == 2:
    for i in vowels:
        for j in consonents:
            print i+j
    for i in consonents:
        for j in vowels:
            print i+j
elif n == 3:
    for i in vowels:
        for j in consonents:
            for k in vowels:
                print i+j+k
    for i in consonents:
        for j in vowels:
            for k in consonents:
                print i+j+k
elif n == 4:
    for a in vowels:
        for b in consonents:
            for c in vowels:
                for d in consonents:
                    print a+b+c+d
    for a in consonents:
        for b in vowels:
            for c in consonents:
                for d in vowels:
                    print a+b+c+d
elif n == 5:
    for a in vowels:
        for b in consonents:
            for c in vowels:
                for d in consonents:
                    for e in vowels:
                        print a+b+c+d+e
    for a in consonents:
        for b in vowels:
            for c in consonents:
                for d in vowels:
                    for e in consonents:
                        print a+b+c+d+e
elif n == 6:
    for a in vowels:
        for b in consonents:
            for c in vowels:
                for d in consonents:
                    for e in vowels:
                        for f in consonents:
                            print a+b+c+d+e+f
    for a in consonents:
        for b in vowels:
            for c in consonents:
                for d in vowels:
                    for e in consonents:
                        for f in vowels:
                            print a+b+c+d+e+f
