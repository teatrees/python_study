#!/usr/bin/env python
# -*- coding: utf-8 -*-
arr = ['C','js','python','js','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node','css','js','html','node','js','python','js','css','js','html','node','js','python','js','css','js','html','node']
dic = {}
for i in arr:
    if i in dic:
        dic[i] = dic[i]+1
    else:
        dic[i] = 1
print dic
