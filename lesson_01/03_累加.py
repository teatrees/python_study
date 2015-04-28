#!/usr/bin/env python
# -*- coding: utf-8 -*-
init_num = 0
#init_status = 'input'
while True:
    a = raw_input('input a number:')
    if a == 'pc':
#        init_status = 'stop'
         break
    else:
        init_num = init_num+int(a)
print init_num

#print input_num
#init_num = 0
#while True:
#    input_number = raw_input('input a number:')
#    if not input_number:
#        break
#    else:
#        init_num = init_num+int(input_number)
#print init_num