#!/usr/bin/env python
# -*- coding: utf-8 -*-
while True:
    year = raw_input('please input year:')
    if int(year) % 400 == 0:
        print year
        break
    elif int(year) % 4 == 0 and int(year) %100 <>0:
        print year
        break
    else:
        print "This's year is not a leap year"
