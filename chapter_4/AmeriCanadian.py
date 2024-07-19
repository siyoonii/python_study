#문제 url : https://dmoj.ca/problem/ccc02j2
#americans translate to canadian
#입력받고 american 같으면 문자를 변환해라/ quit!를 입력하면 프로그램 종료
#4문자 이상, or 포함 > american spelling , or> our y모음 취급


lines = []
while True:
    word = input()
    if word == "quit!":
        break
    lines.append(word)

for word in lines:
    if len(word) > 4 and word[-2:] == "or" and word[-3] not in "aeiouy":
        word = word[:-2] + "our"
    print(word)
