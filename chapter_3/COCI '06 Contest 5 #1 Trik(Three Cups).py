#문제url :https://dmoj.ca/problem/coci06c5p1
#swap: three possible ways

swaps = input()
if swaps.isdigit():
    exit()
if not len(swaps) <= 50:
    exit()

#공이 있는 컵의 위치, 1일경우 왼쪽 컵, 2일경우 중간컵, 3일 경우 오르쪽 컵에 공이 있음
index_cup = 1

for swap_type in swaps:
    if swap_type == "A" and index_cup == 1:
        index_cup = 2
    elif swap_type == "A" and index_cup == 2:
        index_cup = 1
    elif swap_type == "B" and index_cup == 2:
        index_cup = 3
    elif swap_type == "B" and index_cup == 3:
        index_cup = 2
    elif swap_type == "C" and index_cup == 1:
        index_cup = 3
    elif swap_type == "C" and index_cup == 3:
        index_cup = 1

print(index_cup)