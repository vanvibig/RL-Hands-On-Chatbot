# -*- coding: utf-8 -*-

movie_conversations = open('movie_conversations_vn_full.txt', 'r', encoding='utf-8', errors='ignore').read().split('\n')[:-1]

movie_conversations_vn = open('movie_conversations_vn.txt', 'w', encoding='utf-8', errors='ignore')

num_lines = 50000

for i in range(0,num_lines,2):
    if i + 2 > num_lines:
        break
    movie_conversations_vn.write("u0 +++$+++ u2 +++$+++ m0 +++$+++ ['L")
    movie_conversations_vn.write(str(i+1) + "', 'L" + str(i+2) + "']")
    movie_conversations_vn.write("\n")
    

