#3개의 연속된 문자 :-)는 happy face
#3개의 연속된 문자 :-(는 sad face
#메시지 전반적인 무드를 파악해라

#한 줄로 입력, 1~255 문자열
line = input("메시지를 입력하세요.")
if len(line) < 1 or len(line) > 255:
    exit()

happy_face = str(":-)")
sad_face = str(":-(")

if line.count(happy_face) == line.count(sad_face): #happy face의 개수와 sad face 개수가 같으면 "unsure"
    print("unsure")
elif line.count(happy_face) > line.count(sad_face): #happy face 개수 > sad face 개수 "happy"
    print("happy")
elif line.count(happy_face) < line.count(sad_face): #happy face 개수 < sad face 개수 "sad"
    print("sad")
else: #happy face 또는 sad face가 포함되어있지 않으면 "none"
    print("none")