# 문자열 각 알파벳의 개수를 센다.
# 리스트 컴프리헨션으로 리스트 초기화.
# map() 함수로 리스트의 요소를 문자열로 바꾼다.
array = input()
result = [0 for _ in range(26)]

for i in array:
    result[ord(i) - ord('a')] += 1

print(" ".join(map(str, result)))