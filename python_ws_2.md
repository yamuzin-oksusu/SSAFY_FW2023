### iterable

iterable 한지 판별할 수 있는 방법: for roof 이용
```
for val in [1,2,3]:
    print(val)

dic = {1:'a',2:'b',3:'c'}

for key in dic:
    print(key,d[key])
```

### 0718 review
비교연산자는 datatype 구분하지 않지만 is , is not은 datatype까지 구분함
```
print(2.0 == 2) # >> True
print(2.0 is 2) # >> False
```

## 단축평가 
논리 연산에서 두 번째 피연산자를 평가하지 않고 결과를 결정하는 동작
```
# 실수는 0을 제외하고는 모두 True
bool(100) # >> True 
bool(0) # >> False

# 문자열도 empty 문자 제외하고 모두 True
bool("") # >> False

#빈 list 만 False
arr = []
bool(arr) # >> False

# T and T 일 때는 뒤에 있는 값을 전체 결과로 인식
1 + 2 and 'a' # >>  'a'

# F and T(or F) 일 때는 앞에 있는 값을 전체 수식의 결과로 인식
1-1 and 'b' # >> 0

# T and F 일 때 F 값을 결과로 인식
3 and [] # >> []
```
파이썬에서는 T/F로 판단되지 않는 값도 T/F로 변환
```
vowels = 'aeiou'

print(('a' and 'b') in vowels) 
# >> False (b가 vowels 안에 있는지 판단)
print(('b' and 'a') in vowels) # >> True (a가 vowels 안에 있는-지 판단)
```

