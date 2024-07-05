#문제 url : https://dmoj.ca/problem/dmopc16c1p0
#C.C의 만족도 : absolutely // a width of 3 units and an extra-cheesiness of at least 95%
# fairly // a width of 1 units and an extra-cheesiness of at least 50%
# very // 다른 피자들..

#결과 : C.C의 만족도를 "C.C. is M satisfied with her pizza"로 나타내라. // 공백과 온점을 정확히 표현할 것
# M : C.C.의 만족도를 나타내는 문자열, absolutely, fairly, very 중 하나

#첫 줄: C.C가 받게될 피자의 가로 , 정수, 1~3 사이(포함)
pizza_width = input()
if not pizza_width.isdigit():
    exit()
pizza_width = int(pizza_width)
if not 1 <= pizza_width <= 3:
    exit()

#피자가 엑스트라 치즈로 덮인 퍼센트, 정수, 0~100사이(포함)
pizza_extracheese = input()
if not  pizza_extracheese.isdigit():
    exit()
pizza_extracheese = int(pizza_extracheese)
if not 0 <= pizza_extracheese <= 100:
    exit()

M = str()
if pizza_width == 3 and pizza_extracheese >= 95:
    M = "absolutely"
elif pizza_width == 1 and pizza_extracheese <= 50:
    M = "fairly"
else:
    M = "very"

print("C.C. is " + M + " satisfied with her pizza.")
