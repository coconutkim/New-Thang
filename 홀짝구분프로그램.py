# 자연수(1,2.3, ....)
# 홀수는 1, 3, 5, ....
# 짝수는 2,4,6,....

# 2로 나누어서 나머지가 0이면 짝수
# 2로 나누어서 나머지가 0이 아니면 홀수

num = int(input('number:'))

if num % 2 == 0:
    print('짝수')

# elif num % 2 != 0:
#     print('홀수')

else:
    print('홀수')