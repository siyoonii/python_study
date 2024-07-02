#1~3번째 줄의 인풋은 사과팀의 점수, 4~6번째 줄은 바나나팀의 점수
#각 팀의 1번째 줄: 3점, 2번째 줄: 2점, 3번째 줄: 1점 슛 성공 횟수
#모든 성공횟수는 정수이고, 0~100사이이다. 0 <= x <= 100
#결과: 사과팀 승리 A, 바나나팀 승리 B, 비겼을 때 T

#사과팀의 슛 성공횟수를 입력받음(성공횟수 입력 조건 검사)
apple_three = int(input("사과팀의 3점 슛 성공 횟수를 입력하세요: "))
if apple_three < 0 or apple_three > 100:
    exit("범위를 벗어남 (0 <= 사과팀의 3점 슛 성공 횟수 <=100)")

apple_two = int(input("사과팀의 2점 슛 성공 횟수를 입력하세요: "))
if apple_two < 0 or apple_two > 100:
    exit("범위를 벗어남 (0 <= 사과팀의 2점 슛 성공 횟수 <=100)")

apple_one = int(input("사과팀의 1점 슛 성공 횟수를 입력하세요: "))
if apple_one < 0 or apple_one > 100:
    exit("범위를 벗어남 (0 <= 사과팀의 1점 슛 성공 횟수 <=100)")

#바나나팀의 슛 성공횟수를 입력받음 (성공횟수 입력 조건 검사)
banana_three = int(input("바나나팀의 3점 슛 성공 횟수를 입력하세요: "))
if banana_three < 0 or banana_three > 100:
    exit("범위를 벗어남 (0 <= 바나나팀의 3점 슛 성공 횟수 <=100)")

banana_two = int(input("바나나팀의 2점 슛 성공 횟수를 입력하세요: "))
if banana_two < 0 or banana_two > 100:
    exit("범위를 벗어남 (0 <= 바나나팀의 2점 슛 성공 횟수 <=100)")

banana_one = int(input("바나나팀의 1점 슛 성공 횟수를 입력하세요: "))
if banana_one < 0 or banana_one > 100:
    exit("범위를 벗어남 (0 <= 바나나팀의 1점 슛 성공 횟수 <=100)")

#점수 총 합 계산
apple_total = apple_three * 3 + apple_two * 2 + apple_one * 1
banana_total = banana_three * 3 + banana_two * 2 + banana_one * 1

if apple_total > banana_total:
    print("A")
elif apple_total < banana_total:
    print("B")
elif apple_total == banana_total:
    print("T")