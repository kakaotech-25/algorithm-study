import re
from collections import deque

strs = []
answer_list = []
bracket = deque()

while True:
    s = input()
    if s == '.':
        break
    strs.append(s.split(".")[0])

for s in strs:
    # print(s)

    bracket.clear()
    answer = True
    for c in s:
        if c == '(' or c == '[':
            #print(f"{c} append")
            bracket.append(c)
        elif c == ')':
            if len(bracket) > 0 and bracket[-1] == '(':
                #print(") pop")
                bracket.pop()
            else:
                #print("() 안 맞음")
                answer = False
                break
        elif c == ']':
            if len(bracket) > 0 and bracket[-1] == '[':
                #print("] pop")
                bracket.pop()
            else:
                #print("[] 안 맞음")
                answer = False
                break
        else:
            continue
    
    if len(bracket) > 0:
        # print(bracket)
        answer = False
    
    answer_list.append(answer)


for answer in answer_list:
    if answer:
        print('yes')
    else:
        print('no')
