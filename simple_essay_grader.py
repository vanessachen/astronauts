# -*- coding: utf-8 -*-

'''
    read_essays.py

    This Python file can be used as a starting point for
    teaching the computer to grade a school essay.
'''

# Don't worry about these 2 lines
from essays.en1 import essay_en1
from essays.en2 import essay_en2

################################################
informal_words = ['really', 'cool', 'whoa', 'wow', 'way', 'probably']
informality_count1 = 0
informality_count2 = 0
essay_en1_list = essay_en1.split(' ')#making essay 1 into a list
essay_en2_list = essay_en2.split(' ')#making essay 2 into a list

for i in range (len(informal_words)):
    for x in range (len(essay_en1_list)):
        if informal_words[i] == essay_en1_list[x]:
            informality_count1+=1

for i in range (len(informal_words)):
    for x in range (len(essay_en2_list)):
        if informal_words[i] == essay_en2_list[x]:
            informality_count2+=1

print ("Informality count in essay 1 is: " + str(informality_count1))
print (" and informality count in essay 2 is: " + str(informality_count2))

if informality_count1 > informality_count2:
    print("essay 1 is less formal because it has more informal words")
elif informality_count1 == informality_count2:
    print("both essays have the same amount of formal words")
else:
    print("essay 2 is less formal because it has more informal words")


################################################
'''
if "really cool" in essay_en1:
    print("The phrase 'really cool' appears in Essay 1.")
else:
    print("The phrase 'really cool' was NOT found.")
'''
