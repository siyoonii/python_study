#문제url : https://dmoj.ca/problem/wc17c3j3
#password 조건 : 문자열, 8~12자(숫자,소문자,대문자), 최소 3개의 소문자, 최소 2개의 대문자, 최소 1개의 숫자
#준비한 패스워드 : 적어도 100개의 문자,  비어 있지 않은 문자열은 최대 2개로 구성됩니다. 각 문자는 소문자, 대문자 또는 숫자입니다.
#valid 또는 Invalid 로 표시

password = input()

lower = 0
upper = 0
digit = 0
others = 0

for char in password:
    if char.islower():
        lower = lower + 1
    elif char.isupper():
        upper = upper + 1
    elif char.isdigit():
        digit = digit + 1
    elif char.islower() or char.isupper() or char.isdigit():
        others = others + 1

if not 8 <= len(password) <= 12:
    print("Invalid")
elif not 3 <= lower:
    print("Invalid")
elif not 1 <= digit:
    print("Invalid")
elif not 2 <= upper:
    print("Invalid")
else:
    print("Valid")



