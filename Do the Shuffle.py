#문제 url :https://dmoj.ca/problem/ccc08j2

songs = 'ABCDE'

button = 0

while button != 4:
    button = input()
    if not (len(button) == 1 and button in "1234"):
        exit()
    presses = input()
    if not presses.isdigit():
        exit()
    presses = int(presses)
    if not 1 <= presses <= 10:
        exit()
    if button == "1":
        p = presses % 5
        songs = songs[p] + songs[(p+1)%5] + songs[(p+2)%5] + songs[(p+3)%5] + songs[(p+4)%5]
    elif button == "2":
        p = presses % 5
        songs = songs[-p] + songs[-p+1] + songs[-p+2] + songs[-p+3] + songs[-p+4]
    elif button == "3":
        if presses % 2 == 1:
            songs = songs[1] + songs[0] + songs[2:]
    else: #button == 4
        break

output = " "
for song in songs:
    output = output + song + " "

print(output[1:-1])