#학과: 컴퓨터공학부

#이름: 김민우

#학번: 202100613

#좋아하는 음식: 뿌링뿌링 뿌링클, 피자

#피자는 좋아하시나요?

#Fork 이후 수정했는데 반영이 될까?

#Fork 이후 수정한 부분입니다!

from random import randrange

print('제 학과가 무엇입니까?') # 퀴즈 1: 학과

if input() == '컴퓨터공학부':
  print('정답입니다.')
else:
  print('오답입니다.')
  
print('\n제 이름이 무엇입니까?') # 퀴즈 2: 이름

if input() == '김민우':
    print('정답입니다.')
else:
    print('오답입니다.')
    
favFoodList = ['뿌링뿌링 뿌링클', '피자']
foodList = ['떡볶이', '냉면']

print('\n다음 리스트 중 제가 좋아하는 음식은?') # 퀴즈 3: 좋아하는 음식
ans = favFoodList[randrange(0,2)]
foodList.append(ans)
for i in foodList:
    print(i)

if input() == ans:
    print('정답입니다.')
else:
    print('오답입니다.')
