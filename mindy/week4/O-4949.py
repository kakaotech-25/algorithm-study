# 문자의 균형 맞추기
# 괄호 맞추기
# 이전값 다음값을 저장해서 



    
while(True):
    stack =[]
    
    s = input()
    if s =='.':
        break
    
    
    for i in s:
        if i == '(' or i=='[':
            stack.append(i)
        elif i == ')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(i)
                break
        elif i == ']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(i)
                break
    
    if not stack:
            print("yes")
    else:
            print("no")
            
        

        