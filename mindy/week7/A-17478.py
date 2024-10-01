# n까지 질문을 반복하고
# n번째에서 답변
# 그만큼 되돌아가기

import sys

input = sys.stdin.readline

n = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

def re(i,k):
    if i<n:
        an = '____' * i
        print(f'{an}"재귀함수가 뭔가요?"')
        print(f'{an}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(f'{an}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(f'{an}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        return re(i+1,k+1)
    elif i==n and k<n and k>0:
        an = '____' * k
        print(f'{an}라고 답변하였지.')
        return re(i,k-1)
    elif i == n and k==n:
        an = '____' * i
        print(f'{an}"재귀함수가 뭔가요?"')
        print(f'{an}"재귀함수는 자기 자신을 호출하는 함수라네"')
        print(f'{an}라고 답변하였지.')
        return re(i,k-1)
    
    else:
        print("라고 답변하였지.")
        return 0
re(0,0)