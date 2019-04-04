# -*- coding: utf-8 -*-

from underthesea import word_tokenize

data_1 = open('data_Dang.txt', 'r', encoding='utf-8', errors='ignore').read().split('\n')[:-1]

data_2 = open('data_Vi.md', 'r', encoding='utf-8', errors='ignore').read().split('\n')[:-1]

out = open('added.txt', 'w', encoding='utf-8', errors='ignore')

data = data_1 + data_2

data = [l for l in data if l != '']

num_lines = len(data)

#num_lines += 20740 + 1

start_i = 20740 + 1

for i in range(0,num_lines,2):
#    if i + 2 > num_lines:
#        break
#    
#    out.write(data[i])
#    out.write('\n')
#    out.write(data[i+1])
#    out.write('\n')
#    out.write('\n')
    s = '+++$+++ u0 +++$+++ m0 +++$+++ CAMERON +++$+++'
    l = data[i]
    l = l.lower()
    l = l.replace(',', '')
    l = l.replace('?', '')
    l = l.replace('!', '')
    l = l.replace('.', '')
    l = l.strip()
    l = word_tokenize(l,format='text')
    
    l2 = data[i+1]
    l2 = l2.lower()
    l2 = l2.replace(',', '')
    l2 = l2.replace('?', '')
    l2 = l2.replace('!', '')
    l2 = l2.replace('.', '')
    l2 = l2.strip()
    l2 = word_tokenize(l2,format='text')
    
    if len(l.split()) > 10 or len(l2.split()) > 10:
        continue
    
    out.write('L{} {} {}\n'.format(i+start_i,s,l))
    
    out.write('L{} {} {}\n'.format(i+start_i+1,s,l2))
    
    
out.close()

