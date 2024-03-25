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
#         print('%s 는(은) 남자입니다' % name)
#     else :
#         print('%s 는(은) 여자입니다' % name)

# person('길동')

add = lambda a,b : a+b
print(add(10,3))