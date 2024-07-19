#url : https://dmoj.ca/problem/coci08c3p2
#모음: a,e,i,o,u  뒤에  p + 모음 ektl cnrk

encode_sentence = input()
if encode_sentence.isupper():
    exit()
if not len(encode_sentence) <= 100:
    exit()

decode_sentence = " "
i = 0

while i < len(encode_sentence):
    decode_sentence = decode_sentence + encode_sentence[i]
    if encode_sentence[i] in "aeiou":
        i = i + 3
    else:
        i = i + 1
print(decode_sentence)