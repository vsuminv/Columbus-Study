
# 대소문자를 소문자로 바꿈
word = input().upper()
set_word = list(set(word))

cnt_list = []

for i in range(len(set_word)):
    cnt = 0
    # 단어와 같은 알파벳이 있는 경우 카운트
    for j in word:
        if set_word[i] == j:
            cnt += 1
    cnt_list.append(cnt)

# 가장 많이 사용한 알파벳이 여러 개 존재하는 경우
if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    print(set_word[cnt_list.index(max(cnt_list))])


