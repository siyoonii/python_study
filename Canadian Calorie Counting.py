#각 음식은 숫자를 입력하면 선택됨
#음식 종류 : 버거, 음료, 사이드, 디저트
#총 칼로리를 계산하는 프로그램을 작성
#첫 줄: 버거/ 두번째 줄: 사이드/ 세번째 줄: 음료/ 네번째 줄: 디저트

#고객은 각 옵션에서 정확히 하나의 숫자를 선택해야 함
burger_choice = int(input())
if burger_choice < 1 or burger_choice > 4:
    exit("1,2,3,4 옵션 중 하나를 선택해 주세요.")

side_choice = int(input())
if side_choice < 1 or side_choice > 4:
    exit("1,2,3,4 옵션 중 하나를 선택해 주세요.")

drink_choice = int(input())
if drink_choice < 1 or drink_choice > 4:
    exit("1,2,3,4 옵션 중 하나를 선택해 주세요.")

dessert_choice = int(input())
if dessert_choice < 1 or dessert_choice > 4:
    exit("1,2,3,4 옵션 중 하나를 선택해 주세요.")

# 선택한 옵션의 칼로리
if burger_choice == 1:
    burger_calorie = 461
elif burger_choice == 2:
    burger_calorie = 431
elif burger_choice == 3:
    burger_calorie = 420
elif burger_choice == 4:
    burger_calorie = 0

if side_choice == 1:
    side_calorie = 100
elif side_choice == 2:
    side_calorie = 57
elif side_choice == 3:
    side_calorie = 70
elif side_choice == 4:
    side_calorie = 0

if drink_choice == 1:
    drink_calorie = 130
elif drink_choice == 2:
    drink_calorie = 160
elif drink_choice == 3:
    drink_calorie = 118
elif drink_choice == 4:
    drink_calorie = 0

if dessert_choice == 1:
    dessert_calorie = 167
elif dessert_choice == 2:
    dessert_calorie = 266
elif dessert_choice == 3:
    dessert_calorie = 75
elif dessert_choice == 4:
    dessert_calorie = 0

#전체 칼로리 계산
total_calorie = burger_calorie + side_calorie + drink_calorie + dessert_calorie
print("Your total Calorie count is", total_calorie)