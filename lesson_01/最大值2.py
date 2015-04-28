#!/usr/bin/env python
# -*- coding: utf-8 -*-
num1 = 0
num2 = 0
list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]
for a in list:
    if a>num1:
       num1=a
for b in list:
    if b>num2 and b<num1:
       num2=b
print 'The first number is %s and the second number is %s' % (num1,num2)