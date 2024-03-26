# def add(a,b) :
# 	return a+b
    
# a = 3 
# b = 1
# c = add(a,b)
# print(c) # 4

# def say() :
# 	'hi'
# say()

# def sub(a,b) :
# 	return a-b

# print(sub(a=3, b=1))
# print(sub(b=1, a=3))

# def add_many (*args) :
# 	result = 0
# 	for i in args :
# 		result += i
# 	return result

# def add_many(*args): 
#     print(type(args))
#     result = 0 
#     for i in args: 
#         result = result + i   
#     return result 

# # # print(add_many(1,2,3))
# # print(add_many(*[1,2,3,4]))
# print(add_many(*(range(1,11))))

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key, value in my_dict.items():
#     print(key, value)


# def add_sub(type, *args) :
#     result = 0
#     if type == 'add' :
#           for i in args :
#             result += i
#     else :
#         for i in args :
#             result -= i
    
#     return result


# print(add_sub('add',1,2,3,4,5)) # 15
# print(add_sub('sub',1,2,3,4,5)) # -15

# def print_keyword (**kwargs) :
#     print(kwargs)

# print_keyword(a=3 ,b=2)

# def add_sub(a,b) :
#     return a+b , a-b

# print(add_sub(10,3)) # (13, 7)


# def person(name, man=True) :
#     if man == True :
#         print('%s 는(은) 남자입니다' % name)=ㅇ13

#     else :
#         print('%s 는(은) 여자입니다' % name)

# person('길동')

# add = lambda a,b : a+b
# print(add(10,3))

# --------------------------------------------

# print('life '+'is '+'too short')

# number = input('숫자를 입력하시오 : ')
# print(number) # input에 입력되는 모든 것은 문자열로 취급한다.

# print('hello','world') # , 를 쓰면 띄어쓰기가 된다.

# for i in range(1,11) :
#     print(i, end='!') # end의 초기값이 줄바꿈이기 때문에 end의 값을 바꿔주면 요소에 따라 출력이 된다.
#     # 1!2!3!4!5!6!7!8!9!10!

# #---------------------------------------------
# f = open('새파일.txt','r')
# f.close()

# open(파일_이름, 파일_열기모드) # 파일을 생성하기 위한 파이썬 내장 함수
# r - 읽기 모드 : 파일을 읽기만 할 때 사용
# w - 쓰기 모드 : 파일에 내용을 쓸 때 사용
# a - 추가 모드 : 파일의 마지막에 새로운 내용을 추가할 때 사용

# f = open('C:\\test\\test.txt','w')  # 역슬래쉬 이용시에는 2개 써야함.
# f = open('C:/test/test.txt','w') 

# for i in range(1,11) :
#     data = '%d번째 줄입니다 \n' % i
#     f.write(data) # write 내장 함수로 파일에 데이터 입력
# f.close() # 열려 있는 파일 객체를 닫아 주는 역할 / 프로그램을 종료할 때 파이썬이 열려 있는 파일의 객체를 자동으로 닫아주기에 생략해도 되지만 직접 닫아주는게 좋음


# f = open('C:/test/test.txt','r')
# line = f.readline()  # readline 은 파일의 첫번째 줄을 읽어 출력함
# line = f.readline()  # readline 은 파일의 첫번째 줄을 읽어 출력함
# while True :
#     line = f.readline()
#     if not line : break
#     print(line)
# f.close()

# print(line)
# lines = f.readlines()
# for line in lines:
#     line = line.strip() # 줄 끝에 \n 가 있기 때문에 빈줄이 같이 출력되는데 그걸 없앤다.
#     print(line)
# f.close()

# data = f.read() # 파일의 내용 전체를 문자열로 리턴
# print(data)
# print(data.split(' \n'))
# f.close()

# for line in f:
#     print(line)
# f.close()


# f = open('C:/test/test.txt','a')

# for i in range(11,20) :
#     data = "%d번째 줄입니다 \n" % i
#     f.write(data)
# f.close()

# with open('C:/test/test.txt','w') as f :
#     f.write('hello world')

# ---------------------------
# import sys # 프로그램의 입출력 도와주는 프로그램

# args = sys.argv[1:]
# for i in args :
#     print(args)
#     print(i.upper(), end=' ')

# class FourCal :
#     def setdata(self, first, second) :
#         self.first = first
#         self.second = second

#     def add (self) :
#         result = self.first + self.second
#         return result
    
#     def sub (self) :
#         result = self.first - self.second
#         return result
    
# a = FourCal()
# # a.setdata(4,2) # setdata가 없으면 초기화를 하지않았기 때문에 오류가 난다
# print(a.add())
# print(a.sub())

# 생성자를 통해서 초기값을 설정하지않아도 되게끔 클래스 만들기

# class FourCal2 :

#     def __init__(self, first, second) :
#         self.first = first
#         self.second = second

#     def add(self) :
#         return self.first + self.second
#     def div(self) :
#         return self.first / self.second

# b = FourCal2(4,2)

# print(b.add())

# class MoreFourCal2(FourCal2) : # 클래스 상속
#     def pow(self) :
#         return self.first ** self.second

# c = MoreFourCal2(10,3)

# print(c.add())
# print(c.pow())

# d = FourCal2(4,0)
# # print(d.div()) # Zerodivision 오류

# # 메서드 오버라이딩 : 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는것을 오버라이딩
# class safeFourCal(FourCal2) :
#     def div(self):
#         if self.second == 0 :
#             return 0
#         else :
#             return self.first / self.second
        
# e = safeFourCal(4,0)
# print(e.div())

class Family :
    lastname = '이'

a = Family()
b = Family()

print(a.lastname) # 이
print(b.lastname) # 이

a.lastname = '김'

print(a.lastname) # 김 Family의 lastname이 바뀌는것이 아니라 a 객체에 lastname이라는 객체변수가 새롭게 생성된다. 객체변수는 클래스변수와 동일한 이름으로 생성 가능
print(b.lastname) # 이
