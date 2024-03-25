# a = 10  # 변수 선언
# b, c = (10, 20)  # 튜플을 이용한 각각 값 할당
# [d, e] = [10, 20]  # 리스트를 이용한 각각 값 할당
# f = g = 30  # f,g에 똑같은 값을 할당
# h = None  # 비어있는 변수를 할당
# print("재할당 전 : ", h)
# h = 40  # 변수 재할당
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print("재할당 : ", h)

# --------------------------------------------------

# a = [10, 20, 30]
# b = a
# print(a == b)  # true
# a[0] = 200

# print(b)  # [200, 20, 30] 이 출력된다. 값을 저장하는 것이 아닌 a의 주소를 바라보기 때문에 같이 변한다.
# #
# c = [10, 20, 30]
# d = c[:]  # 슬라이싱으로 리스트 전체 아이템 반환(복사)
# c[0] = 100
# print("c의 값은 ? : ", c) # [100, 20, 30]
# print("d의 값은 ? : ", d) # [10, 20, 30]

# --------------------------------------------------

# a = 30
# b = 4
#
# print(a / b)  # 7.5
# print(a // b)  # 7 몫 구하기
#
# a = '자몽'
# print(a * 2)  # 자몽자몽

# c = 1234
# print(str(c)[0])  # 숫자는 문자열로 변환 후 인덱스 출력 가능

# d = '개발자 자몽'
# print(d[0:3:])  # [이상:미만:간격] -> 0이상 4미만 간격없이 -> 개발자 
# print(d[::2])  # 전체 간격 2칸씩 -> 개자자
#
# print(d.count('자'))  # 변수 d에 대한 '자' 개수 반환 -> 2
# print(d.find('이'))  # 변수 d에 대한 '이' 값의 인덱스 반환 , '이'가 2개 있지만 첫 인덱스인 2를 반환
# print(d.find('히'))  # 변수 d에 대한 값이 없을때 -1 반환 -> -1


#
# e = '개발자 자몽'
# split_e = list(e)  # js에서 split("") 랑 동일
# print(split_e)  # ['개', '발', '자', ' ', '자', '몽']
# print(''.join(split_e))  # 개발자 자몽

# --------------------------------------------------

# a = '2024'
# b = ','.join(a)  # '2, 0, 2, 4' 가 출력
# print(','.join(a))  # 문자열을 쪼개서 그 사이에 ''에 있는것을 삽입한다. -> 2,0,2,4
#
# c = 'BIGDATA'
# print(c.lower())  # bigdata 소문자로 변환해 출력
#
# d = "apple"
# print(d.upper())  # APPLE 대문자로 변환해 출력
#
# f = 'ABZCDZEF'
# print(f.split('T'))
# e = '   abc   def   '
# print(e.split())  # 연속된 공백을 하나의 공백으로 간주하여 분할 -> ['test', 'test']
# print(''.join(e.split()))
# #
# ta = e.split(' ') # 문자열의 시작과 끝에 있는 공백은 무시되고 중간에 있는 공백이 구분자로 간주된다.
# print(ta) # ['', '', '', '', 'test', '', '', '', 'test', '', '', '', '']
# result = filter(None, ta)  # filter 가 반환하는 값은 이터레이터 객체이기 때문에 list 로 배열로 변환 후 출력해야 표시된다.
# print("result : ", list(result))
# #
# f = '    zamong    '
# print("공백 제거 전", f)
# print("양쪽 공백 제거", f.strip())
# print("왼쪽 공백 제거", f.lstrip())
# print("오른쪽 공백 제거", f.rstrip())
# #
# g = '나는 사과를 좋아한다 사과'
# print(g)
# print(g.replace('사과', '포도', 1))  # replace('바뀌는 내용','바뀔 내용',바꿀 개수)
# print(g.replace('사과','포도'))
# -> 나는 포도를 좋아한다 사과 (개수를 안쓰면 전체 바꾸기)

# --------------------------------------------------

# a = ['가','나','다','라']
# # print(len(a)) # len : 배열의 길이 반환 -> 4
# # print(a[:])
# # print(a[0:])  # 위, 아래의 결과값이 같다

# a[0] = '까'
# print(a) # ['까','나','다','라']

# a.append('마')
# print(a) # ['까','나','다','라','마']

# a.insert(1,'사')
# print(a) # ['까','사','나','다','라','마']

# a.remove('까')
# print(a) # ['사','나','다','라','마']

# a.sort()
# print(a) # ['나','다','라','마','사']

# a.reverse()
# print(a) # ['사', '마', '라', '다', '나']

# print(a.index('라'))

#
# b = ['짱구', '유리', '철수', '맹구', [2023, 2024]]
# print(b[4][:])  # [2023, 2024]
#
# c = ['가', '나']
# d = ['다', '라']
# print(c + d)  # ['가', '나', '다', '라']
#
# a[0] = '흰둥이'  # 배열 값 수정 -> ['흰둥이', '유리', '철수', '맹구']
# print(a)
#
# a.append('짱구')  # 배열에 값 추가하기 맨 끝에 추가 됨 -> ['흰둥이', '유리', '철수', '맹구', '짱구']
# print(a)
#
# a.insert(1, '원장선생님')  # 원하는 인덱스에 값 추가
# # -> ['흰둥이', '원장선생님', '유리', '철수', '맹구', '짱구']
# print(a)
#
# a.remove('원장선생님')
# print(a)  # 배열 값 삭제하기 -> ['흰둥이', '유리', '철수', '맹구', '짱구']
#
# a.sort()
# print(a)  # 배열 데이터 정렬 -> ['맹구', '유리', '짱구', '철수', '흰둥이']
#
# a.reverse()
# print(a)  # 기존 데이터 순서를 뒤집는다 -> ['흰둥이', '철수', '짱구', '유리', '맹구']
#
# print(a.index('짱구'))  # 배열 값이 어느 인덱스에 있는지 인덱스 값 반환

# --------------------------------------------------

# 튜플과 리스트의 차이점
# 리스트는 [], 튜플은 () -> 리스트의 값은 수정할 수 있지만, 튜플을 값을 변경할 수 없다.
# 변경여부가 가장 큰 차이점이고, 프로그램이 실행되는 동안 값이 변경되면 안되는 경우 튜플을 사용한다.
# 튜플은 리스트에 비해 더 적은 메모리를 필요하고, 속도가 빠르다는 장점이 있다.


# t1 = ()  # 빈 튜플 만들기
# t2 = (1,)  # 한개의 데이터가 있는 튜플 -> 튜플이 1개의 데이터만 가질 때는 뒤에 꼭 콤마를 붙여줘야 한다.
# t3 = (1, 2, 3)  # 숫자형 데이터가 들어있는 튜플
# t4 = 1, 2, 3  # 괄호()를 생략해도 튜플로 만들어진다.
# t5 = ('가', '나', '다')  # 문자열 튜플
# t6 = (1, '가', 2, '나')  # 숫자와 문자열 혼합 튜플
# t7 = (1, 2, (3, 4))  # 튜플안에 또 다른 튜플
# print(len(t5))
# print(t5[0])
# print(t5[:])

# a = (1,2,3)
# b = (1,2,3)
# print(a+b) # (1,2,3,1,2,3)

# a =('가','나','다','가')
# print(a.index('가')) # 0
# print(a.count('가')) # 2

# a = ('가','나','다')
# print(list(a))
# print(tuple(a))
#

# a = ('짱구', '유리', '철수', '맹구')
# print(a[0])  # 튜플을 인덱싱 할때는 [] , 배열과 동일 -> 짱구
# print(a[1:])  # ('유리', '철수', '맹구')
#
# print(t3 + t4)  # 튜플 합치기  -> (1, 2, 3, 1, 2, 3)
# print(len(t3 + t4))  # 튜플 길이 구하기 -> 6
#
# # ⭐ 튜플은 수정이 불가능하기 때문에 수정, append, insert, remove, sort, reverser 등 사용이 불가하다.
#
# print(a.index('짱구'))  # 튜플의 값 인덱스 반환 -> 0
# print(a.count('짱구'))  # 튜플의 값 개수 반환 -> 1
#
# # 주의사항 괄호가 두개다 list(()), tuple(())
# print(list((a)))  # 튜플을 리스트로 변환 -> ['짱구', '유리', '철수', '맹구']
# print(tuple((a)))  # 리스트를 튜플로 변환 -> ('짱구', '유리', '철수', '맹구')

# --------------------------------------------------

# # 딕셔너리 JS의 객체가 비슷한 개념
# school = {'A반': ['짱구', '맹구'], 'B반': ['철수', '유리']}
# class_A = {1: '짱구', 2: '맹구'}
#
# print(school)
# print(class_A)
#
# # school_list = {['A반', '남자']: ['짱구', '맹구'], ['A반', '여자']: ['짱아', '유리']}
# # -> 리스트는 값이 변할 수 있기에 딕셔너리의 키로 사용될 수 없다.
#
# school_list = {('A반', '남자'): ['짱구', '맹구'], ('A반', '여자'): ['짱아', '유리']}
# # -> 반면, 튜플은 값이 변하지 않기에 딕셔너리의 키로 사용될 수 있다.
#
# # 딕셔너리 값 출력방법
# print(school['A반'])  # 첫번째 대괄호를 이용한 출력 방법 -> ['짱구', '맹구']
# print(school.get('A반'))  # 두번째 변수.get()을 이용한 출력 방법 -> ['짱구', '맹구']
#
# print((school.values()))  # 딕셔너리에 있는 모든 value값 가져오기 -> dict_values([['짱구', '맹구'], ['철수', '유리']])
# print(list((school.values())))  # 튜플 형태를 리스트로 변환 -> [['짱구', '맹구'], ['철수', '유리']]
#
# print(school.keys())  # 딕셔너리의 모든 key값 가져오기 -> dict_keys(['A반', 'B반'])
# print(list((school.keys())))  # 튜플 형태를 리스트로 변환 -> ['A반', 'B반']
#
# del school['B반']  # 딕셔너리의 요소 삭제 del 변수[key]
# print(school)  # -> {'A반': ['짱구', '맹구']}
#
# # 딕셔너리 값 수정
# school['A반'] = ['짱구', '맹구', '훈이']
# print(school)  # -> {'A반': ['짱구', '맹구', '훈이']}
#
# # 딕셔너리의 key와 value 를 쌍으로 출력
# print(school.items())  # -> dict_items([('A반', ['짱구', '맹구', '훈이'])])
#
# # 딕셔너리의 모든 값을 지우고 싶을 때
# print(school.clear())  # -> None

num = {'a' : [1,2,3], 'b' : [4,5,6], 'c' : 7}
# print ( num.items())
# print ( list(num.items()))
num['a'] = 4
print(num)

del num['c']
print(num)
print(num.clear()) # None

# # num = {('num','even') : [2,4]}
# # num = {['num','even'] : [2,4]}
# print(num['a']) # [1,2,3]
# print(num.get('a')) #[1,2,3]


# print(num.values())
# print(num.keys())

# print(list(num.values()))
# print(tuple(num.keys()))



# --------------------------------------------------

# set 란 ? 데이터를 집합의 형태로 값을 저장
# set의 핵심은 요소들의 중복을 허용하지 않는다,
# 데이터들 간의 순서가 없기 떄문에 리스트나 튜플 자료형처럼 인덱싱이나 슬라이싱을 이용해 값을 추출하는 방법을 사용할 수 없다.

# s1 = set()  # 빈 세트 만들기
# s2 = set([1, 2, 3])  # set() 안에 리스트를 넣어 세트를 만든다
# s3 = set({1,2,3,1,2,3})
# s4 = set([1,2,3,1,2,3])
# s5 = set((1,2,3,1,2,3))
# s6 = {1,2,3,1,2,3}
# print(s3)
# print(s4)
# print(s5)
# print(s6)
# print(list(s3))  # 중복요소를 제거한 후 배열로 변환 -> [1, 2, 3, 4]
# s4 = {1, 2, 3}  # 중괄호로 세트 선언
#
# s5 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# s6 = {2, 4, 6, 8, 10}
# # 세트의 연산
# # 교집합 A&B , A.intersection(B)
# print(s5 & s6)  # -> {2, 4, 6, 8, 10}
# print(s5.intersection(s6))  # -> {2, 4, 6, 8, 10}
#
# # 합집합 A|B , A.union(B)
# print(s5 | s6)  # -> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(s5.union(s6))  # -> {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#
# # 차집합 A-B , A.difference(B)
# print(s5 - s6)  # -> {1, 3, 5, 7, 9}
# print(s5.difference(s6))  # -> {1, 3, 5, 7, 9}
#
# # 교집합을 뺀 나머지 (합집합 - 교집합)
# print(s5 ^ s6)  # -> {1, 3, 5, 7, 9}
#
# s6.add(11)  # add함수 : 세트에 1개의 값 추가
# print(s6)  # -> {2, 4, 6, 8, 10, 11}
#
# s6.update([3, 5])  # 세트에 여러개 값을 리스트로 추가
# print(s6)  # -> {2, 3, 4, 5, 6, 8, 10, 11}
#
# s6.remove(11)  # 세트에 1개의 값을 삭제
# print(s6)  # -> {2, 3, 4, 5, 6, 8, 10}

# s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# s2 = {2, 4, 6, 8, 10}

# print (s1 & s2)
# print (s1.intersection(s2))

# print(s1 | s2)
# print(s1.union(s2))

# print (s1 - s2)
# print (s1.difference(s2))
# print (s1 ^ s2)

# s2.add(11)
# print (s2) #

# s2.update([3,5])
# print (s2)

# s2.remove(11)
# print (s2)
# s2.update([3, 5]) 
# print (s2)
# s2.update((3, 5))
# print (s2)
# s2.update({3, 5})
# print (s2)

# --------------------------------------------------

# if 문 / if, else 옆에 콜론 까먹지 않기 , 들여쓰기 잘하기
# rain = True
# if rain:
#     print('우산 가져가쇼')
# else:
#     print('우산 두고가쇼')
#

# rain = True
# if rain :
# 	print('우산 가져가쇼')
# else :
# 	print('우산 두고가쇼')
# # in
# print('a' in ['a', 'b', 'c'])  # 리스트
# print('a' in ('a', 'b', 'c'))  # 튜플
# print('a' in {'a', 'b', 'c'})  # 세트
# print('a' in 'apple')  # 문자열 모두 가능 !
#
# values = ['a','b','c']
# str = 'apple'
# print ('a' in values)
# print ('a' in str)
# # # pass : 무언가 수행하지 않고 그냥 넘기고 싶을 때
#
# # 여러가지 조건을 판단할 때 elif
# # 마트에 사과가 있으면 사과를 사오고, 사과가 없으면 바나나를 사오고,둘다 없으면 그냥 오는 시나리오 작성
# mart = ['melon', 'pear']
# if 'apple' in mart:
#     print('apple 구매 완료')
# elif 'banana' in mart:
#     print('banana 구매 완료')
# else:
#     print('그냥 집에 옴')

# mart = ['melon','pear']

# if 'apple' in mart :
# 	print('apple 구매 완료')
# elif 'banana' in mart :
# 	print('bananna 구매 완료')
# else :
# 	pass
#
# # 성적 산출 프로그램 작성
# # 100 ~ 90 A / 89 ~ 80  B / 79 ~ 70 C / 나머지 D
#
# score = int(input('성적을 입력하시오'))
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# else:
#     print('D')
# score = int(input('성적을 입력하시오'))
# if score >= 90 :
# 	print ('A')
# elif score >=80 :
# 	print ('B')
# elif score >= 70 :
# 	print ('C')
# else :
# 	print('D')
# --------------------------------------------------

# while 문 / 조건문 끝에 콜론 과 들여쓰기 신경쓰기
# num = 0
# while num <= 10:
#     print(num)
#     num += 1

# 배열에 있는 리스트 요소 출력하기
# a = [1, 2, 3, 4, 5]
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# while문 강제로 빠져나가기 break
# book = 10
# people = 20
# while people:
#     book -= 1
#     print('남은 책은 %d 권 입니다.' % book)
#     if book == 0:
#         print('책이 모두 소진되었습니다.')
#         break

    
# while문 맨 처음으로 돌아가기 continue
# 1~10 홀수만 출력하기
    
# a = 0
# while a < 10:
#     a += 1
#     if a % 2 == 0:
#         continue
#     print(a)

# for 문
# a = {1,2,3}
# for i in a :
#     print(i)
# people = ['김', '이', '박']
# people = [i + '씨' for i in people]
# print(people)  # -> ['김씨', '이씨', '박씨']


# for문을 이용한 합격 여부 판단( 조건 : 80점 이상 합격)
# students = [75, 80, 93]
# for i in students:
    
#     if i >= 80:
#         print('%d 번 학생 합격' % (students.index(i)+1))
#     else:
#         print('%d 번 학생 불합격' % (students.index(i)+1))

# # for문을 이용한 배열안의 문자열 길이 구하기
# fruit = ['사과', '바나나', '딸기', '파인애플']

# fruit_value_leng = [len(i) for i in fruit]
# print(fruit_value_leng)
#
# # for문을 이용한 배열안의 문자열 소문자에서 대문자로 변환
# eng_fruit = ['apple', 'banana', 'strawberry', 'fineapple']
# eng_fruit = [i.upper() for i in eng_fruit]
# print(eng_fruit)

# for문에서 continue 사용
# students = [75, 80, 93]
# number = 0
# for i in students:
#     number += 1
#     if i < 80:
#         continue
#     print('%d 번 학생 합격' % number)
# fruits = ['사과','바나나','딸기','파인애플']
# fruits_len = [len(i) for i in fruits]
# print(fruits_len)

# fruits = ['apple','bananan','strawberry','fineapple']
# upper_fruits = [i.upper() for i in fruits]
# print(upper_fruits)
#

# # for문과 range함수
# # range 는 range(1,10) 이런식으로 사용되는데 (이상, 미만) / 1이상 10미만 이라는 뜻
# for i in range(1, 10):
#     print(i)  # -> 1~9 까지 출력

# for i in range(1,10) :
# 	print(i)
     
# sum = 0
# for i in range(1,10) :
# 	sum += i
# print(sum)
#
# # range 함수를 이용해 1~10 까지 더해보자
#
# sum = 0
# for i in range(1, 11):
#     sum += i
# print(sum)
#
# # 구구단 만들기
# for i in range(2, 10):
#     for j in range(1, 10):
#         print('%d * %d = %d' % (i, j, (i * j)))
#
# for문으로 리스트 만들기
# a라는 배열에 각 요소에 10을 곱하여 새로운 배열 만들기
# a = [1, 2, 3]
# b = [i * 10 for i in a] -> 리스트 컴프리헨션(comprehension)
# print(b)  # -> [10, 20, 30]

# # 1~10 사이에 짝수인 인자를 2 로 나눴을 때 몫을 구한 배열만들기
# newArr = [i // 2 for i in range(1, 11) if i % 2 == 0]
# newArr = [i // 2 for i in range(1,11) if i % 2 == 0]
# print(newArr)  # ->[1, 2, 3, 4, 5]

# # # range 문을 활용해 구구단 값을 담은 배열 만들기

# for i in range(2,10) :
# 	for j in range(1,10) :
#             print('%d * %d = %d' % (i , j , (i*j)) , end='\n')

# box = [str(i) + '*' + str(j) + '=' + str(i * j) for i in range(2, 10) for j in range(1, 10)]
# print(box)
