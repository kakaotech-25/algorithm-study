# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

input = sys.stdin.readline

[n, m] = input().split()
a_list = input().split()
b_list = input().split()

lines = []
for line in sys.stdin:
	if line.strip() == "":
		break
	lines.append(line.strip().split())
# print(lines)

# print(n, m)
# print(a_list)
# print(b_list)
# print(lines)
# 탐색 1000번 안에 끝내기

# 내 리스트 딕셔너리화
a_dict = dict.fromkeys(a_list, 0)
b_dict = dict.fromkeys(b_list, 0)

# print(lines)
# 라인을 돌면서 딕셔너리에 카운트 증가 
for index, line in enumerate(lines):
	a_send = line[0]
	b_send = line[1] 
	if a_send in a_dict and b_send in b_dict:
		a_dict[b_send] = 0
		b_dict[a_send] = 0
		del(a_dict[a_send])
		del(b_dict[b_send])

# 사전순 정렬후 출력
sort_a = " ".join(list(sorted(a_dict)))

print(sort_a)
