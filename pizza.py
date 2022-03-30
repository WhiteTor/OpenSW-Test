import random

pizza = ['파파존스 마가리타 피자', '뽕뜨락 피자 모모스테키', '미스터 피자 슈퍼 콤보', '뽕뜨락 피자 코코쉬림프',
         '미스터 피자 페퍼로니 피자', '미스터 피자 시카고 딥', '미스터 피자 포테이토 골드', '미스터 피자 불고기 피자', '하와이안 피자',
         '민트초코 오레오 피자']

print('오늘에 피자 추천기\n오늘의 피자는?')

rand = random.randrange(0, len(pizza))

print(pizza[rand])

if rand >= 8:
    print('저런!')
