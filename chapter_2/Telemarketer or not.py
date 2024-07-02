#전화번호 네 자리라고 가정
#첫 번째 숫자는 8 또는 9
#네 번째 숫자는 8 또는 9
#두 번째와 세 번재 숫자는 동일
#각 자리 숫자는 0~9 사이의 정수
#텔레마케터 번호 라면 ignore 출력, 아니면 answer 출력

num_1 = int(input())
if num_1 < 0 or num_1 > 9:
    exit("범위 오류")

num_2 = int(input())
if num_2 < 0 or num_2 > 9:
    exit("범위 오류")

num_3 = int(input())
if num_3 < 0 or num_3 > 9:
    exit("범위 오류")

num_4 = int(input())
if num_4 < 0 or num_4 > 9:
    exit("범위 오류")

#텔레마케터 번호 조건
if ((num_1 == 8 or num_1 == 9) and
        (num_4 == 8 or num_4 ==9) and
        (num_2 == num_3)):
    print("ignore")
else:
    print("answer")