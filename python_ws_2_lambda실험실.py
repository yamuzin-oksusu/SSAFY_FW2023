## 간단한 수식 표현

# 합
print((lambda x , y : x + y)(10, 20)) # 30
print((lambda x , y : x + y , 10, 20)) # (<function <lambda> at 0x000001A202A0F280>, 10, 20)
# print((lambda x , y : x + y)[10, 20]) # error
   # 람다를 한 줄의 함수 개념이라고 생각하자
sum_ab = lambda x, y : x+y
print(sum_ab(1,2)) # 3

## lambda + map

  # map(lambda함수,시퀀스)형식으로 쉽게 사용이 가능하다

# range(n)으로 시퀀스 할당
print(list(map(lambda x : x**2 , range(5)))) # [0, 1, 4, 9, 16]

# list 순회하기
numbers = [1,2,5,7,9]
print(list(map((lambda x : f'{x} 값'),numbers))) # ['1 값', '2 값', '5 값', '7 값', '9 값']

# ws_3_5
  # info = 신규 고객의 이름과 나이를 담은 딕셔너리  

many_user = [{'name': '김시습', 'age': 20, 'address': '서울'}, 
{'name': '허균', 'age': 16, 'address': '강릉'}, {'name': '남영로', 'age': 52, 'address': '조선'},
{'name': '임제', 'age': 36, 'address': '나주'}, {'name': '박지원', 'age': 60, 'address': '한성부'}]


print(list(map((lambda x : {'name' : x['name'], 'age':x['age']}),many_user)))
 # [{'name': '김시습', 'age': 20}, {'name': '허균', 'age': 16}, 
 # {'name': '남영로', 'age': 52}, {'name': '임제', 'age': 36}, 
 # {'name': '박지원', 'age': 60}]