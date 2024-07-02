#2월 18일은 CCC의 스페셜한 날짜다
#숫자인 월, 숫자인 일을 입력 받은 후 2월18일 이전인지, 이후인지 당일인지 확인해라
#입력은 2개의 정수로 각 각 다른 줄로 입력되고 이 정수들은 2015년의 날짜를 의미함
#첫 번째 줄: 월, 정수, 1(1월) ~ 12(12월) 사이
#두 번째 줄: 일, 정수, 1~31, 월에 따라서 달라지는 일을 확인해야 함
#숫자인 월, 숫자인 일을 각 다른 줄로 정수로 입력 받음

month = int(input())
day = int(input())

# 월, 일 조건
if month < 1 or month > 12:
    exit()

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if 1 <= day <= 31:
        print()
    else:
        exit()
elif month == 2:
    if 1 <= day <= 28:
        print()
    else:
        exit()
else:
    if 1 <= day <= 30:
        print()
    else:
        exit()

#이전 이면 단어 Before, 이후면 단어 After, 당일이면 Special
if month < 2 or (month == 2  and day < 18):
    print("Before")
elif month == 2 and day == 18:
    print("Special")
else:
    print("After")