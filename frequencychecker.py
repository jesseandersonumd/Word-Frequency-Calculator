#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:00:53 2020

@author: jesseanderson
"""

import nltk
nltk.download('punkt')
import string
with open('rtnews.txt') as article, open('common_words.txt', mode = 'r') as common:
    word_list = []
    for line in common.read().split():
        word_list.append(line)
    sentenced_article = nltk.tokenize.sent_tokenize(article.read())
    empty_list=[]
    new_list=[]
    for item in sentenced_article: 
        if 'biden' in item.lower():
            for word in item.split():
                if word not in empty_list and ('biden' not in word.lower()) and ('joe' not in word.lower()):
                    word = word.lower().translate({ord(i): None for i in '‘,?“.!…”:’;)('})
                    if (word in word_list)==False:
                        empty_list.append(word)
                    else:
                        continue            
            new_list.append(item)
        else:
            continue

    top_words = {i : empty_list.count(i) for i in empty_list if empty_list.count(i)>=1 or i[-3:]=='ing' or i[-3:]=='ous'}
    for item in new_list:
        print(item)
    print(top_words)