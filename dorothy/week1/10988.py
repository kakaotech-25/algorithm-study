'''
팰린드롬인지 확인
앞, 거꾸로 읽을 때 똑같은 단어

첫째 줄: 단어, 1 <= len(word) <= 100, 소문자

출력: 팰린드롬이면 1, 아니면 0
'''

def isPalindrome(word):
    l = len(word)
    for i in range(l//2):
        if word[i] != word[-(i+1)]:
            return 0
    return 1

word = input()
print(isPalindrome(word))